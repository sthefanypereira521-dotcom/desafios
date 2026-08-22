from database.database import SessionLocal
from models.models import Aluno, Matricula

def test_listar_alunos_matriculas():
    print()

    session = SessionLocal()

    resultado = (
        session.query(Aluno.nome)
        .outerjoin(Matricula, Matricula.aluno_id == Aluno.id)
        .filter(Matricula.id == None)
        .all()
)

    for (nome,) in resultado:
        print(f'{nome} nao tem matricula')


    assert len(resultado) > 0
    session.close()

