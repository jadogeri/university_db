from pydantic import BaseModel, Field
from typing import Optional
from decimal import Decimal

# ==========================================
# Department Schemas
# ==========================================
class DepartmentBase(BaseModel):
    dept_name: str = Field(..., max_length=20)

class DepartmentCreate(DepartmentBase):
    building: Optional[str] = Field(None, max_length=15)
    budget: Decimal = Field(..., gt=0, max_digits=12, decimal_places=2)

class DepartmentResponse(DepartmentBase):
    building: Optional[str]
    budget: Decimal
    
    model_config = {"from_attributes": True}

# ==========================================
# Instructor Schemas
# ==========================================
class InstructorBase(BaseModel):
    id: str = Field(..., max_length=5, alias="ID")
    name: str = Field(..., max_length=20)

class InstructorCreate(InstructorBase):
    dept_name: Optional[str] = Field(None, max_length=20)
    salary: Decimal = Field(..., gt=29000, max_digits=8, decimal_places=2)

class InstructorResponse(InstructorBase):
    dept_name: Optional[str]
    salary: Decimal
    
    model_config = {"from_attributes": True, "populate_by_name": True}
