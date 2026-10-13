from pydantic import BaseModel, Field
from typing import Optional

class CourseBase(BaseModel):
    course_id: str = Field(..., max_length=8)
    title: Optional[str] = Field(None, max_length=50)
    dept_name: Optional[str] = Field(None, max_length=20)

class CourseCreate(CourseBase):
    credits: Optional[int] = Field(None, gt=0, le=99)

class CourseResponse(CourseBase):
    credits: Optional[int]
    model_config = {"from_attributes": True}

