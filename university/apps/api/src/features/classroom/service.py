from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status
from features.classroom.models import Classroom, TimeSlot
from features.classroom.schemas import ClassroomCreate, TimeSlotCreate

class ClassroomService:
    @staticmethod
    def create_classroom(db: Session, data: ClassroomCreate):
        classroom = Classroom(building=data.building, room_number=data.room_number, capacity=data.capacity)
        db.add(classroom)
        try:
            db.commit()
            db.refresh(classroom)
            return classroom
        except IntegrityError:
            db.rollback()
            raise HTTPException(status_code=400, detail="Classroom already exists.")

    @staticmethod
    def get_classrooms(db: Session):
        return db.query(Classroom).all()

    @staticmethod
    def create_time_slot(db: Session, data: TimeSlotCreate):
        slot = TimeSlot(
            time_slot_id=data.time_slot_id, day=data.day,
            start_hr=data.start_hr, start_min=data.start_min,
            end_hr=data.end_hr, end_min=data.end_min
        )
        db.add(slot)
        try:
            db.commit()
            db.refresh(slot)
            return slot
        except IntegrityError:
            db.rollback()
            raise HTTPException(status_code=400, detail="Time slot structural mapping already exists.")

    @staticmethod
    def get_time_slots(db: Session):
        return db.query(TimeSlot).all()
