# Cole Hoover
# HW3
# Authentication/integrity protection with HMAC and SHA-256

from cryptography.fernet import Fernet
from Crypto.Hash import HMAC, SHA256

# Generate the 16-byte key and write to a file
key = Fernet.generate_key()
with open('key.txt', 'wb') as key_file:
    key_file.write(key)

# Read in message from command line
print("Enter your secret message: ")
message = input()

# Generate HMAC with key and SHA256
h = HMAC.new(key, message.encode(), digestmod=SHA256)

# Write message and HMAC to file
with open("mactext.txt", 'wb') as mac_file:
    mac_file.write(message.encode())
    mac_file.write("\n".encode())
    mac_file.write(h.hexdigest().encode())

print("HMAC: ", h.hexdigest())

