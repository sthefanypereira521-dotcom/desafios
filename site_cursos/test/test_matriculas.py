from database.database import SessionLocal
from models.models import Matricula

def test_listar_matriculas():
    print()

    session = SessionLocal()
    matriculas = session.query(Matricula).all()

    for m in matriculas:
        print(m.id, m.aluno_id, m.curso_id, m.ativo)

    assert matriculas is not None
    session.close()
