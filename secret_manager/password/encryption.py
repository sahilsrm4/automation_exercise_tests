from cryptography.fernet import Fernet
import os
from dotenv import load_dotenv

load_dotenv()

def encrypt_password(password:str):
    secret_key = os.getenv("password_key")
    cipher = Fernet(secret_key.encode())
    encrypted_message = cipher.encrypt(password.encode())

    return encrypted_message.decode()
