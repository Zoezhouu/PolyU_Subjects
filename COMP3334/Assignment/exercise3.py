def pkcs(plaintext, length):
    if length > 255:
        raise Exception("Invalid block size")
    
    pad_len = length - (len(plaintext) % length)
    padding = chr(pad_len) * pad_len
    pad_plaintext = plaintext + padding
    
    return pad_plaintext

def validate_pkcs(plaintext, length):
    if len(plaintext) == 0:
        raise Exception("Invalid padding: No plaintext input - length of plaintext is 0.")
    if len(plaintext) % length != 0:
        raise Exception("Invalid padding: no padding has been used in plaintext.")
    # print(len(plaintext))

    last_byte = plaintext[-1]
    # print(repr(last_byte))
    pad_length = ord(last_byte)
    # print(pad_length)

    if pad_length < 1:
        raise Exception("Invalid padding: The padding length is less than 1")
    if pad_length > length: 
        raise Exception("Invalid padding: The padding value is greater than the length of the plaintext")
    
    if plaintext[-pad_length:] != bytes([pad_length]) * pad_length:
        raise Exception("Invalid padding: padding is not last character")

    unpadded_plaintext = plaintext[:-pad_length]

    return unpadded_plaintext
    


def main():
    BLOCKSIZE = 20
    pad_text = pkcs("YELLOW SUBMARINE", BLOCKSIZE)
    # print(repr(pad_text))

    try:
        unpadded_text = validate_pkcs(pad_text, BLOCKSIZE)
        print(unpadded_text.decode())
    except Exception as e:
        print(str(e))
    

main()