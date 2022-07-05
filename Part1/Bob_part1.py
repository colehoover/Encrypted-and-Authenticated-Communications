# Cole Hoover
# HW3
# AES encryption in CBC mode with 128 bit key

# Import Fernet
from cryptography.fernet import Fernet

# Load the key from file.
with open('key.txt', 'rb') as key_file:
    key = key_file.read()

# Read ciphertext from file and print
with open('ctext.txt', 'rb') as cipher_file:
    ciphertext = cipher_file.read()
print("Received Ciphertext: ", ciphertext)

# Instantiate Fernet object with key
f = Fernet(key)

# Decrypt message and print
message = f.decrypt(ciphertext)
print("Message: ", message.decode())
