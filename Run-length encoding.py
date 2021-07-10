#Difficulty: Easy
#Problem statement
"""
This problem was asked by Amazon.
Run-length encoding is a fast and simple method of encoding strings.
The basic idea is to represent repeated successive characters as a single count and character.
For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

Implement run-length encoding and decoding.
You can assume the string to be encoded have no digits and consists solely of alphabetic characters.
You can assume the string to be decoded is valid.
"""

#Solution

def encrypt(text):
    ciphertext = ''
    temp = 1

    for i in range(len(text)):
        if i+1 <= len(text)-1 and text[i] == text[i+1]: #count iteration of char
            temp += 1
        elif i < len(text)-1: #add string to ciphertext
            ciphertext += str(temp)
            ciphertext += text[i]
            temp = 1
        else: #for last char
            ciphertext += str(temp)
            ciphertext += text[i]

    return ciphertext

def decrypt(cipher):
    plaintext = ""
    for i in range(len(cipher) - 1):
        try:
            int(cipher[i])
            plaintext += int(cipher[i])*cipher[i+1]
        except ValueError:
            continue
    return plaintext

a = "AAAABBBCCDAA"
print("Plaintext: ", a)
print('Encrypted: ', encrypt(a))

a = encrypt(a)
print('Decrypted: ', decrypt(a))



