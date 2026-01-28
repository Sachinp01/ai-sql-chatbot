STATUS_SEMANTIC_MAP = {
    "approved": ["Accepted", "Complete"],
    "rejected": ["Rejected"],
    "active": ["Active", "InProcess"],
    "completed": ["Complete"],
}


def expand_status_terms(question: str):
    question_lower = question.lower()

    for term, mapped_values in STATUS_SEMANTIC_MAP.items():
        if term in question_lower:
            return mapped_values

    return None
