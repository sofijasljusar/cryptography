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
