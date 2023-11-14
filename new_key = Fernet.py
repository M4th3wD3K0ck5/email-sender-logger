from cryptography.fernet import Fernet

#generate key
new_key = Fernet.generate_key()
print("Generated Key:", new_key.decode())


# Write the key to a file
with open("key.txt", "w") as key_file:
    key_file.write(new_key.decode())