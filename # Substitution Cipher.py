# Caesar Cipher
def substitution_cipher(plaintext, key):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            shift = ord(char) + key
            if char.isupper():
                if shift > ord('Z'):
                    shift -= 26
                final_char = chr(shift)
            else:
                if shift > ord('z'):
                    shift -= 26
                final_char = chr(shift)
            ciphertext += final_char
        else:
            ciphertext += char
    return ciphertext

# Columnar Transposition
def transposition_cipher(ciphertext, key):
    num_of_columns = len(key)
    num_of_rows = len(ciphertext) // num_of_columns
    if len(ciphertext) % num_of_columns != 0:
        num_of_rows += 1
    plaintext = [''] * num_of_columns
    col = 0
    row = 0
    for char in ciphertext:
        plaintext[col] += char
        col += 1
        if (col == num_of_columns) or (col == num_of_columns - 1 and row >= num_of_rows):
            col = 0
            row += 1
    return ''.join(plaintext)

# Product Cipher
def product_cipher(plaintext, key1, key2):
    ciphertext = substitution_cipher(plaintext, key1)
    plaintext = transposition_cipher(ciphertext, key2)
    return plaintext

# Example usage
plaintext = "MYCITY MUMBAI"
key1 = 3
key2 = "abc"
ciphertext = product_cipher(plaintext, key1, key2)
print(ciphertext)