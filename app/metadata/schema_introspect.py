import json
from sqlalchemy import inspect
from app.db.database import engine

OUTPUT_FILE = "app/metadata/schema_metadata.json"


def generate_metadata():
    inspector = inspect(engine)

    metadata = {
        "database": "chatbot_db",
        "tables": {},
        "relationships": []
    }

    for table_name in inspector.get_table_names():
        columns = inspector.get_columns(table_name)
        pk = inspector.get_pk_constraint(table_name)
        fks = inspector.get_foreign_keys(table_name)

        metadata["tables"][table_name] = {
            "description": f"Table storing {table_name} data",
            "columns": {},
            "primary_key": pk.get("constrained_columns", [])
        }

        for col in columns:
            metadata["tables"][table_name]["columns"][col["name"]] = {
                "type": str(col["type"]),
                "nullable": col["nullable"]
            }

        for fk in fks:
            relationship = {
                "from_table": table_name,
                "from_column": fk["constrained_columns"][0],
                "to_table": fk["referred_table"],
                "to_column": fk["referred_columns"][0]
            }
            metadata["relationships"].append(relationship)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2)

    print("✅ Schema metadata generated successfully")


if __name__ == "__main__":
    generate_metadata()
