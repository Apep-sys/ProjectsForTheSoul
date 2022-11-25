"""Program pentru codificarea mesajelor utilizand Cifrul Cezar."""


def encrypt(message, shift):
    encrypted_message = ''
    upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z']
    lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for letter in message:
        if letter in upper:
            new_letter = ((upper.index(letter)) + shift) % 26
            encrypted_message += upper[new_letter]
        elif letter in lower:
            new_letter = ((lower.index(letter)) + shift) % 26
            encrypted_message += lower[new_letter]
    return encrypted_message


def decrypt(message, shift):
    decrypted_message = ''
    upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z']
    lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']
    for letter in message:
        if letter in upper:
            new_letter = ((upper.index(letter)) - shift) % 26
            decrypted_message += upper[new_letter]
        elif letter in lower:
            new_letter = ((lower.index(letter)) - shift) % 26
            decrypted_message += lower[new_letter]
    return decrypted_message


enc = input('Introduce the message you want to encrypt, but without any spaces: \n')
enc1 = encrypt(enc, 4)
print(enc1)
dec = input('Introduce the message you want to decrypt, but without any spaces: \n')
dec = decrypt(dec, 4)
print(dec)