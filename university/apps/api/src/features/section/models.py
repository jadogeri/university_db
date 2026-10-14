from sqlalchemy import Column, String, Integer, ForeignKey, ForeignKeyConstraint, CheckConstraint
from sqlalchemy.orm import relationship
from database import Base
from constants import TableNames

class Section(Base):
    __tablename__ = TableNames.SECTION
    
    course_id = Column(String(8), ForeignKey(f"{TableNames.COURSE}.course_id", ondelete="CASCADE"), primary_key=True)
    sec_id = Column(String(8), primary_key=True)
    semester = Column(String(6), primary_key=True)
    year = Column(Integer, primary_key=True)
    building = Column(String(15))
    room_number = Column(String(7))
    time_slot_id = Column(String(4))
    
    __table_args__ = (
        ForeignKeyConstraint(
            ["building", "room_number"], 
            [f"{TableNames.CLASSROOM}.building", f"{TableNames.CLASSROOM}.room_number"], 
            ondelete="SET NULL"
        ),
        CheckConstraint("semester IN ('Fall', 'Winter', 'Spring', 'Summer')", name="check_semester"),
        CheckConstraint("year > 1701 AND year < 2100", name="check_year"),
    )
    
    course = relationship("Course", back_populates="sections")
    teachers = relationship("Teaches", back_populates="section")
    student_enrollments = relationship("Takes", back_populates="section")


class Teaches(Base):
    __tablename__ = TableNames.TEACHES
    
    id = Column("ID", String(5), ForeignKey(f"{TableNames.INSTRUCTOR}.ID", ondelete="CASCADE"), primary_key=True)
    course_id = Column(String(8), primary_key=True)
    sec_id = Column(String(8), primary_key=True)
    semester = Column(String(6), primary_key=True)
    year = Column(Integer, primary_key=True)
    
    __table_args__ = (
        ForeignKeyConstraint(
            ["course_id", "sec_id", "semester", "year"],
            [f"{TableNames.SECTION}.course_id", f"{TableNames.SECTION}.sec_id", f"{TableNames.SECTION}.semester", f"{TableNames.SECTION}.year"],
            ondelete="CASCADE"
        ),
    )
    
    instructor = relationship("Instructor", back_populates="teaches_classes")
    section = relationship("Section", back_populates="teachers")
