from database.database import SessionLocal
from models.models import Curso

def test_listar_cursos():
    print()

    session = SessionLocal()
    cursos = session.query(Curso).order_by(Curso.id).all()

    for curso in cursos:
        print(curso.id, curso.nome_cursos, curso.valor)

    assert cursos is not None
    session.close()
