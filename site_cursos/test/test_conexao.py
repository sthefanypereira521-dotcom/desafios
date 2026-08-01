from database.database import engine
from sqlalchemy import text


def test_conexao():
    with engine.connect() as conn:
        resultado = conn.execute(text("SELECT 1"))
        assert resultado.scalar() == 1
