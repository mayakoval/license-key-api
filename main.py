import os
from fastapi import Depends, FastAPI, HTTPException, Header, status
from pydantic import BaseModel

import auth
import crypto

app = FastAPI(
    title="Key generator-validator",
    description="API for generating a crypted license key and key validation",
    version="v1",
    docs_url="/",
)


class RequestModel(BaseModel):
    full_name: str
    software_package: str


def key_generator(request: RequestModel) -> str:
    api_key = os.getenv("API_KEY")
    full_key = request.full_name + " " + request.software_package + api_key
    return full_key


@app.post("/key-generator/", dependencies=[Depends(auth.get_api_key)])
async def generate_key(request: RequestModel):
    generated_key = key_generator(request)
    encrypted_key = await crypto.encrypt_key(generated_key)
    return {"key": encrypted_key}


@app.get("/key-validator/")
async def validate_key(
    user_name: str = Header(),
    license_key: str = Header(),
):
    result = await crypto.decrypt_key(license_key, user_name)
    if result == True:
        raise HTTPException(
            status_code=status.HTTP_204_NO_CONTENT,
        )
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
