import hashlib
# import random
from cryptography.fernet import Fernet

# def create_iv(length):
#   """Creates a random initialization vector of the specified length."""
#   return random.randint(0, 2**length - 1)


message = b'My secret message.'

print("Original Data:", message.decode())

# Encrypt with Fernet
key = Fernet.generate_key()
cipher = Fernet(key)
# iv = str(create_iv(16)) not required since encrypt() has it

# Hash with SHA-256
sha256_hash = hashlib.sha256(message).hexdigest() 

encrypted_data = cipher.encrypt(sha256_hash.encode())

# Decrypt the message
decrypted_data = cipher.decrypt(encrypted_data)

# Print the results
# print("Original Data:", message)
print("SHA-256 Hash:", sha256_hash)
print("Encrypted Data:", encrypted_data)
print("Decrypted Data:", decrypted_data.decode())
