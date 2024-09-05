import os
from passpy import crypto
from .storage import initialize_db
initialize_db()

key_exists = os.path.exists(".env") and crypto.get_fernet_key()

if not key_exists:
    key = crypto.create_fernet_key()
    crypto.save_fernet_key(key)
