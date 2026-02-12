# Advanced Caesar Cipher Script

This project is an advanced implementation of classical substitution ciphers, including Caesar Cipher, ROT13, and Atbash cipher. It also includes cryptanalysis tools like frequency analysis and brute force decryption.

## Features

### Cipher Operations
- **Caesar Cipher (Encrypt/Decrypt)**: Shifts letters by a specified number of positions in the alphabet
- **ROT13**: Special case of Caesar cipher with a fixed shift of 13
- **Atbash Cipher**: Reverse alphabet substitution (A↔Z, B↔Y, etc.)

### Cryptanalysis Tools
- **Frequency Analysis**: Analyzes letter frequency distribution in text with visual bar charts
- **Brute Force**: Tries all 25 possible Caesar cipher shifts to decrypt text

### General Features
- Maintains the case of the original text (upper or lower case)
- Preserves non-alphabetical characters unchanged
- Interactive command-line interface with menu-driven navigation
- Visual feedback with symbols and formatting

## Prerequisites

- **Python** (version 3.8 or above)

## How to Run

1. Clone or download this repository to your local machine.
2. Open a terminal and navigate to the directory containing the script.
3. Run the script with the following command:
   ```bash
   python app.py
   ```

## Usage

The application presents an interactive menu with the following options:

1. **Caesar Cipher (Encrypt)**: Encrypt text with a custom shift value
2. **Caesar Cipher (Decrypt)**: Decrypt text with a known shift value
3. **ROT13**: Apply ROT13 encoding/decoding
4. **Atbash Cipher**: Apply Atbash substitution cipher
5. **Frequency Analysis**: Analyze letter frequency distribution
6. **Brute Force**: Try all possible Caesar cipher shifts
7. **Exit**: Close the application

### Examples

#### Caesar Cipher Encryption
```bash
Choose an option:
1. Caesar Cipher (Encrypt)
2. Caesar Cipher (Decrypt)
3. ROT13
4. Atbash Cipher
5. Frequency Analysis
6. Brute Force (try all shifts)
7. Exit

Enter your choice (1-7): 1
Enter the text: Hello World
Enter the shift value (integer): 3

✓ Encrypted text: Khoor Zruog
```

#### Caesar Cipher Decryption
```bash
Enter your choice (1-7): 2
Enter the text: Khoor Zruog
Enter the shift value (integer): 3

✓ Decrypted text: Hello World
```

#### ROT13
```bash
Enter your choice (1-7): 3
Enter the text: Hello World

✓ ROT13 result: Uryyb Jbeyq
```

#### Atbash Cipher
```bash
Enter your choice (1-7): 4
Enter the text: Hello World

✓ Atbash result: Svool Dliow
```

#### Frequency Analysis
```bash
Enter your choice (1-7): 5
Enter the text: The quick brown fox jumps over the lazy dog

✓ Letter frequency analysis (sorted by frequency):
  o:  9.30% ████
  e:  6.98% ███
  u:  6.98% ███
  ...
```

#### Brute Force Attack
```bash
Enter your choice (1-7): 6
Enter the text: Khoor Zruog

✓ Trying all possible Caesar cipher shifts:
  Shift  1: Jgnnq Yqtnf
  Shift  2: Ifmmp Xpsme
  Shift  3: Hello World
  ...
Hint: Look for readable English text in the results above.
```
