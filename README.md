# DevOps-lab
Repo para estudo devops

- projeto foi dividido em múltiplos containers com Docker Compose:

    api: container FastAPI/Python

    db: container Postgres

    nginx: container NGINX como reverse proxy


- Criação da API (FastAPI)

- Criado main.py com estrutura básica de endpoints

- Separação por módulos (db.py, models.py)

- Banco de dados com Postgres

- Variáveis de ambiente no .env

- db.py conectando via sqlalchemy

- models.py criado com estrutura de tabelas Target e Check

- NGINX

    Criado container separado

    Configurado como reverse proxy para a API

    Corrigido erro de sintaxe no default.conf

- Dockerfile + Compose

    Estrutura multi-serviço com depends_on, healthcheck, restart: unless-stopped

    Infra na EC2

    Projeto rodando na AWS Free Tier

EC2 como ambiente prático para exercitar CI, rede, volume e containers
