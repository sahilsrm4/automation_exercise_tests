import sys
sys.path.append("D:\WatchGuard\playwright_opencart_project")
import os

from secret_manager.password.encryption import encrypt_password
from secret_manager.password.decryption import decrypt_password
from utils.csv_handler import read_csv,create_csv


def encrypt_test_data_password():

    cwd = os.getcwd()
    relative_file_path = "test_data/valid_login.csv"
    file_path = os.path.join(cwd,relative_file_path)
    file_data = read_csv(file_path)
    encrypted_data = []
    for data in file_data:
        password = data["password"]
        encrypted_password = encrypt_password(password)
        encrypted_data.append({"email":data["email"],"password":encrypted_password})
    create_csv(encrypted_data,os.path.join(os.path.dirname(file_path),"encrypted_valid_password.csv"))





if __name__ == "__main__":
    encrypt_test_data_password()