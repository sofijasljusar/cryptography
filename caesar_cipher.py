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

# PREVIOUS CODE
# improvements made - comments

# message = input("Type your message:")
# letters = [*message] # 1 - removed unnecessary list conversion
# key = 3  # taking key as input
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
# 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# imported from library instead to avoid error and memory overhead (plus it is a string)
# # making it a function
# encrypted_letters = [] # 2 - it can be string right away
# for x in letters:
#     if x == " ":  # 3 - first checking if in alphabet - do caesar shift,
#     ...else - add whatever it is (a space, a symbol, a number()
#         encrypted_letters.append(" ")
#     else:
#         initial_letters = alphabet.index(x.lower())
#         encrypted_letters.append(alphabet[(initial_letters+key)%26])
# encrypted_letters[0] = encrypted_letters[0].upper() # 4- no need to capitalize the first letter
# print(f"Encrypted message: {''.join(encrypted_letters)}")
