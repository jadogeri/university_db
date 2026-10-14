from fastapi import APIRouter, Depends, status, Query
from sqlalchemy.orm import Session
from typing import List

from database import get_db
from features.course.service import CourseService
from features.course.schemas import (
    CourseCreate,
    CourseResponse,
    PrereqAssignment,
    CourseWithPrereqResponse,
)

router = APIRouter(prefix="/courses", tags=["Courses"])


@router.get("/", response_model=List[CourseResponse], status_code=status.HTTP_200_OK)
def read_all_courses(
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=100, ge=1, le=500),
    db: Session = Depends(get_db),
):
    """Retrieves all registered university courses with standard attributes."""
    return CourseService.get_all_courses(db=db, skip=skip, limit=limit)


@router.get("/{course_id}", response_model=CourseWithPrereqResponse, status_code=status.HTTP_200_OK)
def read_course_details(course_id: str, db: Session = Depends(get_db)):
    """Retrieves detailed information for a single course, including all its prerequisite items."""
    return CourseService.get_course_by_id(db=db, course_id=course_id)


@router.post("/", response_model=CourseResponse, status_code=status.HTTP_201_CREATED)
def create_new_course(course_in: CourseCreate, db: Session = Depends(get_db)):
    """Creates a new course entity within the university catalog mapping."""
    return CourseService.create_course(db=db, course_data=course_in)


@router.post("/prerequisites", response_model=CourseWithPrereqResponse, status_code=status.HTTP_200_OK)
def assign_course_prerequisite(assignment_in: PrereqAssignment, db: Session = Depends(get_db)):
    """Assigns an existing course as a structural academic prerequisite to another course."""
    return CourseService.add_prerequisite(db=db, assignment=assignment_in)
