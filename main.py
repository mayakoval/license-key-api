from fastapi import Depends, FastAPI
from pydantic import BaseModel

import auth

app = FastAPI()

# Model for request body
class RequestModel(BaseModel):
    full_name: str
    software_package: str


# key generator
def key_generator(request: RequestModel):
    api_key = "test"
    full_key = request.full_name + request.software_package + api_key
    return full_key


# Endpoint generating key: takes name, software and secret
@app.post("/key-generator/", dependencies=[Depends(auth.get_api_key)])
async def generate_key(request: RequestModel):
    # generate key
    generated_key = key_generator(request)
    # hash the generated key
    return generated_key


# Endpoint validating the key
