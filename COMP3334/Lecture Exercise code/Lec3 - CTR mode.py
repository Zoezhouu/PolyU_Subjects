from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import counter

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

def encrypt_CTR(plaintext, key, nonce):
    backend = default_backend()
    ctr = counter.Counter(nonce)
    cipher = Cipher(algorithms.AES(key), modes.CTR(ctr), backend=backend)
    encryptor = cipher.encryptor()
    encrypted_data = encryptor.update(pad_data(plaintext)) + encryptor.finalize()
    return encrypted_data

def decrypt_CTR(ciphertext, key, nonce):
    backend = default_backend()
    ctr = counter.Counter(nonce)
    cipher = Cipher(algorithms.AES(key), modes.CTR(ctr), backend=backend)
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(ciphertext) + decryptor.finalize()
    return unpad_data(decrypted_data)

# Example usage
key = b'0123456789abcdef'  # 128-bit key
nonce = b'1234567890abcdef'  # 128-bit nonce
plaintext = b'This is the plaintext message.'

# Encrypt the plaintext
ciphertext = encrypt_CTR(plaintext, key, nonce)
print("Ciphertext:", ciphertext.hex())

# Decrypt the ciphertext
decrypted_text = decrypt_CTR(ciphertext, key, nonce)
print("Decrypted text:", decrypted_text.decode())