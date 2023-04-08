from typing import Union

from fastapi import FastAPI

app = FastAPI()

# @app.on_event("startup")
# async def startup_event():
#     connect_db()

# @app.on_event("shutdown")
# async def shutdown_event():
#     disconnect_db()

@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
