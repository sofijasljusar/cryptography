from string import ascii_lowercase as alphabet
message = input("Type your message: ").lower()
key = int(input("Type shift: "))


def encrypt_caesar(text, shift):
    encrypted_text = ""
    for x in text:
        if x in alphabet:
            initial_index = alphabet.index(x)
            encrypted_index = (initial_index + shift) % 26
            encrypted_text += alphabet[encrypted_index]
        else:
            encrypted_text += x
    return encrypted_text


encrypted_message = encrypt_caesar(message, key)
print(f"Encrypted message: {encrypted_message}")
