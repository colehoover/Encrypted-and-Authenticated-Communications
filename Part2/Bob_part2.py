# Cole Hoover
# HW3
# RSA encryption with 2048 bit key

from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

# Load private key from file
private_key = RSA.importKey(open('private_key.txt').read())

# Read ciphertext from file and print
with open('ctext.txt', 'rb') as cipher_file:
    ciphertext = cipher_file.read()
print("Received Ciphertext: ", ciphertext)

# Decrypt message
cipher = PKCS1_OAEP.new(private_key)
message = cipher.decrypt(ciphertext)
print('Message:', message.decode())
