from cryptography.fernet import Fernet
from dotenv import set_key


env_file = ".env"

secret_key = Fernet.generate_key()
key = "password_key"

set_key(env_file,key,secret_key.decode())

