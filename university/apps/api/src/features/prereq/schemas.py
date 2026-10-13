# Prereq Schemas
from pydantic import Field

from pydantic import BaseModel


class PrereqBase(BaseModel):
    course_id: str = Field(..., max_length=8)
    prereq_id: str = Field(..., max_length=8)

class PrereqResponse(PrereqBase):
    model_config = {"from_attributes": True}
    