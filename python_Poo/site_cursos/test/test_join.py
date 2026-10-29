from database.database import SessionLocal
from models.models import Aluno, Curso, Matricula


def test_alunos_cursos_matriculas_ativa():
    print()

    session = SessionLocal()

    resultado = (
        session.query(Aluno.nome, Curso.nome_cursos, Matricula.ativo)
        .join(Matricula, Matricula.aluno_id == Aluno.id)
        .join(Curso, Curso.id == Matricula.curso_id)
        .all()
)

    for nome_aluno, nome_curso, ativo in resultado:
        print(f"{nome_aluno} está matriculada em {nome_curso} (ativo: {ativo})")

    assert len(resultado) > 0
    session.close()
    