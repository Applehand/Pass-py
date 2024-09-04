from cryptography.fernet import Fernet
import os
from dotenv import load_dotenv
load_dotenv()

def create_fernet_key() -> bytes:
    return Fernet.generate_key()

def save_fernet_key(key: bytes):
    key_str = key.decode()

    if not os.path.exists(".env"):
        with open(".env", "w") as env_file:
            env_file.write(f"FERNET_KEY={key_str}\n")
            print("FERNET_KEY added to new .env file.")
    else:
        with open(".env", "r") as env_file:
            lines = env_file.readlines()
        
        key_exists = any(line.startswith("FERNET_KEY=") for line in lines)
        
        if not key_exists:
            with open(".env", "a") as env_file:
                env_file.write(f"FERNET_KEY={key_str}\n")
            print("FERNET_KEY added to existing .env file.")
        else:
            print("FERNET_KEY already exists in an .env file.")

def get_fernet_key() -> bytes:
    if not os.path.exists(".env"):
        raise FileNotFoundError( ".env file does not exist.")
    
    with open(".env", "r") as env_file:
        lines = env_file.readlines()
    
    for line in lines:
        if line.startswith("FERNET_KEY="):
            key_str = line.strip().split("=", 1)[1]
            return key_str.encode()
    
    raise ValueError("FERNET_KEY not found in the .env file.")

def encrypt_password(password: str, key: bytes) -> bytes:
    cipher_suite = Fernet(key)
    encrypted_password = cipher_suite.encrypt(password.encode())

    return encrypted_password

def decrypt_password(encrypted_password: bytes, key: bytes) -> str:
    cipher_suite = Fernet(key)
    decrypted_password = cipher_suite.decrypt(encrypted_password)

    return decrypted_password.decode()
