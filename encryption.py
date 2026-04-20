def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char

    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

while True:
    print("\nEncryption Tool")
    print("1. Encrypt text")
    print("2. Decrypt text")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        text = input("Enter text: ")
        shift = int(input("Shift value: "))
        print("Encrypted:", encrypt(text, shift))

    elif choice == "2":
        text = input("Enter text: ")
        shift = int(input("Shift value: "))
        print("Decrypted:", decrypt(text, shift))

    elif choice == "3":
        break

    else:
        print("Invalid choice")
