# AUTOGENERATED! DO NOT EDIT! File to edit: test_nbdev.ipynb (unless otherwise specified).

__all__ = ["root", "read_item", "main", "app"]

# Cell

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
    print("Hello World")
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True, workers=2)


if __name__ == "__main__":
    main()
