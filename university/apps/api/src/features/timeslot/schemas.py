from pydantic import BaseModel, Field

class TimeSlotBase(BaseModel):
    time_slot_id: str = Field(..., max_length=4)
    day: str = Field(..., max_length=1)
    start_hr: int = Field(..., ge=0, lt=24)
    start_min: int = Field(..., ge=0, lt=60)

class TimeSlotCreate(TimeSlotBase):
    end_hr: int = Field(..., ge=0, lt=24)
    end_min: int = Field(..., ge=0, lt=60)

class TimeSlotResponse(TimeSlotBase):
    end_hr: int
    end_min: int
    model_config = {"from_attributes": True}
