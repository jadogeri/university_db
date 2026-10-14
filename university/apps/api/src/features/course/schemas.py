from pydantic import BaseModel, Field
from typing import Optional, List

# ==========================================
# Course Schemas
# ==========================================
class CourseBase(BaseModel):
    course_id: str = Field(..., max_length=8)
    title: str = Field(..., max_length=50)

class CourseCreate(CourseBase):
    dept_name: Optional[str] = Field(None, max_length=20)
    credits: int = Field(..., gt=0, le=99)

class CourseResponse(CourseBase):
    dept_name: Optional[str]
    credits: int
    
    model_config = {"from_attributes": True}

# ==========================================
# Prerequisite Nesting/Asignment Schemas
# ==========================================
class PrereqAssignment(BaseModel):
    course_id: str = Field(..., max_length=8)
    prereq_id: str = Field(..., max_length=8)

class CourseWithPrereqResponse(CourseResponse):
    """Extends standard response to map downstream prerequisite structural arrays"""
    prerequisites: List[CourseResponse] = []
