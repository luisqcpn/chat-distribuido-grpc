Objetivo do Projeto

Construir um sistema de chat distribuído simples e funcional usando Python, gRPC e infraestrutura em nuvem (AWS), com provisionamento automatizado via CloudFormation.

- Arquitetura

Uma instância EC2 pública (Ubuntu) com IP fixo

VPC, Subnet, InternetGateway e Security Group configurados via YAML

Porta 50051 aberta para gRPC

Clonagem automática do repositório e execução do servidor

- Tecnologias e Ferramentas

Python + gRPC

AWS EC2, S3 (sendo opcional), CloudFormation

GitHub para versionamento e deploy

- Etapas Realizadas

Desenvolvimento local do servidor e cliente com gRPC

Geração do .proto com grpcio-tools

- Testes locais

Criação da infraestrutura via CloudFormation

Deploy automatizado via UserData

Testes de conexão remota e comunicação simultânea

- Conclusão

O projeto demonstra como é possível integrar comunicação distribuída e computação em nuvem com ferramentas modernas. Utilizando boas práticas de infraestrutura como código (IaC), provisionamento automatizado e comunicação eficiente via gRPC, foi possível desenvolver uma solução robusta, simples e funcional.

Link do Repositório

https://github.com/luisqcpn/chat-distribuido-grpc
