# apps/api/src/section/schemas.py
from pydantic import BaseModel, Field
from typing_extensions import Literal

# ==========================================
# TEACHES DATA MODELS (DTOs)
# ==========================================

class TeachesBase(BaseModel):
    """
    Base properties shared across all Teaches request and response states.
    Enforces exact textbook datatype bounds.
    """
    # Maps to your "ID" column (Varchar(5) in the textbook)
    id: str = Field(..., max_length=5, min_length=1, description="The unique 5-character ID of the Instructor")
    
    # Composite target fields linking directly to the Section composite primary key
    course_id: str = Field(..., max_length=8, description="The 8-character Course Identifier code")
    sec_id: str = Field(..., max_length=8, description="The Section ID identifier")
    
    # Statically validates allowed textbook values using a Pydantic Literal type guard
    semester: Literal['Fall', 'Winter', 'Spring', 'Summer'] = Field(..., description="Academic term")
    
    # Enforces your exact numeric boundaries checked in the SQL schema
    year: int = Field(..., gt=1701, lt=2100, description="The 4-digit academic calendar year")


class TeachesCreate(TeachesBase):
    """
    The Input Data Model: What the frontend must pass to assign an instructor to teach a section.
    Inherits all properties from TeachesBase without adding extra fields.
    """
    pass


class TeachesResponse(TeachesBase):
    """
    The Output Data Model: Defines how teaching assignment records serialize back into JSON.
    """
    # This configuration lets Pydantic read values straight from your SQLAlchemy 
    # Teaches entity rows automatically, mapping "id" seamlessly from the database "ID" column tag.
    model_config = {"from_attributes": True}
