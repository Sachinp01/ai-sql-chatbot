from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class UserSchema(BaseModel):
    user_id: str
    banking_id: Optional[str]
    created_at: datetime


class LoanSchema(BaseModel):
    loan_id: int
    user_id: str
    loan_status: str
    net_approved_amount: Optional[float]
    loan_disbursement_date: Optional[datetime]
    remark: Optional[str]
    user_reason_decline: Optional[str]
    created_at: datetime
