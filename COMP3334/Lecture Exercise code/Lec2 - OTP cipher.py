# One time pad cipher
# encryption and decryption
def encrypt(plaintext, key):
    ciphertext = ""
    key_length = len(key)
    for i in range(len(plaintext)):
        char = plaintext[i]
        key_char = key[i % key_length]
        encrypted_char = chr((ord(char) + ord(key_char)) % 26 + ord('A'))
        ciphertext += encrypted_char
    return ciphertext

def decrypt(ciphertext, key):
    plaintext = ""
    key_length = len(key)
    for i in range(len(ciphertext)):
        char = ciphertext[i]
        key_char = key[i % key_length]
        decrypted_char = chr((ord(char) - ord(key_char)) % 26 + ord('A'))
        plaintext += decrypted_char
    return plaintext

# Example usage

plaintext = "HELLOWORLD"
key = "POLYUROCKS"
ciphertext = encrypt(plaintext, key)
decrypted_text = decrypt(ciphertext, key)

print("Plaintext:", plaintext)
print("Ciphertext:", ciphertext)
print("Decrypted text:", decrypted_text)


