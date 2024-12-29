# Function to encrypt text using Caesar Cipher
def encrypt(plain_text, shift):
    encrypted_text = ""
    for char in plain_text:
        if char.isalpha():
            # Handle uppercase letters
            shift_base = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            # Non-alphabetic characters are added unchanged
            encrypted_text += char
    return encrypted_text

# Function to decrypt text using Caesar Cipher
def decrypt(encrypted_text, shift):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            # Handle uppercase letters
            shift_base = 65 if char.isupper() else 97
            decrypted_text += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            # Non-alphabetic characters are added unchanged
            decrypted_text += char
    return decrypted_text

# Main function to interact with the user
def main():
    print("Caesar Cipher Encryption/Decryption")
    action = input("Would you like to Encrypt or Decrypt a message? (E/D): ").upper()
    
    if action not in ['E', 'D']:
        print("Invalid choice. Please choose either 'E' for Encrypt or 'D' for Decrypt.")
        return
    
    message = input("Enter the message: ")
    shift = int(input("Enter the shift value: "))
    
    if action == 'E':
        encrypted_message = encrypt(message, shift)
        print(f"Encrypted message: {encrypted_message}")
    elif action == 'D':
        decrypted_message = decrypt(message, shift)
        print(f"Decrypted message: {decrypted_message}")

if __name__ == "__main__":
    main()
