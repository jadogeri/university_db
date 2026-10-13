from pydantic import BaseModel, Field
from typing import Optional

class StudentBase(BaseModel):
    id: str = Field(..., max_length=5)
    name: str = Field(..., max_length=20)
    dept_name: Optional[str] = Field(None, max_length=20)

class StudentCreate(StudentBase):
    tot_cred: Optional[int] = Field(None, ge=0, le=999)

class StudentResponse(StudentBase):
    tot_cred: Optional[int]
    model_config = {"from_attributes": True}

