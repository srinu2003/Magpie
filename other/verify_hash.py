from cryptography.fernet import Fernet
import hashlib


data = b'your_data_to_hash'
sha256_hash = hashlib.sha256(data).hexdigest()

# Generate a key
key = Fernet.generate_key()

# Create a Fernet cipher with the key
f_cipher = Fernet(key)

# Encrypt the SHA-256 hash
# chipper_msg = f_cipher.encrypt(b"my deep dark secret")
encrypted_token = f_cipher.encrypt(sha256_hash.encode())

print(encrypted_token)

decrypted_token = f_cipher.decrypt(encrypted_token)
print(decrypted_token)
# b"my deep dark secret"

# Decrypt the data
decrypted_data = f_cipher.decrypt(encrypted_token)

# Verify the hash
if decrypted_data.decode() == sha256_hash:
    print("Hash verified.")
else:
    print("Hash verification failed.")
