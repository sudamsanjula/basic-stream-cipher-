# Sudam Sanjula
# Stream Cipher

# Function to convert a plaintext into ASCII values
def convert_to_ascii(text):
    return [ord(char) for char in text]

# Function to convert a list of ASCII values back into a text
def convert_to_text(ascii_values):
    return ''.join(chr(value) for value in ascii_values)

# Function to generate a complex keystream with key
def generate_complex_keystream(key):
    key_ascii = [ord(char) for char in key]

#Add more complexity to the keystream generation
    for i in range(len(key_ascii)):
        key_ascii[i] = (key_ascii[i] * 2 + 5) % 256

    return key_ascii

# Encryption function with key
def encrypt(plaintext, key):
    #Convert the both key and plaintext into ASCII values
    complex_keystream = generate_complex_keystream(key)
    plaintext_ascii = convert_to_ascii(plaintext)

#initialize an empty list to store the encrypted ASCII values
    encrypted_text = []
    key_length = len(complex_keystream)

#Perform a loop over every character in the plaintext.
    for i in range(len(plaintext_ascii)):
        char_ascii = plaintext_ascii[i]
        key_char_ascii = complex_keystream[i % key_length]

 #Perform key addition and apply modulus operation
        encrypted_char = (char_ascii + key_char_ascii) % 256
        encrypted_text.append(encrypted_char)

 #Convert the encrypted ASCII values back to a text
    return convert_to_text(encrypted_text)

# Decryption function with key
def decrypt(encrypted_text, key):
    #Convert the both key and encrypted text into ASCII values
    complex_keystream = generate_complex_keystream(key)
    encrypted_ascii = [ord(char) for char in encrypted_text]

#Initialize an empty list to store the decrypted ASCII values
    decrypted_text = []
    key_length = len(complex_keystream)

#Perform a loop over every character in the encrypted text
    for i in range(len(encrypted_ascii)):
        char_ascii = encrypted_ascii[i]
        key_char_ascii = complex_keystream[i % key_length]

#Perform key subtraction and modulus operation
        decrypted_char = (char_ascii - key_char_ascii) % 256
        decrypted_text.append(decrypted_char)

#Convert the decrypted ASCII values back to a text
    return convert_to_text(decrypted_text)

#Main function to get user input, key and call encryption or decryption functions
def main():
    while True:
        choice = input("Do you want to encrypt or decrypt? (e/d): ")

        if choice.lower() == 'e':
            plaintext = input("Enter the plaintext: ")
            key = input("Enter the key: ")
            encrypted_text = encrypt(plaintext, key)
            print("Encrypted text:", encrypted_text)
        elif choice.lower() == 'd':
            encrypted_text = input("Enter the encrypted text: ")
            key = input("Enter the key: ")
            decrypted_text = decrypt(encrypted_text, key)
            print("Decrypted text:", decrypted_text)
        else:
            print("Invalid choice. Please enter 'e' for encrypt or 'd' for decrypt.")
            continue

        more_choice = input("Do you want to do more? (y/n): ")
        if more_choice.lower() != 'y':
            break

# Call the main function
if __name__ == "__main__":
    main()
