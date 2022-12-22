from typing import Union
from fastapi import FastAPI, Response, Header, Request
from app.services.asana import AsanaAPI
import os


app = FastAPI()
asana = AsanaAPI(os.getenv('ASANA_TOKEN', ''))


@app.get("/asana")
def read_root():
    return {"Asana": "Hooks"}


@app.post("/asana")
async def update_item(request: Request, response: Response):
    secret = request.headers.get('X-Hook-Secret', None)
    if secret:
        response.headers["X-Hook-Secret"] = secret

    events = await request.json()
    print(events)

    for event in events['events']:
        if event['action'] == 'added':
            if event['resource']['resource_type'] == 'task':
                if event['parent']['resource_type'] == 'task':
                    taskId = event['resource']['gid']

                    projectId = os.getenv('ASANA_REPOSITORY_PROJECT', '')
                    await asana.addAProjectToATask(taskId=taskId, projectId=projectId)

                    userId = event['user']['gid']
                    await asana.assigneeTask(taskId=taskId, userId=userId)


    return "ok"
