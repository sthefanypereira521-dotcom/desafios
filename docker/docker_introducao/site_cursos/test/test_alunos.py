from database.database import SessionLocal
from models.models import Aluno


def test_listar_alunos():
    print()

    session = SessionLocal()
    alunos = session.query(Aluno).order_by(Aluno.id).all()

    for aluno in alunos:
        print(aluno.id, aluno.nome, aluno.email)

    assert alunos is not None   

    session.close()
