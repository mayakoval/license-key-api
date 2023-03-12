from fastapi import Depends, FastAPI
from pydantic import BaseModel

import auth

app = FastAPI()

# Model for request body
class RequestModel(BaseModel):
    full_name: str
    software_package: str


# Endpoint generating key: takes name, software and secret
@app.post("/key-generator/", dependencies=[Depends(auth.get_api_key)])
async def generate_key(request: RequestModel):
    return request


# Endpoint validating the key
