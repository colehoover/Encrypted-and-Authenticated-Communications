# Cole Hoover
# HW3
# AES encryption in CBC mode with 128 bit key

# Import the Fernet class
# Fernet uses AES with 128-bit key in CBC mode
from cryptography.fernet import Fernet


# Generate the key and write to a file
key = Fernet.generate_key()
with open('key.txt', 'wb') as key_file:
    key_file.write(key)

# Get message from command line
print("Enter your secret message: ")
message = input()

# Instantiate a Fernet object with key.
f = Fernet(key)

# Encrypt message
ciphertext = f.encrypt(message.encode())

# Write ciphertext to file and print
with open('ctext.txt', 'wb') as cipher_file:
    cipher_file.write(ciphertext)
print("Sent Ciphertext: ", ciphertext.decode())
