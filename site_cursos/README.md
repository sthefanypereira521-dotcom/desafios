# Site Cursos

Projeto de estudo com SQLAlchemy, PostgreSQL e Alembic.

## Tecnologias
- Python
- SQLAlchemy (ORM)
- PostgreSQL
- Alembic (migrações)
- python-dotenv

## O que o projeto tem
- Models para Aluno, Curso e Matrícula
- Relacionamento entre tabelas via foreign keys
- Migrações versionadas com Alembic
- Scripts de teste com queries: join, outer join, ordenação

## Como rodar o projeto

1. Clone o repositório
2. Renomeie `.env.example` para `.env`
3. Preencha com suas credenciais do PostgreSQL
4. Instale as dependências:
   poetry install
5. Ative o ambiente virtual:
   poetry shell
6. Rode as migrações:
   alembic upgrade head