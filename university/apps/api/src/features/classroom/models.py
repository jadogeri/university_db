from sqlalchemy import Column, String, Integer, CheckConstraint
from database import Base
from constants import TableNames

class Classroom(Base):
    __tablename__ = TableNames.CLASSROOM
    
    building = Column(String(15), primary_key=True)
    room_number = Column(String(7), primary_key=True)
    capacity = Column(Integer)  # numeric(4,0) maps to Integer


class TimeSlot(Base):
    __tablename__ = TableNames.TIME
    
    time_slot_id = Column(String(4), primary_key=True)
    day = Column(String(1), primary_key=True)
    start_hr = Column(Integer, primary_key=True)
    start_min = Column(Integer, primary_key=True)
    end_hr = Column(Integer)
    end_min = Column(Integer)
    
    __table_args__ = (
        CheckConstraint("start_hr >= 0 AND start_hr < 24", name="check_start_hr"),
        CheckConstraint("start_min >= 0 AND start_min < 60", name="check_start_min"),
        CheckConstraint("end_hr >= 0 AND end_hr < 24", name="check_end_hr"),
        CheckConstraint("end_min >= 0 AND end_min < 60", name="check_end_min"),
    )
