from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status
from features.section.models import Section, Teaches
from features.section.schemas import SectionCreate, TeachesCreate
        
class SectionService:
    @staticmethod
    def create_section(db: Session, data: SectionCreate):
        section = Section(
            course_id=data.course_id, sec_id=data.sec_id, semester=data.semester, year=data.year,
            building=data.building, room_number=data.room_number, time_slot_id=data.time_slot_id
        )
        db.add(section)
        try:
            db.commit()
            db.refresh(section)
            return section
        except IntegrityError:
            db.rollback()
            raise HTTPException(status_code=400, detail="Failed to create section. Ensure parent keys match.")

    @staticmethod
    def get_sections(db: Session):
        return db.query(Section).all()

    @staticmethod
    def assign_teacher(db: Session, data: TeachesCreate):
        teaching_assignment = Teaches(
            id=data.id, course_id=data.course_id, sec_id=data.sec_id,
            semester=data.semester, year=data.year
        )
        db.add(teaching_assignment)
        try:
            db.commit()
            db.refresh(teaching_assignment)
            return teaching_assignment
        except IntegrityError:
            db.rollback()
            raise HTTPException(status_code=400, detail="Teaching assignment failed. Composite section row missing.")
    @staticmethod
    def get_teaching_assignments(db: Session):
        return db.query(Teaches).all()