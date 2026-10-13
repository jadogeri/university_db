from typing import Optional
from sqlalchemy import String, Numeric, ForeignKey, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column
from src.database import Base
from src.constants import TableNames

class Instructor(Base):
    __tablename__ = TableNames.INSTRUCTOR

    id: Mapped[str] = mapped_column("ID", String(5), primary_key=True)
    name: Mapped[str] = mapped_column(String(20), nullable=False)
    dept_name: Mapped[Optional[str]] = mapped_column(
        String(20), ForeignKey(f"{TableNames.DEPARTMENT}.dept_name", ondelete="SET NULL")
    )
    salary: Mapped[Optional[float]] = mapped_column(Numeric(8, 2))

    __table_args__ = (
        CheckConstraint("salary > 29000", name="check_instructor_salary"),
    )
