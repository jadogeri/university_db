from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from features.section.service import SectionService
from features.section.schemas import SectionCreate, SectionResponse, TeachesCreate, TeachesResponse

router = APIRouter(prefix="/sections", tags=["Sections & Teaching Schedules"])

@router.post("/", response_model=SectionResponse, status_code=status.HTTP_201_CREATED)
def create_section(payload: SectionCreate, db: Session = Depends(get_db)):
    return SectionService.create_section(db, payload)

@router.get("/", response_model=List[SectionResponse])
def read_sections(db: Session = Depends(get_db)):
    return SectionService.get_sections(db)

@router.post("/assign-instructor", response_model=TeachesResponse, status_code=status.HTTP_201_CREATED)
def assign_instructor_to_section(payload: TeachesCreate, db: Session = Depends(get_db)):
    return SectionService.assign_teacher(db, payload)
