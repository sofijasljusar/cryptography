from string import ascii_lowercase as alphabet
from collections import Counter


def get_shift(text):
    most_frequent = Counter(text).most_common(1)[0][0]
    shift = (alphabet.index(most_frequent) - alphabet.index("e")) % 26
    return shift


def decrypt_caesar(text):
    key = get_shift(text)
    decrypted_letters = ""
    for x in text:
        if x in alphabet:
            encrypted_index = alphabet.index(x)
            initial_index = (encrypted_index - key) % 26
            decrypted_letters += alphabet[initial_index]
        else:
            decrypted_letters += x
    return decrypted_letters


encrypted_message = input("Type your encrypted message:").lower()
decrypted_message = decrypt_caesar(encrypted_message)
print(f"Decrypted message: {decrypted_message}")

# message 1
# gluhtlishjrvbadvyyplkaohavbyjpwolypzavvdlhrvuuleatlzzhnlzdpajoavcpnlulyljpwolyrlfdvykpzaolopkkluzftivsvmklhaoputfmhcvypalovsilpuluk
# message 2
# vwduw ljudeehghyhubwklqjlfrxogilqgsohdvhuhwxuqdqbeoxhsulqwviruydxowd qgdodupghvljqedvhgrqzklfkedqnbrxghflghrqldpvhwwlqjxsvdihkrxvhfr


# PREVIOUS CODE - improvements as comments
# import statistics  # no need to import the whole module
# encrypted_message = input("Type your encrypted message:")
# letters = [*encrypted_message]

# made it a function
# most_frequent = statistics.mode([char for char in letters if char != ' '])   # switched to more efficient Counter
# disadvantages of counter - extracting value may be verbose
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# key = (alphabet.index(most_frequent) - alphabet.index("e"))%26

# made it a function
# decrypted_letters = []
# for x in letters:
#     if x == " ":
#         decrypted_letters.append(" ")
#     else:
#         encrypted_index = alphabet.index(x.lower())
#         decrypted_letters.append(alphabet[(encrypted_index-key)%26])
# decrypted_letters[0] = decrypted_letters[0].upper()
# print(f"Decrypted message: {''.join(decrypted_letters)}")