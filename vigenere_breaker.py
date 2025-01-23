from string import ascii_lowercase as alphabet


def decrypt_vigenere(text, keyword):
    """Vigenere decryption with keyword"""
    keyword_shifts = [alphabet.index(letter) for letter in keyword]
    decrypted_letters = ""
    for index_in_text, char in enumerate(text):
        encrypted_index = alphabet.index(char)
        # i % len(keyword) start from the beginning of shifts list again
        initial_index = (encrypted_index-keyword_shifts[index_in_text % len(keyword)]) % 26
        decrypted_letters += alphabet[initial_index]
    return decrypted_letters


encrypted_message = input("Type your encrypted message:").lower()
secret_word = input("Type the secret word:")
decrypted_message = decrypt_vigenere(encrypted_message, secret_word)
print(f"Decrypted message: {decrypted_message}")


# text: klkbnqlcytfysryucocphgbdizzfcmjwkuchzyeswfogmmetwwossdchrzyldsbwnydednzwnefydthtddbojicemlucdygicczhoadrzcylwadsxpilpiecskomoltejtkmqqymehpmmjxyolwpeewjckznpccpsvsxauyodhalmriocwpelwbcniyfxmwjcemcyrazdqlsomdbfljwnbijxpddsyoehxpceswtoxwbleecsaxcnuetzywfn
# keyword: sskkuullll

# PREVIOUS - improvements as comments (previous improvements to other files not included)
# # with keyword
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# encrypted_message = input("Type your encrypted message:")
# keyword = input("Type the keyword:")  #removed unnecessary lists
# encrypted_letters = [*encrypted_message] # removed unnecessary lists
# key_letters = [*keyword]
# key_indexes = []  # used list comprehension instead!!!
# for letter in key_letters:
#     key = alphabet.index(letter)
#     key_indexes.append(key)
# print(key_indexes)
# index = 0  # used enumerate instead of manual index handling!!!
# decrypted_letters = []
# for x in encrypted_letters:
#     encrypted_index = alphabet.index(x)
#     decrypted_letters.append(alphabet[(encrypted_index-key_indexes[index%len(keyword)])%26])
#     index += 1
#
# print(f"Decrypted message: {''.join(decrypted_letters)}")



# DOESN'T WORK - how to decrypt this cipher without keyword, but with length?
# figure out length
# break down string into found number of strings with each containing according sequence of nth letters
# analyze frequency for each and break n caesar ciphers

# without keyword
# import statistics
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# encrypted_message = input("Type your encrypted message:")
# letters = [*encrypted_message]
# length_of_keyword = int(input("Type the length of keyword:"))
# index = 0
# nth_letter_index = 0
# list2 = []
# for _ in range(length_of_keyword):
#     list1 = []
#     nth_letter_index = index
#     while nth_letter_index < len(letters):
#         list1.append(letters[nth_letter_index])
#         nth_letter_index += length_of_keyword
#     list2.append(list1)
#     index += 1
#
# key_indexes = []
#
# for sublist in list2:
#     print(sublist)
#     most_frequent = statistics.mode([char for char in sublist if char != ' '])
#     print(most_frequent)
#     key = (alphabet.index(most_frequent)) % 26-1
#     key_indexes.append(key)
# print(key_indexes)
#
# place = 0
# decrypted_letters = []
# for x in letters:
#     encrypted_index = alphabet.index(x)
#     decrypted_letters.append(alphabet[(encrypted_index-key_indexes[place%length_of_keyword])%26])
#     place += 1
#
# print(f"Decrypted message: {''.join(decrypted_letters)}")