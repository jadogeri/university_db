# Advisor Schemas
from typing import Optional

from pydantic import BaseModel, Field


class AdvisorBase(BaseModel):
    s_id: str = Field(..., max_length=5)
    i_id: Optional[str] = Field(None, max_length=5)

class AdvisorResponse(AdvisorBase):
    model_config = {"from_attributes": True}
