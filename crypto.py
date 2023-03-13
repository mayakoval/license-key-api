import os
from cryptography.fernet import Fernet


key = os.getenv("FERNET_KEY")
fernet = Fernet(key)

# https://www.geeksforgeeks.org/how-to-encrypt-and-decrypt-strings-in-python/
async def encrypt_key(generated_key: str):
    encrypted_key = fernet.encrypt(generated_key.encode())
    return encrypted_key


async def decrypt_key(license_key: str, user_name: str):
    decrypted_key = (fernet.decrypt(license_key)).decode()
    name = decrypted_key.split()[:2]
    full_name = name[0] + " " + name[1]
    if user_name == full_name:
        return True
