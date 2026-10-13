from pydantic import BaseModel, Field
from typing import Optional
from typing_extensions import Literal

# Takes Schemas (Enrollment)
class TakesBase(BaseModel):
    id: str = Field(..., max_length=5)
    course_id: str = Field(..., max_length=8)
    sec_id: str = Field(..., max_length=8)
    semester: str = Field(..., max_length=6)
    year: int

class TakesCreate(TakesBase):
    grade: Optional[str] = Field(None, max_length=2)

class TakesResponse(TakesCreate):
    model_config = {"from_attributes": True}
