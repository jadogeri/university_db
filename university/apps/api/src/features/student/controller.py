from fastapi import APIRouter, Depends, status, Query
from sqlalchemy.orm import Session
from typing import List

from database import get_db  # Central context manager session provider
from features.student.service import StudentService
from features.student.schemas import (
    StudentCreate,
    StudentResponse,
    AdvisorBase,
    AdvisorResponse,
    TakesCreate,
    TakesResponse,
)

# Initializing routing group with explicit tagging for OpenAPI swagger UI
router = APIRouter(prefix="/students", tags=["Students"])


@router.get("/", response_model=List[StudentResponse], status_code=status.HTTP_200_OK)
def read_all_students(
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=100, ge=1, le=500),
    db: Session = Depends(get_db),
):
    """Retrieves all registered university student profiles via pagination."""
    return StudentService.get_all_students(db=db, skip=skip, limit=limit)


@router.get("/{student_id}", response_model=StudentResponse, status_code=status.HTTP_200_OK)
def read_student(student_id: str, db: Session = Depends(get_db)):
    """Retrieves a single student's metrics by their custom composite ID string."""
    return StudentService.get_student_by_id(db=db, student_id=student_id)


@router.post("/", response_model=StudentResponse, status_code=status.HTTP_201_CREATED)
def create_student(student_in: StudentCreate, db: Session = Depends(get_db)):
    """Creates a new student account profile inside the academic catalog."""
    return StudentService.create_student(db=db, student_data=student_in)


@router.post("/advisor", response_model=AdvisorResponse, status_code=status.HTTP_200_OK)
def assign_student_advisor(assignment_in: AdvisorBase, db: Session = Depends(get_db)):
    """Maps a student to an instructor for academic tracking."""
    return StudentService.assign_advisor(db=db, advisor_data=assignment_in)


@router.post("/enroll", response_model=TakesResponse, status_code=status.HTTP_201_CREATED)
def enroll_section(enrollment_in: TakesCreate, db: Session = Depends(get_db)):
    """Registers a student into an active class section roster mapping."""
    return StudentService.enroll_in_section(db=db, enrollment_data=enrollment_in)
