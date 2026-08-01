from sqlalchemy import Column, Integer, String, Boolean, DateTime, Numeric,ForeignKey
from database.database import Base


class Aluno(Base):
    __tablename__ = "alunos"
    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    ano_nascimento = Column(Integer)


class Curso(Base):
    __tablename__ = "cursos"
    id = Column(Integer, primary_key=True)
    nome_cursos = Column(String(100),nullable=False)
    carga_hora = Column(Integer, nullable=False)
    valor = Column(Numeric(10, 2))
    ativo = Column(Boolean)
    data_criacao = Column(DateTime)


class Matricula(Base):
    __tablename__ = "matriculas"
    id = Column(Integer, primary_key=True)
    aluno_id = Column(Integer, ForeignKey("alunos.id"))
    curso_id = Column(Integer, ForeignKey("cursos.id"))
    ativo = Column(Boolean)
    data_matricula = Column(DateTime)
