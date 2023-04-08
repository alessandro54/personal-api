from app.db.database import db
from .post import Post

def create_tables():
    with db:
        db.create_tables([Post])
