from Crypto.PublicKey import RSA

# Generate Alice's key pair
key_pair = RSA.generate(2048)
public_key = key_pair.publickey().export_key()
with open("public_key.txt", "wb") as public_key_file:
    public_key_file.write(public_key)
private_key = key_pair.exportKey()
with open("private_key.txt", 'wb') as private_key_file:
    private_key_file.write(private_key)