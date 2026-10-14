from pydantic import BaseModel, Field
from typing import Optional
from features.section.schemas import SemesterEnum

# ==========================================
# Student Schemas
# ==========================================
class StudentBase(BaseModel):
    id: str = Field(..., max_length=5, alias="ID")
    name: str = Field(..., max_length=20)

class StudentCreate(StudentBase):
    dept_name: Optional[str] = Field(None, max_length=20)
    tot_cred: int = Field(default=0, ge=0, le=999)

class StudentResponse(StudentBase):
    dept_name: Optional[str]
    tot_cred: int
    
    model_config = {"from_attributes": True, "populate_by_name": True}

# ==========================================
# Takes (Enrollment) Schemas
# ==========================================
class TakesBase(BaseModel):
    id: str = Field(..., max_length=5, alias="ID")
    course_id: str = Field(..., max_length=8)
    sec_id: str = Field(..., max_length=8)
    semester: SemesterEnum
    year: int = Field(..., gt=1701, lt=2100)

class TakesCreate(TakesBase):
    grade: Optional[str] = Field(None, max_length=2, description="Letter grade (e.g. A, B+, F)")

class TakesResponse(TakesBase):
    grade: Optional[str]
    
    model_config = {"from_attributes": True, "populate_by_name": True}

# ==========================================
# Advisor Schemas
# ==========================================
class AdvisorBase(BaseModel):
    s_id: str = Field(..., max_length=5, alias="s_ID")
    i_id: Optional[str] = Field(None, max_length=5, alias="i_ID")

class AdvisorCreate(AdvisorBase):
    pass

class AdvisorResponse(AdvisorBase):
    model_config = {"from_attributes": True, "populate_by_name": True}
