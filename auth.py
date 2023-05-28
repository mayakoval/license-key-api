import os
from fastapi.security.api_key import APIKeyHeader
from fastapi import HTTPException, Security, status
from dotenv import load_dotenv


load_dotenv(dotenv_path=".env")


api_key_header = APIKeyHeader(name="access_token", auto_error=False)
api_key = os.getenv("API_KEY")


def get_api_key(api_key_header: str = Security(api_key_header)):
    if api_key_header == api_key:
        return api_key_header
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Secret not provided or incorrect",
        )
