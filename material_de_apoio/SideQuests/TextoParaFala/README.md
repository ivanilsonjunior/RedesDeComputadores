# 🔊 SideQuest — Texto para Fala (Text-to-Speech)

Este SideQuest implementa um **serviço web de conversão de texto em áudio**, usando **Flask** para a camada HTTP e **RHVoice** (via `rhvoice-wrapper`) como motor de síntese de voz.

O usuário acessa uma página no navegador, digita um texto, escolhe uma voz e recebe de volta um player de áudio que já reproduz automaticamente o texto sintetizado — tudo em memória, sem gravar arquivos em disco.

---

## 🎯 Objetivo do SideQuest

Permitir que o aluno:

- Suba um **servidor web com Flask** (rotas GET/POST);
- Envie dados de um **formulário HTML** via POST;
- Gere e sirva **conteúdo binário (áudio)** dinamicamente, sem arquivos temporários;
- Integre uma aplicação de rede com uma biblioteca externa de terceiros (RHVoice).

---

## 🧠 Conceitos de Redes/Aplicação Abordados

- Protocolo HTTP (métodos GET e POST)
- Cliente/servidor via navegador
- Formulários HTML e envio de dados
- Streaming de resposta binária (`send_file`)
- Camada de aplicação servindo mídia (áudio)

---

## 📁 Estrutura da Pasta

```
TextoParaFala/
├── servidor_tts.py
├── requirements.txt
└── README.md
```

---

## 🚀 Como Executar

### 1️⃣ Instale o motor RHVoice no sistema (Ubuntu/Debian)

```bash
sudo apt install librhvoice-dev rhvoice rhvoice-brazilian-portuguese
```

> **Por que `librhvoice-dev`?** Distribuições recentes (ex.: Ubuntu 26.04) empacotam o RHVoice como `librhvoice-core10` + `librhvoice-audio2`, uma reorganização mais nova da biblioteca. O `rhvoice-wrapper` (usado neste exemplo) espera a biblioteca clássica `libRHVoice.so`, que só é instalada via `librhvoice-dev` (que por sua vez traz `librhvoice5`, a versão compatível). Sem esse pacote, o servidor encerra com o aviso `Não foi possível carregar a biblioteca do RHVoice` — instalando esse pacote a mensagem some.
>
> O nome exato dos pacotes de voz também pode variar conforme a distribuição. Consulte a [documentação do RHVoice](https://github.com/RHVoice/RHVoice) para outras vozes/idiomas.

> **Suporte opcional a MP3/Opus:** ao iniciar, o `rhvoice-wrapper` pode avisar `Disable mp3 support - lame not found` / `Disable opus support - opusenc not found`. São só avisos (o servidor continua funcionando normalmente em WAV) — para habilitar esses formatos, instale `sudo apt install lame opus-tools`.

### 2️⃣ Instale as dependências Python

```bash
pip install -r requirements.txt
```

### 3️⃣ Rode o servidor

```bash
python3 servidor_tts.py
```

### 4️⃣ Acesse no navegador

```
http://127.0.0.1:5000
```

Digite um texto, escolha uma voz na lista suspensa (montada automaticamente a partir das vozes instaladas no RHVoice) e clique em **Gerar Áudio**.

---

## ⚠️ Observações Importantes

- A lista de vozes do `<select>` vem de `tts.voices_info`, consultada uma única vez na inicialização do servidor — se você instalar/remover pacotes de voz do RHVoice, reinicie o servidor para atualizar a lista.
- O áudio gerado é guardado em memória em uma única variável global (`ultimo_audio`), compartilhada por todos os clientes — suficiente para fins didáticos, mas não adequado para múltiplos usuários simultâneos em produção.
- `debug=True` é usado apenas para facilitar o desenvolvimento; não deve ser usado em produção.
- Em Python ≥ 3.14, o script já aplica automaticamente um contorno para um bug de compatibilidade do `rhvoice-wrapper` com o novo `ctypes` (ele passava o caminho da lib como `bytes`, o que quebra a partir do 3.14). Se, mesmo assim, o motor não inicializar, o servidor encerra com uma mensagem indicando exatamente o que falta instalar, em vez de um traceback cru.
- O `rhvoice-wrapper` procura os dados de voz por padrão em `/usr/local/share/RHVoice` e `/usr/local/etc/RHVoice`, mas o pacote `apt` instala em `/usr/share/RHVoice` e `/etc/RHVoice`. Sem apontar para os caminhos corretos, o motor "inicializa" só aparentemente e falha com `RHVoice: engine initialization error` mesmo com o RHVoice funcionando via `RHVoice-test`. O script já passa `data_path`/`config_path` corretos (constantes `RHVOICE_DATA_PATH`/`RHVOICE_CONFIG_PATH` no topo do arquivo) — ajuste-as se seu RHVoice estiver instalado em outro lugar.

---

## 💡 Sugestões de Extensão (Desafios)

- Guardar o áudio por sessão/usuário em vez de uma única variável global;
- Permitir escolher o formato de saída (WAV, MP3 via conversão);
- Adicionar um histórico de textos convertidos;
- Expor a conversão como uma API REST (JSON in, áudio out) além da página HTML.

---

## 📚 Aplicação Didática

Este SideQuest pode ser utilizado para:

- Demonstrações em sala de aula de servidores web com Flask;
- Introdução a integração de aplicações de rede com bibliotecas externas;
- Base para projetos de acessibilidade (leitura de texto em voz alta);
- Discussão sobre streaming de mídia via HTTP.

---

**SideQuest desenvolvido para fins educacionais no contexto da disciplina de Redes de Computadores. 🚀**
