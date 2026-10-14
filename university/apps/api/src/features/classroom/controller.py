from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from features.classroom.service import ClassroomService
from features.classroom.schemas import ClassroomCreate, ClassroomResponse, TimeSlotCreate, TimeSlotResponse

router = APIRouter(prefix="/classrooms", tags=["Classrooms & Time Slots"])

@router.post("/", response_model=ClassroomResponse, status_code=status.HTTP_201_CREATED)
def create_classroom(payload: ClassroomCreate, db: Session = Depends(get_db)):
    return ClassroomService.create_classroom(db, payload)

@router.get("/", response_model=List[ClassroomResponse])
def read_classrooms(db: Session = Depends(get_db)):
    return ClassroomService.get_classrooms(db)

@router.post("/time-slots", response_model=TimeSlotResponse, status_code=status.HTTP_201_CREATED)
def create_time_slot(payload: TimeSlotCreate, db: Session = Depends(get_db)):
    return ClassroomService.create_time_slot(db, payload)

@router.get("/time-slots", response_model=List[TimeSlotResponse])
def read_time_slots(db: Session = Depends(get_db)):
    return ClassroomService.get_time_slots(db)
