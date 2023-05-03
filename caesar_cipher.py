import sys

def caesar_cipher(shift_amount):
    message = input("Enter a message to encrypt: ").upper()
    encrypted_message = ""

    for char in message:
        if char.isalpha():
            char_code = ord(char) - 65
            encrypted_char_code = (char_code + shift_amount) % 26
            encrypted_char = chr(encrypted_char_code + 65)
            encrypted_message += encrypted_char
    return encrypted_message

if __name__ == "__main__":
    shift_amount = int(sys.argv[1])
    encrypted_message = caesar_cipher(shift_amount)
    for i in range(0, len(encrypted_message), 5):
        print(encrypted_message[i:i+5])
        if i % 50 == 45:
            print()

