from typing import Optional
from sqlalchemy import String, Numeric, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column
from database import Base
from constants import TableNames

class Department(Base):
    __tablename__ = TableNames.DEPARTMENT

    dept_name: Mapped[str] = mapped_column(String(20), primary_key=True)
    building: Mapped[Optional[str]] = mapped_column(String(15))
    budget: Mapped[Optional[float]] = mapped_column(Numeric(12, 2))

    __table_args__ = (
        CheckConstraint("budget > 0", name="check_dept_budget"),
    )
