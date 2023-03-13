import os
from cryptography.fernet import Fernet


key = os.getenv("FERNET_KEY")
fernet = Fernet(key)

# https://www.geeksforgeeks.org/how-to-encrypt-and-decrypt-strings-in-python/
async def encrypt_key(generated_key: str):
    encrypted_key = fernet.encrypt(generated_key.encode())
    return encrypted_key
