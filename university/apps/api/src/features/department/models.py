from sqlalchemy import Column, String, Numeric, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship
from database import Base
from constants import TableNames

class Department(Base):
    __tablename__ = TableNames.DEPARTMENT
    
    dept_name = Column(String(20), primary_key=True)
    building = Column(String(15))
    budget = Column(Numeric(12, 2))
    
    __table_args__ = (
        CheckConstraint("budget > 0", name="check_budget"),
    )
    
    # Relationships using forward string targets
    instructors = relationship("Instructor", back_populates="department")
    courses = relationship("Course", back_populates="department")
    students = relationship("Student", back_populates="department")


class Instructor(Base):
    __tablename__ = TableNames.INSTRUCTOR
    
    id = Column("ID", String(5), primary_key=True)
    name = Column(String(20), nullable=False)
    dept_name = Column(String(20), ForeignKey(f"{TableNames.DEPARTMENT}.dept_name", ondelete="SET NULL"), nullable=True)
    salary = Column(Numeric(8, 2))
    
    __table_args__ = (
        CheckConstraint("salary > 29000", name="check_salary"),
    )
    
    department = relationship("Department", back_populates="instructors")
    teaches_classes = relationship("Teaches", back_populates="instructor")
    advised_students = relationship("Advisor", back_populates="instructor")
