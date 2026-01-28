from sqlalchemy import text
from app.db.database import engine

def execute_sql(sql: str):
    with engine.connect() as conn:
        result = conn.execute(text(sql))
        rows = result.fetchall()
        columns = result.keys()

    return {
        "columns": columns,
        "rows": rows
    }
