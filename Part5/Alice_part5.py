# Cole Hoover
# HW3
# RSA digital signature with 2048 bit key

from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA

# Get message from command line
print("Enter your secret message: ")
message = input()

# Read Alice's private key
key = RSA.import_key(open("private_key.txt").read())

# Hash and sign the message
h = SHA256.new(message.encode())
signature = pkcs1_15.new(key).sign(h)
print("Signature: ", signature)

# Write message and signature to file
with open("sigtext.txt", "wb") as sig_file:
    sig_file.write(message.encode())
    sig_file.write("\n".encode())
    sig_file.write(signature.hex().encode())

