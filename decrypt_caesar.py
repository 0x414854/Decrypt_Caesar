"""
This script decrypts a text encrypted using the Caesar Cipher by trying all possible keys (1-25). 
It reads the encrypted text from a file specified by the user and attempts to decrypt it with each key, printing the results.
"""

def decrypt_caesar(ciphertext):
    for key in range(1, 26):
        plain_text = ""
        for char in ciphertext:
            if char.isalpha():
                shift = ord(char) - key
                if char.isupper():
                    if shift < ord('A'):
                        shift += 26
                else:
                    if shift < ord('a'):
                        shift += 26
                plain_text += chr(shift)
            else:
                plain_text += char
        print(f"Key : {key} Deciphered Text : {plain_text}")
        
    print()


def main():
    file_path = input("Enter the file path of the ciphered text : ")
    with open(file_path, 'r') as file:
        ciphertext = file.read()
    decrypt_caesar(ciphertext)


if __name__ == "__main__":
    main()
