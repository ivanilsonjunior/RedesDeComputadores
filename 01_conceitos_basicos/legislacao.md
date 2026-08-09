# Legislação Relacionada a Redes no Brasil
Material didático — Redes de Computadores / ADS
DIATINF — IFRN

Quem projeta, administra ou desenvolve para redes de computadores no Brasil precisa conhecer, mesmo que em nível introdutório, as leis e normas que regulam esse ambiente. Elas afetam decisões técnicas reais: que logs guardar, por quanto tempo, como tratar dados de usuários, e quais equipamentos podem ser usados legalmente.

---

## ✔️ Marco Civil da Internet (Lei 12.965/2014)

Estabelece princípios, garantias, direitos e deveres para o uso da Internet no Brasil. Os pontos mais relevantes para quem trabalha com redes:

- **Neutralidade de rede** (art. 9º): o responsável pela transmissão, comutação ou roteamento tem o dever de tratar de forma isonômica qualquer pacote de dados, sem distinção por conteúdo, origem, destino, serviço, terminal ou aplicação. Ou seja: um provedor não pode, por exemplo, degradar deliberadamente o tráfego de um serviço concorrente.
- **Privacidade**: usuários têm direito à inviolabilidade e ao sigilo de suas comunicações, salvo por ordem judicial.
- **Guarda de registros (logs)**: provedores de **conexão** são obrigados a manter os registros de conexão (não o conteúdo, mas metadados como IP e horário) por 1 ano; provedores de **aplicação** devem manter registros de acesso por 6 meses.
- **Responsabilidade dos provedores**: em regra, um provedor de aplicação só pode ser responsabilizado civilmente por conteúdo de terceiros se descumprir uma ordem judicial específica para removê-lo.

## ✔️ LGPD — Lei Geral de Proteção de Dados (Lei 13.709/2018)

Regula a coleta, o armazenamento, o tratamento e o compartilhamento de dados pessoais — inclusive dados coletados via rede, como endereços IP, que podem ser considerados dado pessoal quando permitem identificar uma pessoa.

Conceitos centrais para quem desenvolve sistemas em rede:
- **Dado pessoal** x **dado sensível** (este último exige cuidado redobrado: saúde, biometria, orientação, etc.).
- **Agentes de tratamento**: controlador (decide o que fazer com o dado) e operador (processa por conta do controlador).
- **Base legal**: todo tratamento de dado precisa se apoiar em uma hipótese prevista em lei (ex.: consentimento, execução de contrato, cumprimento de obrigação legal).
- **ANPD** (Autoridade Nacional de Proteção de Dados): órgão responsável por fiscalizar e regulamentar a aplicação da lei.

Na prática, a LGPD é o motivo pelo qual sistemas modernos evitam logar dados desnecessários, criptografam informações sensíveis em trânsito (ver [`material_de_apoio/SideQuests/Segurança/Criptografia/`](../material_de_apoio/SideQuests/Segurança/Criptografia/)) e precisam justificar por que coletam cada dado.

## ✔️ Resoluções da Anatel

A Agência Nacional de Telecomunicações regula, entre outros pontos:
- **Homologação de equipamentos**: roteadores, access points e outros dispositivos de radiofrequência só podem ser legalmente comercializados e usados no Brasil se homologados pela Anatel.
- **Uso do espectro de radiofrequência**: as faixas usadas por Wi-Fi (2,4 GHz e 5 GHz) são de uso livre, mas regulamentado — respeitando limites de potência de transmissão para evitar interferência.

## ✔️ Normas ABNT / ISO

- **ISO/IEC 27001**: define um Sistema de Gestão de Segurança da Informação (SGSI) — o "como organizar" a segurança em uma instituição.
- **ISO/IEC 27002**: traz um catálogo de boas práticas e controles de segurança (ex.: controle de acesso, segurança em redes) que complementa a 27001.
- Ambas são referências comuns em auditorias de segurança e em editais públicos que exigem conformidade.

---

## Por que isso importa na prática

| Situação técnica | Norma envolvida |
|---|---|
| Decidir por quanto tempo guardar logs de acesso de um servidor | Marco Civil da Internet |
| Um provedor limitar a velocidade de um serviço específico (ex.: streaming) | Neutralidade de rede (Marco Civil) |
| Um sistema armazenar o IP dos usuários em um banco de dados | LGPD |
| Vender ou instalar um roteador Wi-Fi no Brasil | Homologação Anatel |
| Documentar controles de segurança de uma rede corporativa | ISO/IEC 27001/27002 |

---

DIATINF — IFRN
Material educacional de Redes de Computadores e ADS.
