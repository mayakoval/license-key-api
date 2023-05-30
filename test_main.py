from fastapi.testclient import TestClient

from main import app
import auth

client = TestClient(app)

async def mock_api_key():
    return "test"

app.dependency_overrides[auth.get_api_key] = mock_api_key

mock_generator_request_body = {"full_name": "Maya Tester", "software_package": "microsoft"}
mock_validator_request_body = {"full_name": "maya tester", "key": "gAAAAABkdQ55e7UpQDk0QPIRD01wptWdL6zDoaAN22fs6Pq5qTW_pfSM6iPZRm82JTTc1KViWqfMkKNKgouuLAlLBBX37_ZLt3_17KFVABPsn-d9mJaCjnc="}

def test_generate_key():
    response = client.post("/key-generator/", json=mock_generator_request_body)
    response_data = response.json()
    assert response.status_code == 200
    assert "key" in response_data

def test_validate_key():
    response = client.post("/key-validator/", json=mock_validator_request_body)
    assert response.status_code == 204
