import os
from dotenv import load_dotenv
from cryptography.fernet import Fernet
import secret_manager.password.encryption as encryption

load_dotenv()

def decrypt_password(password:str):
    secret_key = os.getenv("password_key")
    chipher = Fernet(secret_key)
    decrypted_password = chipher.decrypt(password.encode())
    return decrypted_password.decode()



if __name__ == "__main__":
    password = "12345@"
    encrypted_password = encryption.encrypt_password(password)
    print("Encryted_Passowrd:",encrypted_password)
    decrypted_password = decrypt_password(encrypted_password)
    print("Decrypted_password:",decrypted_password)

