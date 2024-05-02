import os
from binascii import hexlify,unhexlify
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

# generate a random 128-bit key from Python’s crypto PRNG
key = os.urandom(16)
print("k = %s" % hexlify(key))

# create an instance of AES-128 to encrypt a single block
cipher = Cipher(algorithms.AES(key), modes.ECB())
m = b"a secret message"
# The length of the provided data should be a multiple of the block length.

# encrypt message
encryptor = cipher.encryptor()
ct= encryptor.update(m) + encryptor.finalize()
print("enc(%s) = %s" % (hexlify(m), hexlify(ct)))

# decrypt message
decryptor= cipher.decryptor()
pt= decryptor.update(ct) + decryptor.finalize()
print("dec(%s) = %s" % (hexlify(ct), hexlify(pt)))