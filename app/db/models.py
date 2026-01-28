from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(String(64), unique=True, nullable=False)
    banking_id = Column(String(32), nullable=True)
    created_at = Column(DateTime, nullable=False)

    loans = relationship("Loan", back_populates="user")


class Loan(Base):
    __tablename__ = "loans"

    id = Column(Integer, primary_key=True, autoincrement=True)
    loan_id = Column(Integer, nullable=False)
    user_id = Column(String(64), ForeignKey("users.user_id"), nullable=False)

    loan_status = Column(String(32), nullable=False)
    net_approved_amount = Column(Float, nullable=True)
    loan_disbursement_date = Column(DateTime, nullable=True)
    remark = Column(String(255), nullable=True)
    user_reason_decline = Column(String(255), nullable=True)
    created_at = Column(DateTime, nullable=False)

    user = relationship("User", back_populates="loans")
