# Fix this encryption function, it does not encrypt correctly!
def encrypt(letter):
    return chr(ord(letter)+3)
# Add a decription function!
def decrypt(letter):
    return chr(ord(letter)-3) #fix here

print(''.join([encrypt(l) for l in list("HELLO")]))
print(''.join([decrypt(l) for l in list("KHOOR")]))
