# Enlace — Bluetooth e Broadcast
Material didático — Redes de Computadores / ADS
DIATINF — IFRN

Exemplos ligados à Camada de Enlace: descoberta de dispositivos próximos (Bluetooth) e entrega broadcast em uma LAN (ver também a teoria em [`06_componentes_fisicos/unicast_broadcast_multicast.md`](../../../06_componentes_fisicos/unicast_broadcast_multicast.md)).

---

## 📂 `Bluetooth/`

### `listarDevsBluetooth.py`
Varre dispositivos Bluetooth próximos e imprime endereço e nome de cada um.

- **Dependência**: [`PyBluez`](https://pypi.org/project/PyBluez/) (`pip install pybluez`). É uma biblioteca antiga, com suporte mais estável em **Linux com BlueZ**; em Windows/Mac a instalação pode ser instável — trate como opcional/demonstração em laboratório Linux.
- **Execução**:
  ```bash
  python3 listarDevsBluetooth.py
  ```

---

## 📂 `Broadcast/Basico/`

Par cliente/servidor mínimo demonstrando broadcast UDP puro — a versão mais simples do conceito (comparar com [`06_componentes_fisicos/broadcast_demo.py`](../../../06_componentes_fisicos/broadcast_demo.py), que já separa cliente/servidor em funções dentro de um único arquivo).

### `Esperador.py`
Fica escutando por broadcasts na porta `5005` e imprime tudo que chega.

### `Enviador.py`
Descobre todos os IPs locais da máquina e envia a mesma mensagem em broadcast (`255.255.255.255:5005`) a partir de cada um deles — útil para observar, em uma máquina com várias interfaces de rede, por qual delas a mensagem realmente sai.

### Como executar

Terminal 1:
```bash
python3 Esperador.py
```

Terminal 2:
```bash
python3 Enviador.py "mensagem opcional"
```

---

DIATINF — IFRN
Material educacional de Redes de Computadores e ADS.
