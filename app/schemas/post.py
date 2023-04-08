from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel, EmailStr


class PostBase(BaseModel):
    title: str
    content: Optional[str] = None


class PostCreate(PostBase):
    pass


class Post(PostBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True


class PostUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None

    class Config:
        orm_mode = True
