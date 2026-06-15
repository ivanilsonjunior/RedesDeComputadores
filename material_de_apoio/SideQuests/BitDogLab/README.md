# BitDogLab - Comunicação serial com LED RGB

Este exemplo mostra como controlar a BitDogLab pelo computador usando a porta
serial USB.

A ideia principal é separar o sistema em dois programas:

- `ComunicaçãoSerial/BitDog.py`: roda dentro da BitDogLab, usando MicroPython.
- `ComunicaçãoSerial/Computador.py`: roda no computador, usando Python e a
  biblioteca `pyserial`.

Esta pasta também possui o exemplo `MedidorDeSom`, que usa o microfone da
BitDogLab e a matriz de LEDs 5x5 para criar um medidor visual de volume.

O computador envia comandos de texto pela serial. A BitDogLab recebe esses
comandos, interpreta o texto e liga ou desliga os LEDs conectados aos pinos
GPIO `11`, `12` e `13`.

## Objetivos didáticos

- Entender a diferença entre o programa que roda na placa e o programa que roda
  no computador.
- Usar comunicação serial para trocar mensagens entre dois dispositivos.
- Controlar saídas digitais da BitDogLab usando `machine.Pin`.
- Criar um protocolo simples baseado em comandos de texto.
- Consultar o estado atual de cada LED/pino.
- Ler sensores analógicos da placa, como o microfone.
- Exibir informações físicas usando a matriz de LEDs da BitDogLab.

## Arquivos

### `BitDog.py`

Este arquivo deve ser enviado para a BitDogLab.

Ele faz as seguintes tarefas:

- configura os pinos `11`, `12` e `13` como saídas digitais;
- inicia todos os LEDs apagados;
- espera comandos chegarem pela serial USB;
- interpreta comandos como `SET 11 1`, `ALL 0` e `STATUS`;
- responde pela serial informando se o comando funcionou;
- informa o estado atual de cada LED.

### `Computador.py`

Este arquivo deve ser executado no computador.

Ele faz as seguintes tarefas:

- lista as portas seriais encontradas;
- pede ao usuário a porta da BitDogLab;
- abre a comunicação serial;
- mostra um menu interativo;
- envia comandos para a placa;
- mostra as respostas enviadas pela BitDogLab.

### `MedidorDeSom/BitDogSom.py`

Este arquivo deve ser enviado para a BitDogLab.

Ele faz as seguintes tarefas:

- lê o microfone no GPIO `28`;
- calcula uma estimativa de volume;
- acende a matriz NeoPixel 5x5 no GPIO `7`;
- mostra no terminal serial a amplitude e o volume em porcentagem.

## Protocolo usado

O protocolo deste exemplo é baseado em linhas de texto. Cada comando termina
com uma quebra de linha (`\n`).

| Comando | Significado |
| --- | --- |
| `STATUS` | Consulta o estado dos LEDs |
| `SET 11 1` | Liga o LED do pino 11 |
| `SET 11 0` | Desliga o LED do pino 11 |
| `SET 12 1` | Liga o LED do pino 12 |
| `SET 12 0` | Desliga o LED do pino 12 |
| `SET 13 1` | Liga o LED do pino 13 |
| `SET 13 0` | Desliga o LED do pino 13 |
| `ALL 1` | Liga todos os LEDs |
| `ALL 0` | Desliga todos os LEDs |

Exemplo de resposta da BitDogLab:

```text
OK: pino 11 LIGADO
ESTADO: pino 11=LIGADO, pino 12=DESLIGADO, pino 13=DESLIGADO
```

## Instalação no computador

No computador, instale as dependências do exemplo usando o arquivo
`requirements.txt`:

```bash
pip install -r requirements.txt
```

Em alguns ambientes Linux, pode ser necessário usar:

```bash
python3 -m pip install -r requirements.txt
```

## Como executar

1. Conecte a BitDogLab ao computador usando o cabo USB.
2. Envie o arquivo `ComunicaçãoSerial/BitDog.py` para a BitDogLab.
3. Deixe o programa da BitDogLab em execução.
4. No computador, execute:

```bash
python3 ComunicaçãoSerial/Computador.py
```

5. O programa vai listar as portas seriais encontradas.
6. Digite o número da lista ou o nome completo da porta correspondente à
   BitDogLab.

Exemplos de nomes de porta:

- Windows: `COM3`, `COM4`, `COM5`
- Linux: `/dev/ttyACM0`, `/dev/ttyUSB0`
- macOS: `/dev/tty.usbmodem...`

Exemplo:

```text
33. /dev/ttyACM0 - Board in FS mode - Board CDC
```

Nesse caso, você pode digitar `33` ou `/dev/ttyACM0`.

Depois disso, use o menu para ligar, desligar e consultar os LEDs.

## Menu do computador

```text
1 - Ligar um LED especifico
2 - Desligar um LED especifico
3 - Ligar todos os LEDs
4 - Desligar todos os LEDs
5 - Consultar estado dos LEDs
0 - Sair
```

Quando uma opção é escolhida, o computador envia um comando para a BitDogLab.
Por exemplo, ao escolher ligar o pino `11`, o computador envia:

```text
SET 11 1
```

A placa responde informando se o comando foi aceito e qual é o estado atual dos
três pinos.

## Observações para a aula

Este exemplo usa texto em vez de bytes binários para facilitar a visualização da
comunicação. Isso permite que os alunos testem os comandos manualmente em um
monitor serial, se desejarem.

Os pinos usados neste exemplo são:

| Pino | Função no exemplo |
| --- | --- |
| `11` | LED do RGB |
| `12` | LED do RGB |
| `13` | LED do RGB |

Dependendo da revisão da placa ou da configuração do hardware, as cores reais
do LED RGB podem variar. Por isso, o exemplo identifica os LEDs pelo número do
pino.

## Problemas comuns

### A porta serial não aparece

Verifique se:

- o cabo USB está conectado corretamente;
- o cabo USB permite dados, não apenas carregamento;
- a placa foi reconhecida pelo sistema operacional;
- outro programa não está usando a mesma porta serial.

### Erro ao abrir a porta serial

Feche outros programas que possam estar usando a BitDogLab, como monitor serial,
Thonny, Arduino IDE ou outro terminal.

### O computador envia comando, mas não recebe resposta

Verifique se:

- o arquivo `BitDog.py` está rodando na BitDogLab;
- a porta serial escolhida é a porta correta;
- a placa não está em modo de bootloader;
- o comando enviado termina com quebra de linha.

## Referência da BitDogLab

Documentação oficial da placa:

https://github.com/BitDogLab/BitDogLab/tree/main/doc/Bitdoglab%20V6
