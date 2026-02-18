from cryptography.fernet import Fernet
import os

KEY_FILE = "secret.key"

def generate_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as f:
        f.write(key)

def load_key():
    if not os.path.exists(KEY_FILE):
        generate_key()
    return open(KEY_FILE, "rb").read()

def encrypt_password(password):
    key = load_key()
    f = Fernet(key)
    return f.encrypt(password.encode()).decode()

def decrypt_password(encrypted_password):
    key = load_key()
    f = Fernet(key)
    return f.decrypt(encrypted_password.encode()).decode()
