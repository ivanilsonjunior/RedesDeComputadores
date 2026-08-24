"""
Servidor Web de Texto-para-Fala (TTS) com Flask e RHVoice
SideQuest — Redes de Computadores / ADS
DIATINF — IFRN

Objetivo:
    Demonstrar um serviço web simples de conversão de texto em áudio
    (Text-to-Speech). O usuário digita um texto no navegador, o servidor
    Flask sintetiza o áudio com o RHVoice e devolve uma página que já
    reproduz o resultado automaticamente.

Conceitos reforçados:
    - servidor HTTP com Flask (rotas GET/POST)
    - formulário HTML enviando dados via POST
    - geração de conteúdo binário (áudio WAV) em memória, sem gravar em disco
    - streaming de um arquivo de resposta com send_file()

Dependências:
    - Flask                          -> pip install flask
    - rhvoice-wrapper                -> pip install rhvoice-wrapper
    - Motor RHVoice instalado no sistema (Ubuntu/Debian):
          sudo apt install librhvoice-dev rhvoice rhvoice-brazilian-portuguese
      (veja o README.md desta pasta para mais detalhes, incluindo por que
      o pacote librhvoice-dev é necessário e vozes disponíveis)

Execução:
    $ python3 servidor_tts.py

    Se faltar alguma dependência do sistema, o script encerra com uma
    mensagem indicando o que instalar, em vez de um traceback cru.

Teste:
    Abra http://127.0.0.1:5000 no navegador, digite um texto,
    informe o nome de uma voz instalada e clique em "Gerar Áudio".
"""

import sys
import io

from flask import Flask, request, send_file, render_template_string

# Compatibilidade com Python >= 3.14: o rhvoice-wrapper passa o caminho da
# biblioteca como `bytes` para ctypes.CDLL(), mas o Python 3.14 adicionou uma
# checagem interna (`name.endswith(".fwork")`) que só aceita `str`, quebrando
# com TypeError antes mesmo de tentar carregar a lib. Corrigimos aqui,
# decodificando o caminho de volta para `str`, sem precisar alterar o pacote
# instalado.
import rhvoice_wrapper.rhvoice_bindings as _rhvoice_bindings

_original_lib_selector = _rhvoice_bindings._lib_selector


def _lib_selector_compat(lib_path):
    resultado = _original_lib_selector(lib_path)
    return resultado.decode() if isinstance(resultado, bytes) else resultado


_rhvoice_bindings._lib_selector = _lib_selector_compat

from rhvoice_wrapper import TTS  # noqa: E402 (precisa vir depois do patch acima)

app = Flask(__name__)

# Caminhos padrão do pacote RHVoice no Debian/Ubuntu (apt install rhvoice ...).
# O rhvoice-wrapper, por padrão, procura em /usr/local/share|etc/RHVoice, que
# não é onde o apt instala os dados — sem isso o motor "inicializa" mas não
# encontra nenhuma voz/idioma e RHVoice_new_tts_engine falha silenciosamente.
RHVOICE_DATA_PATH = "/usr/share/RHVoice"
RHVOICE_CONFIG_PATH = "/etc/RHVoice"

# Inicializa o motor TTS. Se o RHVoice não estiver instalado corretamente no
# sistema, encerramos com uma mensagem clara em vez de deixar o traceback
# cru do ctypes/rhvoice_wrapper confundir quem for rodar o exemplo.
try:
    tts = TTS(data_path=RHVOICE_DATA_PATH, config_path=RHVOICE_CONFIG_PATH)
except OSError as erro:
    sys.exit(
        "Não foi possível carregar a biblioteca do RHVoice ({erro}).\n"
        "Peça para o administrador instalar o motor de síntese de voz:\n"
        "    sudo apt install librhvoice-dev rhvoice rhvoice-brazilian-portuguese\n"
        "O pacote 'librhvoice-dev' é necessário mesmo em produção: ele traz a\n"
        "biblioteca libRHVoice.so que o rhvoice-wrapper espera encontrar —\n"
        "só 'rhvoice'/'librhvoice-core10' (motor novo, sem essa lib) não bastam.".format(erro=erro)
    )
