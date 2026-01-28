import os
import json
from dotenv import load_dotenv
from groq import Groq

from app.ai.prompt import SYSTEM_PROMPT
from app.ai.semantic_mapper import expand_status_terms

# 🔹 Load environment variables FIRST
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = os.getenv("GROQ_MODEL", "llama-3.1-8b-instant")

if not GROQ_API_KEY:
    raise RuntimeError("GROQ_API_KEY not found in environment variables")

client = Groq(api_key=GROQ_API_KEY)


def generate_sql(question: str, schema_metadata: dict) -> str:
    """
    1️⃣ Handle business semantics first (approved, rejected, active, etc.)
    2️⃣ If semantic match → return deterministic SQL (NO LLM)
    3️⃣ Else → fall back to LLM-based SQL generation
    """

    # 🔹 STEP 1: Semantic handling (OVERRIDES LLM)
    mapped_statuses = expand_status_terms(question)

    if mapped_statuses:
        values = ", ".join(f"'{v}'" for v in mapped_statuses)
        return (
            "SELECT COUNT(*) "
            "FROM loans "
            f"WHERE loan_status IN ({values})"
        )

    # 🔹 STEP 2: LLM fallback
    prompt = SYSTEM_PROMPT.format(
        schema=json.dumps(schema_metadata["tables"], indent=2),
        relationships=json.dumps(schema_metadata["relationships"], indent=2),
    )

    response = client.chat.completions.create(
        model=GROQ_MODEL,
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": question},
        ],
        temperature=0,
        max_tokens=300,
    )

    sql = response.choices[0].message.content.strip()

    # 🔒 Normalize SQL (remove trailing semicolon)
    if sql.endswith(";"):
        sql = sql[:-1].strip()

    return sql
