import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
# print(chars)
chars = list(chars) # converts the chars string to list
key = chars.copy()

random.shuffle(key)

# ENCRYPT
plain_text = input("Enter a message to Encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"Original message : {plain_text}")
print(f"Encrypted message: {cipher_text}")

# DECRYPT
cipher_text = input("Enter a message to Decrypt: ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"Encrypted message: {cipher_text}")
print(f"Original message : {plain_text}")
