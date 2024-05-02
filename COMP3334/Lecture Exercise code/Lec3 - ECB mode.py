from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def encrypt_ecb(key, plaintext):
    cipher = AES.new(key, AES.MODE_ECB)
    padded_plaintext = pad(plaintext, AES.block_size)
    ciphertext = cipher.encrypt(padded_plaintext)
    return ciphertext

def decrypt_ecb(key, ciphertext):
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted_data = cipher.decrypt(ciphertext)
    plaintext = unpad(decrypted_data, AES.block_size)
    return plaintext

# Example usage
key = b'thisisa16bytekey'
plaintext = b'This is the plaintext message'

# Encryption
encrypted_data = encrypt_ecb(key, plaintext)
print("Encrypted data:", encrypted_data)

# Decryption
decrypted_data = decrypt_ecb(key, encrypted_data)
print("Decrypted data:", decrypted_data.decode())