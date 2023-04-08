from fastapi import APIRouter, Depends
from app.services.post_service import get_posts
from app.db.util import get_db
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/posts",
    tags=["posts"],
    dependencies=[
        Depends(get_db)
    ],
    responses={404: {"description": "Not found"}},
)


@router.get("/", tags=["posts"])
async def read_all(db: Session = Depends(get_db)):
    return {"posts": get_posts(db)}
