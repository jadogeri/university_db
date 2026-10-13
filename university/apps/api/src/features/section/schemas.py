from pydantic import BaseModel, Field
from typing import Optional
from typing_extensions import Literal

class SectionBase(BaseModel):
    course_id: str = Field(..., max_length=8)
    sec_id: str = Field(..., max_length=8)
    semester: Literal['Fall', 'Winter', 'Spring', 'Summer']
    year: int = Field(..., gt=1701, lt=2100)

class SectionCreate(SectionBase):
    building: Optional[str] = Field(None, max_length=15)
    room_number: Optional[str] = Field(None, max_length=7)
    time_slot_id: Optional[str] = Field(None, max_length=4)

class SectionResponse(SectionCreate):
    model_config = {"from_attributes": True}