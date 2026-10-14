
from typing import Optional
from sqlalchemy import String, Numeric, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.orm import Mapped, mapped_column


from database import Base
from constants import TableNames

class Takes(Base):
    __tablename__ = TableNames.TAKES

    id: Mapped[str] = mapped_column("ID", String(5), ForeignKey(f"{TableNames.STUDENT}.ID", ondelete="CASCADE"), primary_key=True)
    course_id: Mapped[str] = mapped_column(String(8), primary_key=True)
    sec_id: Mapped[str] = mapped_column(String(8), primary_key=True)
    semester: Mapped[str] = mapped_column(String(6), primary_key=True)
    year: Mapped[int] = mapped_column(Numeric(4, 0, asdecimal=False), primary_key=True)
    grade: Mapped[Optional[str]] = mapped_column(String(2))

    __table_args__ = (
        PrimaryKeyConstraint("ID", "course_id", "sec_id", "semester", "year"),
        ForeignKey("section.course_id", "section.sec_id", "section.semester", "section.year", ondelete="CASCADE"),
    )
