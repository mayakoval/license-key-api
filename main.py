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


class GeneratorRequestModel(BaseModel):
    full_name: str
    software_package: str

class ValidatorRequestModel(BaseModel):
    full_name: str
    key: str


def key_generator(request: GeneratorRequestModel) -> str:
    api_key = os.getenv("API_KEY")
    full_key = request.full_name + " " + request.software_package + api_key
    return full_key


@app.post("/key-generator/", dependencies=[Depends(auth.get_api_key)])
def generate_key(request: GeneratorRequestModel):
    generated_key = key_generator(request)
    encrypted_key = crypto.encrypt_key(generated_key)
    return {"key": encrypted_key}


@app.post("/key-validator/", dependencies=[Depends(auth.get_api_key)])
def validate_key(request: ValidatorRequestModel):
    result = crypto.decrypt_key(request.key, request.full_name)
    if result == True:
        raise HTTPException(
            status_code=status.HTTP_204_NO_CONTENT,
        )
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
