from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from db.base import Base


class Experience(Base):
    __tablename__ = "experiences"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), index=True)
    content = Column(String(1000))
    created_at = Column(DateTime(), default=datetime.now())
    updated_at = Column(DateTime(), onupdate=datetime.now())

    def __repr__(self):
        return f"Experience(id={self.id}, title={self.title}, content={self.content}, created_at={self.created_at}, updated_at={self.updated_at})"
