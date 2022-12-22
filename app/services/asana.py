import httpx
import json


class AsanaAPI:

  def __init__(self, personal_token) -> None:
    self.token = personal_token
    self.base_url = 'https://app.asana.com/api/1.0'

  def getHeader(self):
    return {
        'Content-type': 'application/json',
        'Authorization': f'Bearer {self.token}'
    }

  async def addAProjectToATask(self, taskId, projectId):

    url = f'{self.base_url}/tasks/{taskId}/addProject'
    data = {
        'data': {
            'project': projectId
        }
    }
    headers = self.getHeader()

    async with httpx.AsyncClient() as client:
        response = await client.post(url, data=json.dumps(data), headers=headers)

    return response

  async def assigneeTask(self, taskId, userId):

    url = f'{self.base_url}/tasks/{taskId}'
    data = {
        'data': {
            'assignee': userId
        }
    }
    headers = self.getHeader()

    async with httpx.AsyncClient() as client:
        response = await client.put(url, data=json.dumps(data), headers=headers)

    return response
