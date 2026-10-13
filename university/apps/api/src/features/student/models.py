from typing import Optional
from sqlalchemy import String, Numeric, ForeignKey, PrimaryKeyConstraint, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column
from src.database import Base
from src.constants import TableNames

class Student(Base):
    __tablename__ = TableNames.STUDENT

    id: Mapped[str] = mapped_column("ID", String(5), primary_key=True)
    name: Mapped[str] = mapped_column(String(20), nullable=False)
    dept_name: Mapped[Optional[str]] = mapped_column(
        String(20), ForeignKey(f"{TableNames.DEPARTMENT}.dept_name", ondelete="SET NULL")
    )
    tot_cred: Mapped[Optional[int]] = mapped_column(Numeric(3, 0, asdecimal=False))

    __table_args__ = (
        CheckConstraint("tot_cred >= 0", name="check_student_tot_cred"),
    )

