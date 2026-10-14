from sqlalchemy import Column, String, Integer, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship
from database import Base
from constants import TableNames

class Course(Base):
    __tablename__ = TableNames.COURSE
    
    course_id = Column(String(8), primary_key=True)
    title = Column(String(50))
    dept_name = Column(String(20), ForeignKey(f"{TableNames.DEPARTMENT}.dept_name", ondelete="SET NULL"), nullable=True)
    credits = Column(Integer)
    
    __table_args__ = (
        CheckConstraint("credits > 0", name="check_credits"),
    )
    
    department = relationship("Department", back_populates="courses")
    sections = relationship("Section", back_populates="course")
    
    # Self-Referential Many-to-Many setup using string targets for Prereq
    prerequisites = relationship(
        "Course",
        secondary=TableNames.PREREQ,
        primaryjoin="Course.course_id == prereq.c.course_id",
        secondaryjoin="Course.course_id == prereq.c.prereq_id",
        backref="required_for"
    )


# Prereq association declared cleanly under course
from sqlalchemy import Table
prereq = Table(
    TableNames.PREREQ,
    Base.metadata,
    Column("course_id", String(8), ForeignKey(f"{TableNames.COURSE}.course_id", ondelete="CASCADE"), primary_key=True),
    Column("prereq_id", String(8), ForeignKey(f"{TableNames.COURSE}.course_id", ondelete="CASCADE"), primary_key=True),
)
