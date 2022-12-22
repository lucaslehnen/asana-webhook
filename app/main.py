from typing import Union
from fastapi import FastAPI, Response, Header, Request


app = FastAPI()


@app.get("/asana")
def read_root():
    return {"Asana": "Hooks"}


@app.post("/asana")
async def update_item(request: Request, response: Response, x_hook_secret: str | None = Header(default=None)):
    response.headers["X-Hook-Secret"] = x_hook_secret

    return await request.json()
