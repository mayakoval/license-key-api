from fastapi.testclient import TestClient

from main import app
import crypto

client = TestClient(app)

mock_license_key = 'gAAAAABkdQ55e7UpQDk0QPIRD01wptWdL6zDoaAN22fs6Pq5qTW_pfSM6iPZRm82JTTc1KViWqfMkKNKgouuLAlLBBX37_ZLt3_17KFVABPsn-d9mJaCjnc='
mock_user_name = 'Maya Tester'
incorrect_user_name = 'Anonymous'

def test_decrypt_key_correctly():
    result = crypto.decrypt_key(mock_license_key, mock_user_name)
    assert result == True

def test_decrypt_key_incorrectly():
    result = crypto.decrypt_key(mock_license_key, incorrect_user_name)
    assert result == False
