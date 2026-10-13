from typing import Optional
from sqlalchemy import String, Numeric, ForeignKey, PrimaryKeyConstraint, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column
from src.database import Base
from src.constants import TableNames

class Section(Base):
    __tablename__ = TableNames.SECTION

    course_id: Mapped[str] = mapped_column(String(8), ForeignKey(f"{TableNames.COURSE}.course_id", ondelete="CASCADE"), primary_key=True)
    sec_id: Mapped[str] = mapped_column(String(8), primary_key=True)
    semester: Mapped[str] = mapped_column(String(6), primary_key=True)
    year: Mapped[int] = mapped_column(Numeric(4, 0, asdecimal=False), primary_key=True)
    building: Mapped[Optional[str]] = mapped_column(String(15))
    room_number: Mapped[Optional[str]] = mapped_column(String(7))
    time_slot_id: Mapped[Optional[str]] = mapped_column(String(4))

    __table_args__ = (
        PrimaryKeyConstraint("course_id", "sec_id", "semester", "year"),
        CheckConstraint("semester IN ('Fall', 'Winter', 'Spring', 'Summer')", name="check_section_semester"),
        CheckConstraint("year > 1701 AND year < 2100", name="check_section_year"),
        ForeignKey("classroom.building", "classroom.room_number", ondelete="SET NULL")
    )


