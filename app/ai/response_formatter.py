def format_response(query_result: dict) -> str:
    rows = query_result["rows"]
    columns = query_result["columns"]

    if not rows:
        return "No data found for your query."

    response = f"Found {len(rows)} records.\n\n"
    for row in rows[:5]:
        response += ", ".join(
            f"{col}: {val}" for col, val in zip(columns, row)
        ) + "\n"

    return response
