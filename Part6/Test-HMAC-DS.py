# Cole Hoover
# HW3
# Testing both HMAC authentication/integrity protection
# and RSA digital signature
import timeit
from cryptography.fernet import Fernet
from Crypto.Hash import HMAC, SHA256
from Crypto.Signature import pkcs1_15
from Crypto.PublicKey import RSA

# Read in message from command line
print("Enter your message: ")
message = input()

# HMAC Generation
# Generate 16 byte key
key = Fernet.generate_key()

# Get start time
start_HMAC = timeit.default_timer()

# Generate HMAC 100 times
for i in range(100):
    # Generate HMAC with key and SHA256
    h = HMAC.new(key, message.encode(), digestmod=SHA256)

# Get end time
end_HMAC = timeit.default_timer()

# Compute total time of HMAC generation
total_time_HMAC = end_HMAC - start_HMAC

# Compute average time of 1 HMAC generation
avg_time_HMAC = total_time_HMAC / 100
print("Average time of one HMAC generation: ", avg_time_HMAC, "seconds")

# RSA Digital Signature Generation
# Get private key
private_key = RSA.import_key(open("private_key.txt").read())

# Hash the message
h = SHA256.new(message.encode())

# Get start time
start_sign = timeit.default_timer()
signature = ''

# Sign 100 times
for i in range(100):
    # Sign the hash
    signature = pkcs1_15.new(private_key).sign(h)


# Get end time
end_sign = timeit.default_timer()

# Compute total time to sign
total_time_sign = end_sign - start_sign

# Compute average time for one digital signature
avg_time_sign = total_time_sign / 100
print("Average time for one signature generation: ", avg_time_sign, "seconds")

# RSA Digital Signature verification
# Get public key
public_key = RSA.import_key(open('public_key.txt').read())

# Compute the hash
h = SHA256.new(message.encode())

# Set the signature verification method
verifier = pkcs1_15.new(public_key)

# Get start time
start_verify = timeit.default_timer()

# Verify 100 times
for i in range(100):
    # Verify
    verifier.verify(h, signature)

# Get end time
end_verify = timeit.default_timer()

# Compute total time
total_time_verify = end_verify - start_verify

# Compute average time of one verification
avg_time_verify = total_time_verify / 100
print("Average time for one signature verification:", avg_time_verify, "seconds")
