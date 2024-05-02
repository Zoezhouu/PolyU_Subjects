from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives import hashes


def pad_data(data):
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(data)
    padded_data += padder.finalize()
    return padded_data


def unpad_data(padded_data):
    unpadder = padding.PKCS7(128).unpadder()
    data = unpadder.update(padded_data)
    data += unpadder.finalize()
    return data


def encrypt_CBC(plaintext, key, iv):
    backend = default_backend()
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
    encryptor = cipher.encryptor()
    encrypted_data = encryptor.update(pad_data(plaintext)) + encryptor.finalize()
    return encrypted_data


def decrypt_CBC(ciphertext, key, iv):
    backend = default_backend()
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(ciphertext) + decryptor.finalize()
    return unpad_data(decrypted_data)


# Example usage
key = b'0123456789abcdef'  # 128-bit key
iv = b'abcdefghijklmnop'  # 128-bit IV

plaintext = b'This is the plaintext message.'

# Encrypt the plaintext
ciphertext = encrypt_CBC(plaintext, key, iv)
print("Ciphertext:", ciphertext.hex())

# Decrypt the ciphertext
decrypted_text = decrypt_CBC(ciphertext, key, iv)
print("Decrypted text:", decrypted_text.decode())