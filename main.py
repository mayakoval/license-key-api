import os
from dotenv import load_dotenv
from fastapi import Depends, FastAPI
from pydantic import BaseModel

import auth
import crypto

app = FastAPI()

load_dotenv(dotenv_path=".env")


class RequestModel(BaseModel):
    full_name: str
    software_package: str


def key_generator(request: RequestModel):
    api_key = os.getenv("API_KEY")
    full_key = request.full_name + request.software_package + api_key
    return full_key


@app.post("/key-generator/", dependencies=[Depends(auth.get_api_key)])
async def generate_key(request: RequestModel):
    generated_key = key_generator(request)
    encrypted_key = await crypto.encrypt_key(generated_key)
    return {"key": encrypted_key}


# Endpoint validating the key
