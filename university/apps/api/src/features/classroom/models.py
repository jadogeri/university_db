from typing import Optional
from constants import TableNames
from sqlalchemy import String, Numeric, PrimaryKeyConstraint
from sqlalchemy.orm import Mapped, mapped_column
from database import Base

class Classroom(Base):
    __tablename__ = TableNames.CLASSROOM

    building: Mapped[str] = mapped_column(String(15), primary_key=True)
    room_number: Mapped[str] = mapped_column(String(7), primary_key=True)
    capacity: Mapped[Optional[int]] = mapped_column(Numeric(4, 0, asdecimal=False))

    __table_args__ = (PrimaryKeyConstraint("building", "room_number"),)
