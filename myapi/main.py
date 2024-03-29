__all__ = ["root", "read_item", "main", "app"]


import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


def main():
    print("Loading Hello World...")

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True, workers=2)
