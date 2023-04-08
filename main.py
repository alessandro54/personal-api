from fastapi import FastAPI
from app.controllers.posts_controllers import router as posts_router

app = FastAPI()

app.include_router(posts_router)


@app.get("/")
async def greet():
    return {"message": "Hello World"}
