from sqlalchemy import Column, String, Integer, ForeignKey, ForeignKeyConstraint, CheckConstraint
from sqlalchemy.orm import relationship
from database import Base
from constants import TableNames

class Student(Base):
    __tablename__ = TableNames.STUDENT
    
    id = Column("ID", String(5), primary_key=True)
    name = Column(String(20), nullable=False)
    dept_name = Column(String(20), ForeignKey(f"{TableNames.DEPARTMENT}.dept_name", ondelete="SET NULL"), nullable=True)
    tot_cred = Column(Integer, default=0)
    
    __table_args__ = (
        CheckConstraint("tot_cred >= 0", name="check_tot_cred"),
    )
    
    department = relationship("Department", back_populates="students")
    classes_taken = relationship("Takes", back_populates="student")
    advisor_assignment = relationship("Advisor", back_populates="student", uselist=False)


class Takes(Base):
    __tablename__ = TableNames.TAKES
    
    id = Column("ID", String(5), ForeignKey(f"{TableNames.STUDENT}.ID", ondelete="CASCADE"), primary_key=True)
    course_id = Column(String(8), primary_key=True)
    sec_id = Column(String(8), primary_key=True)
    semester = Column(String(6), primary_key=True)
    year = Column(Integer, primary_key=True)
    grade = Column(String(2))
    
    __table_args__ = (
        ForeignKeyConstraint(
            ["course_id", "sec_id", "semester", "year"],
            [f"{TableNames.SECTION}.course_id", f"{TableNames.SECTION}.sec_id", f"{TableNames.SECTION}.semester", f"{TableNames.SECTION}.year"],
            ondelete="CASCADE"
        ),
    )
    
    student = relationship("Student", back_populates="classes_taken")
    section = relationship("Section", back_populates="student_enrollments")


class Advisor(Base):
    __tablename__ = TableNames.ADVISOR
    
    s_id = Column("s_ID", String(5), ForeignKey(f"{TableNames.STUDENT}.ID", ondelete="CASCADE"), primary_key=True)
    i_id = Column("i_ID", String(5), ForeignKey(f"{TableNames.INSTRUCTOR}.ID", ondelete="SET NULL"))
    
    student = relationship("Student", back_populates="advisor_assignment")
    instructor = relationship("Instructor", back_populates="advised_students")
