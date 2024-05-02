# Fix this encryption function, it does not encrypt correctly!
def encrypt(letter):
    return chr((ord(letter) - ord('A') +3) % 26 + ord('A'))
# Add a decription function!
def decrypt(letter):
    return chr((ord(letter)- ord('A') -3) % 26 + ord('A')) #fix here

print(''.join([encrypt(l) for l in list("HELLO")]))
print(''.join([decrypt(l) for l in list("KHOOR")]))
