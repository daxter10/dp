def caesar_cipher_encrypt(text, shift):

    encrypted_text = []
    
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            base = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - base + shift_amount) % 26 + base)
            encrypted_text.append(new_char)
        else:
            encrypted_text.append(char)
    
    return ''.join(encrypted_text)

def caesar_cipher_decrypt(text, shift):
    
    return caesar_cipher_encrypt(text, -shift)

while True:
    print("Caesar Cipher")
    print()
    print('type 1 for exit')
    choice = input("Type 'e' to encrypt or 'd' to decrypt: ").strip().lower()
    
    if choice not in ['e', 'd','1']:
        print("Invalid choice. Please choose 'encrypt' or 'decrypt'.")
        
    
    text = input("Enter the text: ")
    shift = int(input("Enter the shift (integer): "))
    
    if choice == 'e':
        result = caesar_cipher_encrypt(text, shift)
        print("Encrypted text: ", result)
    elif choice == 'd':
        result = caesar_cipher_decrypt(text, shift)
        print("Decrypted text: ", result)

    elif choice =='1':
        break
