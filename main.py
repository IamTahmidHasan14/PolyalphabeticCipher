def encrypt(plaintext, key):
    c_text = ""
    key_len = len(key)
    for i, c in enumerate(plaintext):
        if c.isalpha():
            s = ord(key[i % key_len].lower()) - 97
            if c.isupper():
                encrypted_char = chr((ord(c) - 65 + s) % 26 + 65)
            else:
                encrypted_char = chr((ord(c) - 97 + s) % 26 + 97)
            c_text = c_text + encrypted_char
        else:
            c_text = c_text+ c
    print("Encrypted text:", c_text)
    return c_text

def decrypt(c_text, key):
    plaintext = ""
    key_len = len(key)
    for i, c in enumerate(c_text):
        if c.isalpha():
            s = ord(key[i % key_len].lower()) - 97
            if c.isupper():
                decrypted_char = chr((ord(c) - 65 - s) % 26 + 65)
            else:
                decrypted_char = chr((ord(c) - 97 - s) % 26 + 97)
            plaintext = plaintext + decrypted_char
        else:
            plaintext = plaintext + c
    print("Decrypted text:", plaintext)

plaintext = "Tahmid Hasan"
print("Plain Text:", plaintext)
key = "code"

encrypted_text = encrypt(plaintext, key)
decrypted_text = decrypt(encrypted_text, key)