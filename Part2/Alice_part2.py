# Cole Hoover
# HW3
# RSA encryption with 2048 bit key

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Get message from command line and encode
print("Enter your secret message:")
message = input()

# Get public key
public_key = RSA.importKey(open('public_key.txt').read())

# Encrypt the message with the public RSA key
rsa = PKCS1_OAEP.new(public_key)
ciphertext = rsa.encrypt(message.encode())

# Write ciphertext to file and print
with open('ctext.txt', 'wb') as cipher_file:
    cipher_file.write(ciphertext)
print("Sent Ciphertext: ", ciphertext)

