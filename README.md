# SADI — Sistema de Estacionamento Inteligente

Projeto acadêmico para demonstrar um sistema de estacionamento inteligente. O repositório reúne um painel administrativo em Streamlit, comunicação HTTP com Node-RED e um monitor de arquivos YAML/imagens para coordenar a aquisição e o processamento.

> **Estado atual:** a etapa de leitura de placas em `watcher.py` ainda usa resultados fixos de demonstração. Ela não executa um modelo de visão computacional.

## Estrutura do repositório

```text
.
├── images-src/              # Imagens de entrada/de exemplo
├── images-dst/              # Imagens recebidas para processamento (conteúdo ignorado pelo Git)
├── interface/
│   ├── assets/              # Imagens mostradas no painel
│   ├── carros_cadastro.csv  # Cadastro local de placas
│   ├── config.yaml          # Status exibidos na interface
│   ├── database.py          # Leitura e gravação do CSV
│   └── main_interface.py    # Aplicação Streamlit
├── node-red-flow/flows.json # Fluxo para importar no Node-RED
├── python_requests/         # Cliente HTTP para enviar comandos ao Node-RED
├── yaml-src/                # Exemplos de estado da aquisição
├── yaml-dst/status.yaml     # Estado observado pelo watcher
├── requirements.txt         # Dependências Python
└── watcher.py               # Monitor de imagens e estado YAML
```

## Requisitos

- Python 3.9 ou superior
- Node-RED, se quiser testar o envio de comandos

## Instalação

Na raiz do repositório, crie um ambiente virtual e instale as dependências:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

No Windows, ative o ambiente com `.venv\Scripts\activate`.

## Executar

Inicie o painel web:

```bash
streamlit run interface/main_interface.py
```

Inicie o monitor em outro terminal, também a partir da raiz do repositório:

```bash
python watcher.py
```

O `watcher.py` observa `yaml-dst/status.yaml` e verifica a pasta `images-dst/`. A pasta já está incluída no repositório como diretório vazio; os arquivos de imagem adicionados nela não são versionados.

O cliente HTTP envia requisições para `http://127.0.0.1:1880/comando` por padrão. Ajuste os argumentos de `send_command` em `python_requests/request.py` se o Node-RED estiver em outro endereço ou caminho.

## Configuração e dados

- `interface/config.yaml` define `status_analysis` (`Em Espera`, `Aprovado` ou `Reprovado`) e `status_motor` (`Fechado`, `Abrindo`, `Aberto` ou `Fechando`).
- `yaml-dst/status.yaml` usa a chave `inference` para indicar se o watcher deve processar (`true`) ou aguardar (`false`).
- `interface/carros_cadastro.csv` armazena os cadastros localmente. O painel contém uma área de administrador demonstrativa; altere as credenciais fixas antes de qualquer uso real.
- Importe `node-red-flow/flows.json` no Node-RED para carregar o fluxo de exemplo. Confirme que ele expõe a rota HTTP esperada pelo cliente.

## Observações

Execute os comandos a partir da raiz para que os caminhos relativos usados pelo watcher e pela interface encontrem os arquivos de configuração e dados. O fluxo completo depende de componentes externos (por exemplo, aquisição de imagens e Node-RED) que não são iniciados por este repositório.
