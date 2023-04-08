from sqlalchemy.orm import Session
from sqlalchemy import update
from fastapi import HTTPException
from app.models.post import Post

def get_posts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Post).offset(skip).limit(limit).all()
