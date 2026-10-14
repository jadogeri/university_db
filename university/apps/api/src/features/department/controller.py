from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from features.department.service import DepartmentService
from features.department.schemas import DepartmentCreate, DepartmentResponse, InstructorCreate, InstructorResponse

router = APIRouter(prefix="/departments", tags=["Departments & Instructors"])

@router.post("/", response_model=DepartmentResponse, status_code=status.HTTP_201_CREATED)
def create_department(payload: DepartmentCreate, db: Session = Depends(get_db)):
    return DepartmentService.create_department(db, payload)

@router.get("/", response_model=List[DepartmentResponse])
def read_departments(db: Session = Depends(get_db)):
    return DepartmentService.get_departments(db)

@router.post("/instructors", response_model=InstructorResponse, status_code=status.HTTP_201_CREATED)
def create_instructor(payload: InstructorCreate, db: Session = Depends(get_db)):
    return DepartmentService.create_instructor(db, payload)

@router.get("/instructors", response_model=List[InstructorResponse])
def read_instructors(db: Session = Depends(get_db)):
    return DepartmentService.get_instructors(db)
