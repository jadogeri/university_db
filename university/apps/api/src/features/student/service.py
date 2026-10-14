from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status
from features.student.models import Student, Advisor, Takes
from features.student.schemas import StudentCreate, AdvisorBase, TakesCreate


class StudentService:
    @staticmethod
    def get_all_students(db: Session, skip: int = 0, limit: int = 100):
        """Fetches a paginated list of students."""
        return db.query(Student).offset(skip).limit(limit).all()

    @staticmethod
    def get_student_by_id(db: Session, student_id: str):
        """Retrieves a specific student, raising a 404 if missing."""
        student = db.query(Student).filter(Student.id == student_id).first()
        if not student:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Student with ID '{student_id}' does not exist.",
            )
        return student

    @staticmethod
    def create_student(db: Session, student_data: StudentCreate):
        """Inserts a new student into the university catalog."""
        # Convert Pydantic model to SQLAlchemy Model (using the ID field alias)
        new_student = Student(
            id=student_data.id,
            name=student_data.name,
            dept_name=student_data.dept_name,
            tot_cred=student_data.tot_cred,
        )
        db.add(new_student)
        try:
            db.commit()
            db.refresh(new_student)
            return new_student
        except IntegrityError:
            db.rollback()
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Student record creation failed. Check if ID '{student_data.id}' or dept_name is invalid.",
            )

    @staticmethod
    def assign_advisor(db: Session, advisor_data: AdvisorBase):
        """Assigns or updates an academic advisor for a student."""
        # Clean lookups to verify matching targets
        StudentService.get_student_by_id(db, advisor_data.s_id)
        
        # Check if an advisor row already exists for this student
        existing_assignment = db.query(Advisor).filter(Advisor.s_id == advisor_data.s_id).first()
        
        if existing_assignment:
            existing_assignment.i_id = advisor_data.i_id
            db.commit()
            db.refresh(existing_assignment)
            return existing_assignment
        else:
            new_advisor = Advisor(s_id=advisor_data.s_id, i_id=advisor_data.i_id)
            db.add(new_advisor)
            try:
                db.commit()
                db.refresh(new_advisor)
                return new_advisor
            except IntegrityError:
                db.rollback()
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Failed to assign advisor. Verify Instructor ID is correct.",
                )

    @staticmethod
    def enroll_in_section(db: Session, enrollment_data: TakesCreate):
        """Enrolls a student into a specific course section."""
        # Verify student exists first
        StudentService.get_student_by_id(db, enrollment_data.id)
        
        new_enrollment = Takes(
            id=enrollment_data.id,
            course_id=enrollment_data.course_id,
            sec_id=enrollment_data.sec_id,
            semester=enrollment_data.semester,
            year=enrollment_data.year,
            grade=enrollment_data.grade,
        )
        db.add(new_enrollment)
        try:
            db.commit()
            db.refresh(new_enrollment)
            return new_enrollment
        except IntegrityError:
            db.rollback()
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Enrollment mapping failed. Verify target Section composite keys exist.",
            )
