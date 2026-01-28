import pandas as pd
from pandas import to_datetime
from sqlalchemy.orm import Session

from app.db.database import engine, SessionLocal, Base
from app.db.models import User, Loan
from app.db.schemas import UserSchema, LoanSchema


# 🔁 Helper function (ADDED)
def clean_str(value):
    if pd.isna(value):
        return None
    return str(value)


DATA_PATH = "data/Sample Data.xlsx"


def migrate():
    print("🚀 Migration script started")

    Base.metadata.create_all(bind=engine)
    db: Session = SessionLocal()

    df = pd.read_excel(DATA_PATH)
    print("📄 Excel loaded successfully")

    for _, row in df.iterrows():
        # -------- USER --------
        user_schema = UserSchema(
            user_id=row["userId"],
            banking_id=str(row["bankingId"]) if pd.notna(row["bankingId"]) else None,
            created_at=to_datetime(row["createdAt"], utc=True).to_pydatetime()
        )

        user = db.query(User).filter_by(user_id=user_schema.user_id).first()
        if not user:
            user = User(
                user_id=user_schema.user_id,
                banking_id=user_schema.banking_id,
                created_at=user_schema.created_at
            )
            db.add(user)
            db.commit()

        # -------- LOAN --------
        loan_schema = LoanSchema(
            loan_id=row["id"],
            user_id=row["userId"],
            loan_status=row["loanStatus"],
            net_approved_amount=row["netApprovedAmount"],
            loan_disbursement_date=(
                to_datetime(row["loan_disbursement_date"], utc=True).to_pydatetime()
                if pd.notna(row["loan_disbursement_date"])
                else None
            ),
            remark=clean_str(row["remark"]),
            user_reason_decline=clean_str(row["userReasonDecline"]),
            created_at=to_datetime(row["createdAt"], utc=True).to_pydatetime()
        )

        loan = Loan(
            loan_id=loan_schema.loan_id,
            user_id=loan_schema.user_id,
            loan_status=loan_schema.loan_status,
            net_approved_amount=loan_schema.net_approved_amount,
            loan_disbursement_date=loan_schema.loan_disbursement_date,
            remark=loan_schema.remark,
            user_reason_decline=loan_schema.user_reason_decline,
            created_at=loan_schema.created_at
        )

        db.add(loan)

    db.commit()
    db.close()
    print("✅ Data migration completed successfully")


if __name__ == "__main__":
    migrate()
