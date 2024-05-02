# Class exercise
# Encrypt the string “We love crypto at PolyU!” using the key “superlongkey”
# The output will not be printable in plain letters, encode it in hexadecimal
# The output should start with 0xB3

def initialize_state():
    state = bytearray(range(256))
    return state

def convert_key(key):
    return bytearray(key, 'utf-8')

def key_scheduling(state, key):
    key_length = len(key)
    j = 0

    for i in range(256):
        j = (j + state[i] + key[i % key_length]) % 256
        state[i], state[j] = state[j], state[i]

    return state

def generate_keystream(state):
    i = 0
    j = 0

    # iterate from 0 to 255
    while True:
        i = (i + 1) % 256
        j = (j + state[i]) % 256
        state[i], state[j] = state[j], state[i]
        yield state[(state[i] + state[j]) % 256]


def encrypt(plaintext, key):
    rc4_state = initialize_state()
    key = convert_key(key)
    rc4_state = key_scheduling(rc4_state, key)
    keystream = generate_keystream(rc4_state)

    ciphertext = bytearray()
    for char in plaintext.encode('utf-8'):
        keystream_byte = next(keystream)
        encrypted_byte = char ^ keystream_byte
        ciphertext.append(encrypted_byte)

    return "0x" + ciphertext.hex()

plaintext = "We love crypto at PolyU!"
key = "superlongkey"

encrypted_data = encrypt(plaintext, key)
print("Encrypted Data (Hex):", encrypted_data)