from typing import Union
from fastapi import FastAPI, Response, Header, Request


app = FastAPI()


@app.get("/asana")
def read_root():
    return {"Asana": "Hooks"}


@app.post("/asana")
async def update_item(request: Request, response: Response):
    secret = request.headers.get('X-Hook-Secret', None)
    if secret:
        response.headers["X-Hook-Secret"] = secret

    print(await request.json())

    return "ok"
