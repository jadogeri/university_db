from sqlalchemy import String, Numeric, PrimaryKeyConstraint, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column
from database import Base
from constants import TableNames

class TimeSlot(Base):
    __tablename__ = TableNames.TIME

    time_slot_id: Mapped[str] = mapped_column(String(4), primary_key=True)
    day: Mapped[str] = mapped_column(String(1), primary_key=True)
    start_hr: Mapped[int] = mapped_column(Numeric(2, 0, asdecimal=False), primary_key=True)
    start_min: Mapped[int] = mapped_column(Numeric(2, 0, asdecimal=False), primary_key=True)
    end_hr: Mapped[int] = mapped_column(Numeric(2, 0, asdecimal=False))
    end_min: Mapped[int] = mapped_column(Numeric(2, 0, asdecimal=False))

    __table_args__ = (
        PrimaryKeyConstraint("time_slot_id", "day", "start_hr", "start_min"),
        CheckConstraint("start_hr >= 0 AND start_hr < 24", name="check_start_hr"),
        CheckConstraint("start_min >= 0 AND start_min < 60", name="check_start_min"),
        CheckConstraint("end_hr >= 0 AND end_hr < 24", name="check_end_hr"),
        CheckConstraint("end_min >= 0 AND end_min < 60", name="check_end_min"),
    )
