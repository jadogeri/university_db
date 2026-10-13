from pydantic import BaseModel, Field
from typing import Optional

class DepartmentBase(BaseModel):
    dept_name: str = Field(..., max_length=20)
    building: Optional[str] = Field(None, max_length=15)

class DepartmentCreate(DepartmentBase):
    budget: Optional[float] = Field(None, gt=0)

class DepartmentResponse(DepartmentBase):
    budget: Optional[float]
    model_config = {"from_attributes": True}
