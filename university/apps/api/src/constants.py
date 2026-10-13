# apps/api/src/constants.py
from enum import Enum

class TableNames(str, Enum):
    ADVISOR = "advisor"
    CLASSROOM = "classroom"
    COURSE = "course"
    DEPARTMENT = "department"
    INSTRUCTOR = "instructor"
    PREREQ = "prereq"
    SECTION = "section"
    STUDENT = "student"
    TAKES = "takes"
    TEACHES = "teaches"
    TIME = "time"
