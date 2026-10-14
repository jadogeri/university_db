from pydantic import BaseModel, Field
from typing import Optional

# ==========================================
# Classroom Schemas
# ==========================================
class ClassroomBase(BaseModel):
    building: str = Field(..., max_length=15)
    room_number: str = Field(..., max_length=7)

class ClassroomCreate(ClassroomBase):
    capacity: Optional[int] = Field(None, ge=0, le=9999)

class ClassroomResponse(ClassroomBase):
    capacity: Optional[int]
    
    model_config = {"from_attributes": True}

# ==========================================
# Time Slot Schemas
# ==========================================
class TimeSlotBase(BaseModel):
    time_slot_id: str = Field(..., max_length=4)
    day: str = Field(..., max_length=1, description="Single character representation (e.g., M, T, W)")
    start_hr: int = Field(..., ge=0, lt=24)
    start_min: int = Field(..., ge=0, lt=60)

class TimeSlotCreate(TimeSlotBase):
    end_hr: int = Field(..., ge=0, lt=24)
    end_min: int = Field(..., ge=0, lt=60)

class TimeSlotResponse(TimeSlotBase):
    end_hr: int
    end_min: int
    
    model_config = {"from_attributes": True}
