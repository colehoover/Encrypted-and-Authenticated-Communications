# Cole Hoover
# HW3
# Authentication/integrity protection with HMAC and SHA-256

from Crypto.Hash import HMAC, SHA256

# Read the key from file
with open("key.txt", 'rb') as key_file:
    key = key_file.read()

# Read message and HMAC from file
with open("mactext.txt", 'rb') as mac_file:
    message = mac_file.readline()
    hmac = mac_file.readline()

# Strip the new line
message = message.strip("\n".encode())

# Generate the HMAC to verify
h = HMAC.new(key, message, digestmod=SHA256)

# Verify and print
try:
    h.hexverify(hmac.decode())
    print("The message '%s' is authentic" % message.decode())
except ValueError:
    print("The message or the key is wrong")