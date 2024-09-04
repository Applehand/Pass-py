import os
from passpy import crypto

key_exists = os.path.exists(".env") and crypto.get_fernet_key()

if not key_exists:
    key = crypto.create_fernet_key()
    crypto.save_fernet_key(key)
    print("Fernet key generated and saved.")
else:
    print("Fernet key already exists.")
