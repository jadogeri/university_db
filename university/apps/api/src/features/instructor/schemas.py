from pydantic import BaseModel, Field
from typing import Optional

class InstructorBase(BaseModel):
    id: str = Field(..., max_length=5)
    name: str = Field(..., max_length=20)
    dept_name: Optional[str] = Field(None, max_length=20)

class InstructorCreate(InstructorBase):
    salary: Optional[float] = Field(None, gt=29000)

class InstructorResponse(InstructorBase):
    salary: Optional[float]
    model_config = {"from_attributes": True}
