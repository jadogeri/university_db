from pydantic import BaseModel, Field
from typing import Optional

class ClassroomBase(BaseModel):
    building: str = Field(..., max_length=15)
    room_number: str = Field(..., max_length=7)

class ClassroomCreate(ClassroomBase):
    capacity: Optional[int] = Field(None, ge=0, le=9999)

class ClassroomResponse(ClassroomBase):
    capacity: Optional[int]
    model_config = {"from_attributes": True}
