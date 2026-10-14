from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status
from features.department.models import Department, Instructor
from features.department.schemas import DepartmentCreate, InstructorCreate

class DepartmentService:
    @staticmethod
    def create_department(db: Session, data: DepartmentCreate):
        dept = Department(dept_name=data.dept_name, building=data.building, budget=data.budget)
        db.add(dept)
        try:
            db.commit()
            db.refresh(dept)
            return dept
        except IntegrityError:
            db.rollback()
            raise HTTPException(status_code=400, detail="Department name duplicate constraint violation.")

    @staticmethod
    def get_departments(db: Session):
        return db.query(Department).all()

    @staticmethod
    def create_instructor(db: Session, data: InstructorCreate):
        instructor = Instructor(id=data.id, name=data.name, dept_name=data.dept_name, salary=data.salary)
        db.add(instructor)
        try:
            db.commit()
            db.refresh(instructor)
            return instructor
        except IntegrityError:
            db.rollback()
            raise HTTPException(status_code=400, detail="Instructor creation failed. Verify Department exists.")

    @staticmethod
    def get_instructors(db: Session):
        return db.query(Instructor).all()
