import os
import secrets

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

def encrypt_data(data, key):
    cipher = AES.new(key, AES.MODE_CBC)
    encrypted_data = cipher.encrypt(pad(data.encode(), AES.block_size))
    iv = base64.b64encode(cipher.iv).decode('utf-8')
    ciphertext = base64.b64encode(encrypted_data).decode('utf-8')
    return iv + ciphertext


def decrypt_data(encrypted_data, key):
    iv = base64.b64decode(encrypted_data[:24])
    ciphertext = base64.b64decode(encrypted_data[24:])
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return decrypted_data.decode('utf-8')


class InterfaceCyberSecurityEncoder:
    def encode(self, text):
        key = os.urandom(32)
        return encrypt_data(text, key), key


if __name__ == '__main__':
    enc, key = InterfaceCyberSecurityEncoder().encode('Привет у меня сломался роутер')
    print(enc, key)
    decrypted_data = decrypt_data(enc, key)

    print("Декодированные данные:", decrypted_data)