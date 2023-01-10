def cezar_cipher(plaintext, key):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            shift = ord(char) + key
            if char.isupper():
                if shift > ord('Z'):
                    shift -= 26
                final_char = chr(shift)
            elif char.islower():
                if shift > ord('z'):
                    shift -= 26
                final_char = chr(shift)
            ciphertext += final_char
        else:
            ciphertext += char
    return ciphertext

def cezar_decipher(ciphertext, key):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            shift = ord(char) - key
            if char.isupper():
                if shift < ord('A'):
                    shift += 26
                final_char = chr(shift)
            elif char.islower():
                if shift < ord('a'):
                    shift += 26
                final_char = chr(shift)
            plaintext += final_char
        else:
            plaintext += char
    return plaintext


print("Welcome to the Caesar Cipher program.")
while True:
    operation = input("Do you want to encrypt or decrypt a message? (e/d)")
    if operation == "e":
        plaintext = input("Enter the message to encrypt: ")
        key = int(input("Enter the key (number of letters to shift): "))
        ciphertext = cezar_cipher(plaintext, key)
        print("Encrypted message:", ciphertext)
    elif operation == "d":
        ciphertext = input("Enter the message to decrypt: ")
        key = int(input("Enter the key (number of letters to shift): "))
        plaintext = cezar_decipher(ciphertext, key)
        print("Decrypted message:", plaintext)
    else:
        print("Invalid operation. Please enter 'e' for encryption or 'd' for decryption.")
    continue_program = input("Do you want to continue using the program? (y/n)")
    if continue_program == "n":
        break
    elif continue_program == "y":
        continue
    else:
        print("Invalid input. Exiting program.")
        break
