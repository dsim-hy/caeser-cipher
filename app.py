def caesarCipher(s, k, decrypt=False):
    """
    Encrypt or decrypt text using Caesar cipher.
    
    Args:
        s: Input string
        k: Shift value
        decrypt: If True, decrypt the text (shift backwards)
    
    Returns:
        Encrypted or decrypted string
    """
    if decrypt:
        k = -k
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

def rot13(s):
    """Apply ROT13 cipher (Caesar cipher with shift of 13)."""
    return caesarCipher(s, 13)

def atbashCipher(s):
    """
    Apply Atbash cipher (reverse alphabet substitution).
    A↔Z, B↔Y, C↔X, etc.
    """
    result = []
    for char in s:
        if char.isalpha():
            if char.isupper():
                result.append(chr(ord('Z') - (ord(char) - ord('A'))))
            else:
                result.append(chr(ord('z') - (ord(char) - ord('a'))))
        else:
            result.append(char)
    return ''.join(result)

def frequencyAnalysis(text):
    """
    Perform frequency analysis on the text.
    Returns a dictionary with letter frequencies.
    """
    freq = {}
    total = 0
    
    for char in text:
        if char.isalpha():
            char = char.lower()
            freq[char] = freq.get(char, 0) + 1
            total += 1
    
    # Convert to percentages and sort
    if total > 0:
        freq_percent = {k: (v / total * 100) for k, v in freq.items()}
        return dict(sorted(freq_percent.items(), key=lambda x: x[1], reverse=True))
    return {}

def bruteForce(encrypted_text):
    """
    Try all possible Caesar cipher shifts (1-25).
    Returns a list of all possible decryptions.
    """
    results = []
    for shift in range(1, 26):
        decrypted = caesarCipher(encrypted_text, shift, decrypt=True)
        results.append((shift, decrypted))
    return results

def main():
    print("=" * 50)
    print("Welcome to the Advanced Caesar Cipher App!")
    print("=" * 50)
    
    while True:
        print("\nChoose an option:")
        print("1. Caesar Cipher (Encrypt)")
        print("2. Caesar Cipher (Decrypt)")
        print("3. ROT13")
        print("4. Atbash Cipher")
        print("5. Frequency Analysis")
        print("6. Brute Force (try all shifts)")
        print("7. Exit")
        
        choice = input("\nEnter your choice (1-7): ").strip()
        
        if choice == '7':
            print("Goodbye!")
            break
        
        if choice not in ['1', '2', '3', '4', '5', '6']:
            print("Invalid choice. Please enter a number between 1 and 7.")
            continue
        
        user_input = input("Enter the text: ").strip()
        
        if choice == '1':
            # Caesar Cipher Encrypt
            while True:
                try:
                    shift = int(input("Enter the shift value (integer): "))
                    break
                except ValueError:
                    print("Invalid input. Please enter an integer for the shift value.")
            encrypted_text = caesarCipher(user_input, shift)
            print(f"\n✓ Encrypted text: {encrypted_text}")
        
        elif choice == '2':
            # Caesar Cipher Decrypt
            while True:
                try:
                    shift = int(input("Enter the shift value (integer): "))
                    break
                except ValueError:
                    print("Invalid input. Please enter an integer for the shift value.")
            decrypted_text = caesarCipher(user_input, shift, decrypt=True)
            print(f"\n✓ Decrypted text: {decrypted_text}")
        
        elif choice == '3':
            # ROT13
            result = rot13(user_input)
            print(f"\n✓ ROT13 result: {result}")
        
        elif choice == '4':
            # Atbash Cipher
            result = atbashCipher(user_input)
            print(f"\n✓ Atbash result: {result}")
        
        elif choice == '5':
            # Frequency Analysis
            freq = frequencyAnalysis(user_input)
            if freq:
                print("\n✓ Letter frequency analysis (sorted by frequency):")
                for letter, percentage in freq.items():
                    bar = '█' * int(percentage / 2)
                    print(f"  {letter}: {percentage:5.2f}% {bar}")
            else:
                print("\n✗ No alphabetic characters found in the text.")
        
        elif choice == '6':
            # Brute Force
            print("\n✓ Trying all possible Caesar cipher shifts:")
            results = bruteForce(user_input)
            for shift, decrypted in results:
                print(f"  Shift {shift:2d}: {decrypted}")
            print("\nHint: Look for readable English text in the results above.")

if __name__ == "__main__":
    main()
