# AI-Powered SQL Chatbot Backend

An AI-powered chatbot that allows users to ask natural language questions and receive accurate, context-aware answers derived strictly from structured database data.

This project demonstrates a complete **Text-to-SQL AI pipeline** with strong emphasis on **data correctness, security, and explainability**.

---

## 🚀 Features

- Natural language → SQL query generation
- Grounded responses strictly from database data (no hallucination)
- Secure SQL validation (prevents injections & unsafe queries)
- Semantic mapping for business terms (e.g., “approved” loans)
- FastAPI backend with interactive Swagger UI
- PostgreSQL relational database
- Extensible, production-style architecture

---

## 🧠 Example

**User Question**
How many loans are approved?


**Generated SQL**
```sql
SELECT COUNT(*) 
FROM loans 
WHERE loan_status IN ('Accepted', 'Complete')
Response

count: 16
🏗️ Architecture Overview
User Question
   ↓
Semantic Mapping (business terms)
   ↓
LLM (Groq – LLaMA 3.1)
   ↓
SQL Normalization & Validation
   ↓
PostgreSQL Execution
   ↓
Human-readable Response
🧰 Tech Stack
Backend: FastAPI

Database: PostgreSQL

LLM: Groq (LLaMA 3.1 – API-based)

ORM: SQLAlchemy

Data Processing: Pandas

Validation: Pydantic

API Docs: Swagger (OpenAPI)

📂 Project Structure
ai_chatbot_backend/
│
├── app/
│   ├── ai/
│   │   ├── sql_generator.py
│   │   ├── sql_validator.py
│   │   ├── semantic_mapper.py
│   │   ├── query_executor.py
│   │   └── response_formatter.py
│   │
│   ├── db/
│   │   ├── database.py
│   │   ├── models.py
│   │   └── schemas.py
│   │
│   ├── metadata/
│   │   └── schema_metadata.json
│   │
│   └── main.py
│
├── data/
│   └── Sample Data.xlsx
│
├── requirements.txt
├── .env.example
└── README.md
🗄️ Data Model
loans table
Column	Description
id	Primary key
user_id	User identifier
loan_status	Status of loan (Accepted, Complete, Rejected, etc.)
net_approved_amount	Approved amount
loan_disbursement_date	Disbursement date
created_at	Record creation time
Semantic Mapping
Business terms are mapped to database values:

Business Term	DB Values
approved	Accepted, Complete
rejected	Rejected
active	Active, InProcess
⚙️ Setup Instructions
1️⃣ Clone Repository
git clone <private-repo-url>
cd ai_chatbot_backend
2️⃣ Create Virtual Environment
python -m venv venv
source venv/Scripts/activate
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Configure Environment Variables
Create .env file:

GROQ_API_KEY=your_groq_api_key
GROQ_MODEL=llama-3.1-8b-instant
▶️ Run the Application
uvicorn app.main:app --reload
Open Swagger UI:

http://127.0.0.1:8000/docs
🔒 Accuracy & Safety
SQL execution is read-only

No multi-statement queries allowed

SQL keywords validated

LLM output normalized before execution

Business semantics handled deterministically

📌 Assignment Coverage Checklist
✔ Chatbot creation (NL → DB answers)
✔ Data migration to relational DB
✔ AI workflow design (Text-to-SQL)
✔ Schema & metadata documentation
✔ Accuracy & reliability guarantees
✔ Aggregations, filters, conditions
✔ Extensible for joins & follow-up queries

📈 Future Enhancements (Optional)
Conversation memory for follow-up questions

SQL explanation in responses

ER diagram visualization

Dockerized deployment

Unit & integration tests

👤 Author
Sachin Patil

This project was built as part of an AI Backend Engineering assignment to demonstrate real-world application of LLMs with structured data systems.

