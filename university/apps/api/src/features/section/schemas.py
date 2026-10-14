from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum

class SemesterEnum(str, Enum):
    FALL = "Fall"
    WINTER = "Winter"
    SPRING = "Spring"
    SUMMER = "Summer"

# ==========================================
# Section Schemas
# ==========================================
class SectionBase(BaseModel):
    course_id: str = Field(..., max_length=8)
    sec_id: str = Field(..., max_length=8)
    semester: SemesterEnum
    year: int = Field(..., gt=1701, lt=2100)

class SectionCreate(SectionBase):
    building: Optional[str] = Field(None, max_length=15)
    room_number: Optional[str] = Field(None, max_length=7)
    time_slot_id: Optional[str] = Field(None, max_length=4)

class SectionResponse(SectionBase):
    building: Optional[str]
    room_number: Optional[str]
    time_slot_id: Optional[str]
    
    model_config = {"from_attributes": True}

# ==========================================
# Teaches Schemas
# ==========================================
class TeachesBase(BaseModel):
    id: str = Field(..., max_length=5, alias="ID")
    course_id: str = Field(..., max_length=8)
    sec_id: str = Field(..., max_length=8)
    semester: SemesterEnum
    year: int = Field(..., gt=1701, lt=2100)

class TeachesCreate(TeachesBase):
    pass

class TeachesResponse(TeachesBase):
    model_config = {"from_attributes": True, "populate_by_name": True}
