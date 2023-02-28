import os
from typing import Union
from fastapi import FastAPI

app = FastAPI()


@app.get("/status")
def status():
    sha = os.environ.get('COMMIT_SHA')
    return {"sha": sha}


@app.get("/hello")
def hello():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
