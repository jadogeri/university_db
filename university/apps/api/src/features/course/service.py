from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status
from features.course.models import Course, prereq
from features.course.schemas import CourseCreate, PrereqAssignment


class CourseService:
    @staticmethod
    def get_all_courses(db: Session, skip: int = 0, limit: int = 100):
        """Fetches a paginated list of courses from the catalog."""
        return db.query(Course).offset(skip).limit(limit).all()

    @staticmethod
    def get_course_by_id(db: Session, course_id: str):
        """Retrieves a specific course by its primary key, raising 404 if missing."""
        course = db.query(Course).filter(Course.course_id == course_id).first()
        if not course:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Course with ID '{course_id}' does not exist.",
            )
        return course

    @staticmethod
    def create_course(db: Session, course_data: CourseCreate):
        """Inserts a new course blueprint into the university curriculum."""
        new_course = Course(
            course_id=course_data.course_id,
            title=course_data.title,
            dept_name=course_data.dept_name,
            credits=course_data.credits,
        )
        db.add(new_course)
        try:
            db.commit()
            db.refresh(new_course)
            return new_course
        except IntegrityError:
            db.rollback()
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Course creation failed. Ensure course_id '{course_data.course_id}' is unique and dept_name is valid.",
            )

    @staticmethod
    def add_prerequisite(db: Session, assignment: PrereqAssignment):
        """Links a prerequisite course to a target course via the association table."""
        # 1. Prevent an immediate circular logic trap
        if assignment.course_id == assignment.prereq_id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="A course cannot be a prerequisite of itself.",
            )

        # 2. Verify both courses actually exist first
        course = CourseService.get_course_by_id(db, assignment.course_id)
        prereq_course = CourseService.get_course_by_id(db, assignment.prereq_id)

        # 3. Check if relationship mapping already exists
        if prereq_course in course.prerequisites:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Course '{assignment.prereq_id}' is already a prerequisite for '{assignment.course_id}'.",
            )

        # 4. Append relationship cleanly via SQLAlchemy model trackers
        course.prerequisites.append(prereq_course)
        try:
            db.commit()
            return course
        except Exception:
            db.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to establish prerequisite mapping table record.",
            )
