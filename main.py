from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Model for request body
class RequestModel(BaseModel):
    full_name: str
    software_package: str
    secret: str

# Endpoint generating key: takes name, software and secret
@app.post("/key-generator/")
async def generate_key(request):
    return request

# Endpoint validating the key
