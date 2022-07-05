# Cole Hoover
# HW3
# Testing AES and RSA encryption and decryption
import timeit
from cryptography.fernet import Fernet
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Read in message from command line
print("Enter your message: ")
message = input()

# AES Encryption
# Generate AES key
key = Fernet.generate_key()
# Instantiate a Fernet object with key.
f = Fernet(key)
AES_ciphertext = ""

# Get start time
start_AES_enc = timeit.default_timer()

# Encrypt 100 times
for i in range(100):
    # Encrypt message
    AES_ciphertext = f.encrypt(message.encode())

# Get end time
end_AES_enc = timeit.default_timer()

# Compute total time of 100 encryptions
total_time_AES_enc = end_AES_enc - start_AES_enc

# Compute average time for one encryption
avg_time_AES_enc = total_time_AES_enc / 100
print("Average time for one AES encryption: ", avg_time_AES_enc, "seconds")

# AES Decryption
# Get start time
start_AES_dec = timeit.default_timer()

# Decrypt 100 times
for i in range(100):
    # Decrypt message
    AES_dec_message = f.decrypt(AES_ciphertext)

# Get end time
end_AES_dec = timeit.default_timer()

# Compute total time of 100 decryptions
total_time_AES_dec = end_AES_dec - start_AES_dec

# Compute average time for one decryption
avg_time_AES_dec = total_time_AES_dec / 100
print("Average time for one AES decryption: ", avg_time_AES_dec, "seconds")

# RSA Encryption
# Get key pair
public_key = RSA.importKey(open('public_key.txt').read())
private_key = RSA.importKey(open("private_key.txt").read())
RSA_ciphertext = ""

# Get start time
start_RSA_enc = timeit.default_timer()

# Encrypt 100 times
for i in range(100):
    # Encrypt the message with the public RSA key
    rsa = PKCS1_OAEP.new(public_key)
    RSA_ciphertext = rsa.encrypt(message.encode())

# Get end time
end_RSA_enc = timeit.default_timer()

# Compute total time of 100 encryptions
total_time_RSA_enc = end_RSA_enc - start_RSA_enc

# Compute average time for one encryption
avg_time_RSA_enc = total_time_RSA_enc / 100
print("Average time for one RSA encryption: ", avg_time_RSA_enc, "seconds")

# RSA Decryption
# Get start time
start_RSA_dec = timeit.default_timer()

# Decrypt 100 times
for i in range(100):
    # Decrypt message with private key
    cipher = PKCS1_OAEP.new(private_key)
    RSA_dec_message = cipher.decrypt(RSA_ciphertext)

# Get end time
end_RSA_dec = timeit.default_timer()

# Compute total time of 100 decryptions
total_time_RSA_dec = end_RSA_dec - start_RSA_dec

# Compute average time for one decryption
avg_time_RSA_dec = total_time_RSA_dec / 100
print("Average time for one RSA decryption: ", avg_time_RSA_dec, "seconds")
