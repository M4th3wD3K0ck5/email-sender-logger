from cryptography.fernet import Fernet

def encrypt_file(file_path, encryption_key):
    with open(file_path, 'rb') as file:
        data = file.read()

    cipher_suite = Fernet(encryption_key)
    encrypted_data = cipher_suite.encrypt(data)

    with open(file_path + '.enc', 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)

def decrypt_file(file_path, encryption_key):
    with open(file_path, 'rb') as encrypted_file:
        encrypted_data = encrypted_file.read()

    cipher_suite = Fernet(encryption_key)
    decrypted_data = cipher_suite.decrypt(encrypted_data)

    with open(file_path[:-4] + '_decrypted.txt', 'wb') as decrypted_file:
        decrypted_file.write(decrypted_data)

def main():
    file_path = input("Enter the path of the file to decrypt: ")
    encryption_key = input("Enter the encryption key: ")

    try:
        decrypt_file(file_path, encryption_key.encode())
        print("File decrypted successfully.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
