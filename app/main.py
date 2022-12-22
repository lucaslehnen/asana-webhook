from typing import Union
from fastapi import FastAPI, Response, Header


app = FastAPI()


@app.get("/asana")
def read_root():
    return {"Hello": "World"}


@app.post("/asana")
def update_item(response: Response, x_hook_secret: str | None = Header(default=None)):
    response.headers["X-Hook-Secret"] = x_hook_secret

    return ""
