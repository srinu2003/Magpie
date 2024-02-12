from os import getcwd
from os.path import isfile
from cryptography.fernet import Fernet

class KeyNotFoundError(FileNotFoundError):
    def __init__(self, *args: object) -> None:
        super().__init__(f'''No key found in Dir: '{args[0]}'
New Key file generated at same location.''')

    def __str__(self) -> str:
        return super().__str__()
    

def generate_key() -> bytes:
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)

    return load_key()

def load_key() -> bytes:
    try:
        if(not isfile('./key.key')):
            current_dir = getcwd()
            raise KeyNotFoundError((current_dir))
    except KeyNotFoundError:
        return generate_key()
        # raise KeyNotFoundError(getcwd())
    
    with open('key.key', 'rb') as key_file:
        key = key_file.read()
    return key

# f = Fernet(generate_key())

def encrypt_message(message: str, key: bytes) -> str:
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    return encrypted_message.decode()

def decrypt_message(encrypted_message: str, key: bytes) -> str:
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message)
    return decrypted_message.decode()

# print(decrypt_message(encrypt_message('Hello',generate_key()),load_key()))
# print(encrypt_message('Hello',generate_key()))