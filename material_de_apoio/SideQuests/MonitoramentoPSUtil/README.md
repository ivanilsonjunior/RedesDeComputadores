# Monitoramento de Sistema com psutil

Este projeto é um exemplo didático em Python que utiliza a biblioteca **psutil**
para monitorar recursos do sistema operacional, aplicando **Programação
Orientada a Objetos (POO)**.

## 🎯 Objetivo

Demonstrar de forma prática:
- Uso da biblioteca psutil
- Conceitos básicos de POO em Python
- Monitoramento de CPU, memória e disco

Indicado para cursos técnicos, disciplinas de Redes, Sistemas Operacionais
e Internet das Coisas (IoT).

## 🛠️ Tecnologias utilizadas

- Python 3
- psutil

## 📦 Instalação da biblioteca

```bash
pip install psutil
```

## ▶️ Execução do programa

No terminal, dentro da pasta do projeto:

```bash
python monitor.py
```

## 📌 Conceitos de POO aplicados

- Classe `MonitorSistema`: representa o monitor de recursos
- Método `__init__`: inicializa o objeto
- Métodos específicos: cada recurso do sistema tem seu próprio método
- Método `iniciar`: controla o fluxo principal do programa

## 🚀 Possíveis extensões

- Salvar os dados em arquivo CSV
- Enviar informações via MQTT
- Adaptar para Raspberry Pi
- Criar alertas quando o uso ultrapassar limites

## 📚 Licença

Projeto livre para fins educacionais.
