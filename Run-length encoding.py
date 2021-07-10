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
    print(len(text))
    print(len(text) - 1)
    for i in range(len(text) - 1):
        if text[i] == text[i+1]:
            temp += 1
        else:
            ciphertext += str(temp)
            ciphertext += text[i]
            temp = 1
    return ciphertext

a = "AAAABBBCCDAA"
print(len(a))
print(encrypt(a))

