from cryptography.fernet import Fernet
import hashlib


data = b'your_data_to_hash'
sha256_hash = hashlib.sha256(data).hexdigest()

# Generate a key
key = Fernet.generate_key()

# Create a Fernet cipher with the key
f_chiper = Fernet(key)

# Encrypt the SHA-256 hash
# chiper_msg = f_chiper.encrypt(b"my deep dark secret")
encrypted_token = f_chiper.encrypt(sha256_hash.encode())

print(encrypted_token)
# b'gAAAAABlZIzeo68hJtG-CrHGpXFxx7jNHKWWWrY3TC9oJVRKsl55N12SQt20l9JQ00BE6XATwNGPm_pIInAcoQIV3UeumBn2IbkJ6PhoncVrfINeTmK3HTg='

decryped_token = f_chiper.decrypt(encrypted_token)
print(decryped_token)
# b'my deep dark secret'

# Decrypt the data
decrypted_data = f_chiper.decrypt(encrypted_token)

# Verify the hash
if decrypted_data.decode() == sha256_hash:
    print("Hash verified.")
else:
    print("Hash verification failed.")
