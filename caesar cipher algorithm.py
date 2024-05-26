def caesar_cipher(text, shift, decrypt=False):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            shift_amount = shift if not decrypt else -shift
            shifted_char = chr((ord(char) - ord('a' if char.islower() else 'A') + shift_amount) % 26 + ord('a' if char.islower() else 'A'))
            encrypted_text += shifted_char
        else:
            encrypted_text += char
    return encrypted_text

def main():
    while True:
        choice = input("Do you want to encrypt or decrypt? (e/d): ").lower()
        if choice not in ['e', 'd']:
            print("Invalid choice. Please enter 'e' for encryption or 'd' for decryption.")
            continue
        break

    text = input("Enter the message: ")
    shift = int(input("Enter the shift value: "))

    if choice == 'e':
        encrypted_text = caesar_cipher(text, shift)
        print("Encrypted message:", encrypted_text)
    else:
        decrypted_text = caesar_cipher(text, shift, decrypt=True)
        print("Decrypted message:", decrypted_text)

if __name__ == "__main__":
    main()