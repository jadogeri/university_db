from sqlalchemy import String, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.orm import Mapped, mapped_column

from pydantic import BaseModel, Field
from constants import TableNames


class PrereqBase(BaseModel):
    course_id: str = Field(..., max_length=8)
    prereq_id: str = Field(..., max_length=8)

class PrereqCreate(PrereqBase):
    pass

class PrereqResponse(PrereqBase):
    model_config = {"from_attributes": True}    

    course_id: Mapped[str] = mapped_column(String(8), ForeignKey(f"{TableNames.COURSE}.course_id", ondelete="CASCADE"), primary_key=True)
    prereq_id: Mapped[str] = mapped_column(String(8), ForeignKey(f"{TableNames.COURSE}.course_id"), primary_key=True)

    __table_args__ = (PrimaryKeyConstraint("course_id", "prereq_id"),)
