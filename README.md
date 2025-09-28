Task 1 – Caesar Cipher Algorithm

SkillCraft Technology – Cybersecurity Internship

# Example usage
if __name__ == "__main__":
    plaintext = "Hello SkillCraft"
    shift = 3

    print("Plaintext:", plaintext)
    encrypted = caesar_encrypt(plaintext, shift)
    print("Encrypted:", encrypted)

    decrypted = caesar_decrypt(encrypted, shift)
    print("Decrypted:", decrypted)


✅ Sample Output
Plaintext: Hello SkillCraft
Encrypted: Khoor VnlooFudiw
Decrypted: Hello SkillCraft

📖 Explanation

Encryption (Shift = 3):

H → K
e → h
l → o
Spaces/punctuation remain unchanged.

Decryption:

Simply shifts letters in the reverse direction to get back original plaintext.
🔐 Learning Outcome
Understood the concept of substitution ciphers.
Learned how character encoding (ord, chr) can be used for cryptography.
Implemented both encryption and decryption functions in Python.
