# Site Cursos

Projeto de estudo com SQLAlchemy, PostgreSQL, Alembic, docker e docker compose.

## Tecnologias
- Python
- SQLAlchemy (ORM)
- PostgreSQL
- Alembic (migrações)
- python-dotenv
- Docker & Docker Compose 
- Pytest testes automatizados

## O que o projeto tem
- Models para Aluno, Curso e Matrícula
- Relacionamento entre tabelas via foreign keys
- Migrações versionadas com Alembic
- Scripts de teste com queries: join, outer join, ordenação

## Como rodar o projeto

1. Pré-requisitos
   Docker e Docker Compose instalados

2. Clone o repositório

2. Renomeie `.env.example` para `.env`
   Preencha com suas credenciais do PostgreSQL

3.  Suba os containers
   - docker compose up   

4. Se quiser rodar só as migrations 
   sem recriar tudo
   - docker compose up migrate
   
