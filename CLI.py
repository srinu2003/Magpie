from symmetric_encryption import *

print("Welcome to the Text encryption and decryption tool.")
print("""
    1. Encrypt : (e/E)
    2. Decrypt : (d/D)
    3. Exit    : (b/B)
      """)

while True:
    option = input('Enter option:')
    match option[0]:
        case '1' | 'e' | 'E':
            # Text Encrypt
            message = input('Enter your message: ')
            op = input("Want to generate a new key? (y/n):")
            if op == 'y':
                key = generate_key()
                print(encrypt_message(message, key))
            else:
                key = load_key()
                print(encrypt_message(message, key))

        case '2' | 'd' | 'D':
            # Text Decrypt
            message = input('Enter Chiphered message: ')
            op = input("Want to enter a key? (y/n):")
            if op == 'y':
                input_key = input('Enter your key: ')
                print(decrypt_message(message, input_key.encode()))
            else:
                print(decrypt_message(message, load_key()))

        case '3' | 'break' | 'b' | 'B':
            print("Exiting text...(bye!)")
            break
        case _:
            print("Something's wrong with your input! Please try again.")
            # break

