def caesarCipher(s, k):
    k = k % 26
    cipher = []
    
    for i in range(len(s)):
        if s[i].isalpha():
            if s[i].isupper():
                cipher.append(chr(ord('A') + (ord(s[i]) - ord('A') + k) % 26))
            else:
                cipher.append(chr(ord('a') + (ord(s[i]) - ord('a') + k) % 26))
        else:
            cipher.append(s[i])
    
    return ''.join(cipher)

def main():
    print("Welcome to the Caesar Cipher app!")
    
    while True:
        user_input = input("\nEnter the text to encrypt (or 'exit' to quit): ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        
        while True:
            try:
                shift = int(input("Enter the shift value (integer): "))
                break
            except ValueError:
                print("Invalid input. Please enter an integer for the shift value.")
        
        # Encrypt the input text
        encrypted_text = caesarCipher(user_input, shift)
        print(f"Encrypted text: {encrypted_text}")

if __name__ == "__main__":
    main()
