from database.database import SessionLocal
from models.models import Aluno, Curso, Matricula

def test_listar_alunos_cursos_matriculas_valor():
    print()

    session = SessionLocal()

    resultado = (
        session.query(Aluno.nome, Curso.nome_cursos, Curso.valor)
        .join(Matricula, Matricula.aluno_id == Aluno.id)
        .join(Curso, Curso.id == Matricula.curso_id)
        .all()
)

    for nome_aluno, nome_curso, valor in resultado:
        print(f"{nome_aluno} esta matriculada no curso de {nome_curso} o valor custa R$ {valor}")

    assert len(resultado) > 0
    session.close()
