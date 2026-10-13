from typing import Optional
from sqlalchemy import String, Numeric, ForeignKey, PrimaryKeyConstraint, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column
from src.database import Base
from src.constants import TableNames

class Course(Base):
    __tablename__ = TableNames.COURSE

    course_id: Mapped[str] = mapped_column(String(8), primary_key=True)
    title: Mapped[Optional[str]] = mapped_column(String(50))
    dept_name: Mapped[Optional[str]] = mapped_column(
        String(20), ForeignKey(f"{TableNames.DEPARTMENT}.dept_name", ondelete="SET NULL")
    )
    credits: Mapped[Optional[int]] = mapped_column(Numeric(2, 0, asdecimal=False))

    __table_args__ = (
        CheckConstraint("credits > 0", name="check_course_credits"),
    )

