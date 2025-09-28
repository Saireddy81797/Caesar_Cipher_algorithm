def caesar_cipher_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():  # Check if character is a letter
            # Handle uppercase and lowercase separately
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char  # Keep numbers, spaces, symbols unchanged
    return result


def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)  # Just reverse shift


# --- Main Program ---
message = input("Enter your message: ")
shift = int(input("Enter shift value: "))

encrypted = caesar_cipher_encrypt(message, shift)
decrypted = caesar_cipher_decrypt(encrypted, shift)

print("\nEncrypted Message:", encrypted)
print("Decrypted Message:", decrypted)
