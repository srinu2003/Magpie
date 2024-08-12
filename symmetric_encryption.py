from __future__ import annotations
from os import getcwd
from os.path import isfile
from cryptography.fernet import Fernet
from cryptography.fernet import InvalidToken
from binascii import Error as BinasciiError


class KeyNotFoundError(FileNotFoundError):
    """Raised when the key file is not found in the current directory."""
    def __init__(self, *args: object) -> None:
        super().__init__(f'''No key found in Dir: '{args[0]}'
New Key file should be generated at same location.''')

    def __str__(self) -> str:
        return super().__str__()


def generate_key() -> bytes:
    """
    Generates a symmetric encryption key and saves it to a file named 'key.key'.

    Returns:
        bytes: The generated encryption key.
    """
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)

    return load_key()


def load_key() -> bytes:
    """
    Load the encryption key from a file.

    If the key file does not exist, a new key will be generated.

    Returns:
        bytes: The encryption key.
    """
    try:
        if not isfile('./key.key'):
            current_dir = getcwd()
            raise KeyNotFoundError(current_dir)
    except KeyNotFoundError:
        return generate_key()
        # raise KeyNotFoundError(getcwd())

    with open('key.key', 'rb') as key_file:
        key = key_file.read()
    return key


# f = Fernet(generate_key())

def encrypt_message(message: str, key: bytes) -> str:
    """
    Encrypts a message using symmetric encryption.

    Args:
        message (str): The message to be encrypted.
        key (bytes): The encryption key.

    Returns:
        str: The encrypted message.

    """
    f: Fernet = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    return encrypted_message.decode()


def decrypt_message(encrypted_message: str, key: bytes) -> str | type[InvalidToken] | Exception | type[BinasciiError]:
    """
    Decrypts an encrypted message using the provided key.

    Args:
        encrypted_message (str): The encrypted message to be decrypted.
        key (bytes): The key used for decryption.

    Returns:
        str: The decrypted message.     

    Raises:
        InvalidToken: If the provided key is invalid.
        BinasciiError: If there is an error with the encrypted message.
        Exception: If any other exception occurs during decryption.
    """
    f: Fernet = Fernet(key)
    try:
        decrypted_message = f.decrypt(encrypted_message.encode())
    except InvalidToken:
        return InvalidToken
    except BinasciiError:
        return BinasciiError
    except Exception as e:
        return e

    return decrypted_message.decode()

# print(decrypt_message(encrypt_message('hi',load_key()),load_key()))
# print(decrypt_message('',load_key()))
