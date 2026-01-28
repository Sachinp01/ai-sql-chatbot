from fastapi import FastAPI, HTTPException
import json

from app.ai.sql_generator import generate_sql
from app.ai.sql_validator import validate_sql
from app.ai.query_executor import execute_sql
from app.ai.response_formatter import format_response

app = FastAPI(title="AI SQL Chatbot")

SCHEMA_PATH = "app/metadata/schema_metadata.json"

@app.post("/chat")
def chat(question: str):
    with open(SCHEMA_PATH) as f:
        schema_metadata = json.load(f)

    try:
        sql = generate_sql(question, schema_metadata)
        validate_sql(sql)
        result = execute_sql(sql)
        answer = format_response(result)

        return {
            "question": question,
            "sql": sql,
            "answer": answer
        }

    except ValueError as ve:
        if str(ve) == "AMBIGUOUS_QUESTION":
            raise HTTPException(
                status_code=400,
                detail="Your question is ambiguous. Please clarify."
            )
        if str(ve) == "DATA_NOT_AVAILABLE":
            raise HTTPException(
                status_code=404,
                detail="The requested data is not available."
            )
        raise HTTPException(status_code=400, detail=str(ve))

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
