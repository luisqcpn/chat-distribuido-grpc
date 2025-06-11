#Chat Distribuído com gRPC na AWS

Projeto desenvolvido para a disciplina de Computação em Nuvem, com o objetivo de criar um sistema de chat distribuído usando gRPC, provisionamento via AWS CloudFormation e hospedação em uma instância EC2.

🔧 Tecnologias Utilizadas

Python 3.10+

gRPC e Protocol Buffers

AWS EC2

AWS CloudFormation

GitHub

Ubuntu 22.04

🚀 Funcionalidades

Chat distribuído com múltiplos clientes simultâneos

Transmissão em tempo real com stream bidirecional gRPC

Provisionamento automatizado da infraestrutura via YAML (CloudFormation)

Deploy automatizado com clonagem do repositório direto da EC2

📂 Estrutura do Projeto
chat-distribuido-grpc/
├── client/
│   └── chat_client.py
├── server/
│   └── chat_server.py
├── proto/
│   ├── chat.proto
│   ├── chat_pb2.py
│   └── chat_pb2_grpc.py
├── infra/
│   └── cloudformation.yaml
├── README.md
├── relatorio.md
└── .gitignore

📥 Execução Local

Servidor
cd server
pip install -r requirements.txt
python chat_server.py

Cliente
cd client
pip install -r requirements.txt
python chat_client.py

Importante: Altere o IP no chat_client.py para o IP público da EC2.

🔍 Testes Realizados

* Testes com dois terminais clientes simultâneos

* Verificação dos logs via tail -f server.log

* Deploy com repositório Git funcionou corretamente

* Acesso SSH com chave chat_key no Ubuntu
