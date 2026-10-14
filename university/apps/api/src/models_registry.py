# from src.database import Base

from src.features.classroom.models import Classroom
from src.features.timeslot.models import TimeSlot
from src.features.department.models import Department
from src.features.course.models import Course, Prereq
from src.features.instructor.models import Instructor
from src.features.student.models import Student, Advisor
from src.features.section.models import Section, Teaches, Takes

__all__ = [
    "Base", "Classroom", "TimeSlot", "Department", "Course", 
    "Prereq", "Instructor", "Student", "Advisor", "Section", "Teaches", "Takes"
]