except RuntimeError as erro:
    sys.exit(
        f"Falha ao inicializar o motor TTS (RHVoice): {erro}\n"
        f"Verifique se {RHVOICE_DATA_PATH!r} e {RHVOICE_CONFIG_PATH!r} existem e\n"
        "contêm os dados de idioma/voz instalados. Se seu RHVoice foi instalado\n"
        "em outro local, ajuste RHVOICE_DATA_PATH/RHVOICE_CONFIG_PATH no topo\n"
        "deste arquivo, ou instale as vozes com:\n"
        "    sudo apt install rhvoice-brazilian-portuguese"
    )
except Exception as erro:
    sys.exit(f"Falha ao inicializar o motor TTS (RHVoice): {erro}")

# Guarda em memória o último áudio gerado, para a rota /audio_stream servir.
# Didático: em uma aplicação real, cada usuário/sessão teria seu próprio
# áudio (ex.: um dicionário indexado por ID de sessão), em vez de uma única
# variável global compartilhada por todos os clientes.
ultimo_audio = None

# Lista de vozes realmente instaladas no RHVoice deste sistema, montada uma
# única vez a partir de tts.voices_info (nome, idioma, sexo, país). Evita que
# o usuário precise digitar o nome exato de uma voz "de cabeça".
VOZES_DISPONIVEIS = sorted(
    tts.voices_info.values(), key=lambda v: (v['lang'], v['name'])
)

# Voz marcada como selecionada por padrão no <select>: a primeira em
# português, se houver, senão a primeira da lista.
VOZ_PADRAO = next((v['name'] for v in VOZES_DISPONIVEIS if v['lang'] == 'pt'), VOZES_DISPONIVEIS[0]['name'])

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Texto para Fala — RHVoice + Flask</title>
</head>
<body>
    <h1>Conversor de Texto em Áudio (Text-to-Speech)</h1>
    <form action="/falar" method="POST">
        <textarea name="texto" rows="4" cols="50">Digite seu texto aqui...</textarea><br>
        <label for="voz">Escolha a voz:</label>
        <select name="voz" id="voz">
            {% for v in vozes %}
                <option value="{{ v.name }}" {% if v.name == voz_selecionada %}selected{% endif %}>
                    {{ v.name }} ({{ v.lang }}-{{ v.country }}, {{ v.gender }})
                </option>
            {% endfor %}
        </select><br>
        <input type="submit" value="Gerar Áudio">
    </form>
    {% if audio_url %}
        <h2>Reproduzir Áudio:</h2>
        <audio controls autoplay>
            <source src="{{ audio_url }}" type="audio/wav">
            Seu navegador não suporta a tag de áudio.
        </audio>
    {% endif %}
</body>
</html>
"""


@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE, vozes=VOZES_DISPONIVEIS, voz_selecionada=VOZ_PADRAO)


@app.route('/falar', methods=['POST'])
def falar():
    global ultimo_audio

    texto = request.form['texto']
    voz = request.form['voz']

    try:
        # tts.get() é o método correto do rhvoice-wrapper para sintetizar e
        # devolver os bytes de áudio de uma vez (note o "format_", não "format").
        audio_bytes = tts.get(texto, voice=voz, format_='wav')
        if not audio_bytes:
            return f"Nenhum áudio gerado — a voz '{voz}' existe e está instalada?"
        ultimo_audio = audio_bytes
        return render_template_string(
            HTML_TEMPLATE, audio_url="/audio_stream", vozes=VOZES_DISPONIVEIS, voz_selecionada=voz
        )
    except Exception as e:
        return f"Erro ao gerar áudio: {e}"


@app.route('/audio_stream')
def audio_stream():
    if ultimo_audio is None:
        return "Nenhum áudio gerado ainda.", 404

    audio_io = io.BytesIO(ultimo_audio)
    return send_file(audio_io, mimetype="audio/wav", as_attachment=False, download_name="output.wav")


if __name__ == '__main__':
    # Roda o app em localhost na porta 5000
    app.run(debug=True, port=5000)
