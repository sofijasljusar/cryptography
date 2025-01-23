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
