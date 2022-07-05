# Encrypted-and-Authenticated-Communications
I implemented encrypted communications between two parties, Alice and Bob, and evaluated the performance of AES and RSA. I also implemented authenticated communications between them, and evaluated the performance of HMAC and RSA digital signature. For simplicity, Alice and Bob were simulated by two programs running on the same computer. When Alice sends a message to Bob, she writes the message to a file. Bob receives the message through reading from the file.

# Part 1
Part 1 implements encryption and decryption using AES in CBC mode with a 128-bit key. When the Alice program is run, the key is generated and written to a file, a message is input from the command line and the generated ciphertext is written to a file. When the Bob program is run, the key and ciphertext are read from their respective files and the message is decrypted.

# Part 2
Part 2 implements encryption and decryption using RSA with 2048-bit key. Running the generate key program will generate the RSA key pair and write them to files. Running the Alice program will get a message from the command line, read the public key, encrypt the message and write the ciphertext to a file. Running the Bob program will read the private key and ciphertext from the files and decrypt the message. 

# Part 3
Part 3 measures the performance of AES and RSA encryption and decryption. Running the generate key program will generate the RSA key pair. Running the test program encrpyts and decrypts a message 100 times using both AES and RSA and measures the average time for one encryption and decryption.

# Part 4 
Part 4 implements authentication and integrity protection using HMAC with SHA-256 as the underlying hash algorithm. Running the Alice program generates a 16-bit key and writes it to a file, reads a message from the command line, generates the HMAC, and writes it and the message to a file. Running the Bob program reads the key, HMAC, and message from a file, and verifies the HMAC.

# Part 5 
Part 5 implements digital signature using RSA with 2048-bit key. Running the generate key program generates the RSA key pair. Running the Alice program reads a message from the command line, reads the private key, hashes and signs the message, and writes the message and signature to a file. Running the Bob program reads the message and signature from the file, reads the public key, and verifys the signature. 

# Part 6
Part 6 measures the performance of HMAC and RSA digital signature. Running the generate key program generates the RSA key pair. Running the test program generates an HMAC, a digital signature, and verifies a digital signature 100 times and measures the average time for each. 
