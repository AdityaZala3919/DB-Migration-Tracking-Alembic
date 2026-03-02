from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional, List


# -------- USER SCHEMAS --------

class UserBase(BaseModel):
    full_name: str
    email: EmailStr


class UserCreate(UserBase):
    pass


class UserUpdate(BaseModel):
    full_name: Optional[str] = None
    email: Optional[EmailStr] = None


class UserResponse(BaseModel):
    id: int
    full_name: str
    email: EmailStr
    created_at: datetime
    first_name: Optional[str]
    last_name: Optional[str]

    class Config:
        from_attributes = True


# -------- PROJECT SCHEMAS --------

class ProjectBase(BaseModel):
    name: str
    user_id: int


class ProjectCreate(ProjectBase):
    pass


class ProjectResponse(BaseModel):
    id: int
    name: str
    user_id: int

    class Config:
        from_attributes = True