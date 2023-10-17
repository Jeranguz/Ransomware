from cryptography.fernet import Fernet
import os

def load_key():
    return open('key.key', 'rb').read()

def decrypt(folder_path, key):
    f = Fernet(key)
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'rb') as file:
                encrypted_data = file.read()
            decrypted_data = f.decrypt(encrypted_data)
            with open(file_path, 'wb') as file:
                file.write(decrypted_data)

if __name__ == '__main__':

    path_to_ecrypt = 'C:\\Users\\Jeremy\\Desktop\\Prueba ransonware'
    os.remove(path_to_ecrypt+'\\'+'readme.txt')

    key = load_key()
    decrypt(path_to_ecrypt, key)

