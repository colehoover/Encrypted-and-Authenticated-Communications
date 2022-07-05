# Cole Hoover
# HW3
# RSA digital signature with 2048 bit key

from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA

# Read message and signature from file
with open("sigtext.txt", 'rb') as sig_file:
    message = sig_file.readline()
    signature = sig_file.readline()

# Fix signature type
signature = signature.fromhex(signature.decode())

# Strip the message
message = message.strip("\n".encode())

# Get Alice's public key
key = RSA.import_key(open('public_key.txt').read())

# Compute the hash
h = SHA256.new(message)
# Set the signature verification method
verifier = pkcs1_15.new(key)

# Verify and print
try:
    verifier.verify(h, signature)
    print("The signature is valid.")
except (ValueError, TypeError):
    print("The signature is not valid.")