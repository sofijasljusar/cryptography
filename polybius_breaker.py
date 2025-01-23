# code 1
alphabet_square = [
    ["a", "f", "k", "p", "u"],
    ["b", "g", "l", "q", "v"],
    ["c", "h", "m", "r", "w"],
    ["d", "i", "n", "s", "x"],
    ["e", "j", "o", "t", "y"]
]
# code 2
alphabet_spiral = [
    ["f", "g", "h", "i", "j", "k"],
    ["e", "x", "y", "z", "0", "l"],
    ["d", "w", "7", "8", "1", "m"],
    ["c", "v", "6", "9", "2", "n"],
    ["b", "u", "5", "4", "3", "o"],
    ["a", "t", "s", "r", "q", "p"]
]

def decrypt_polybius_square(text):
    letters = ""
    numbers = [int(char) for char in text]
    index = 0
    while index < len(numbers)-1:
        first_number = numbers[index]-1  # -1 because index in matrix from 0 to 4 and code 1 has numbers from 1 to 5
        second_number = numbers[index+1]-1
        letters += alphabet_square[first_number][second_number]
        index += 2
    return letters


def decrypt_polybius_spiral(text):
    numbers = [int(char) for char in text]
    # use join on generator that yields letter from alphabet based on pair of numbers from encrypted text
    letters = ''.join(alphabet_spiral[numbers[i]][numbers[i + 1]] for i in range(0, len(numbers)-1, 2))
    return letters


encryption_type = input("Enter 'square' or 'spiral':")
encrypted_message = input("Type your encrypted message:")
if encryption_type == 'square':
    decrypted_message = decrypt_polybius_square(encrypted_message)
elif encryption_type == 'spiral':
    decrypted_message = decrypt_polybius_spiral(encrypted_message)
print(f"Decrypted message: {decrypted_message}")


# code 1
# 4454113454112333534454124243424432514121231131135315544254424442434432514153435432423441112551355334134243225343114454345343225134314214325134125334121554153451335144441122514442544244441534512355154321345111131121235142543153332142435144531534143451254253154433515432534144343513544

# with corrected angle
# a = 525150535130034030405035055210105230021025505103305200455350155053255035203150411551020351514525455353452150512414502550005110535015505325511052513150401551304520100352424232222510105150514015503005454151103522
# with y
# code 2
# 525150535130034030405035055210105230021025505103305200455350155053255035203150411551020351514525455353452150512414502550005110535015505325511052513150401551304520100352424232222510105150514015503005454151103522
# print(a == b)
# 5 vowels
# 525150535130034030405435055210105230021025505103305200455350155053255035203150411551020353510521455351452150112434502550005130535015505325511052513150401551304522100252424232222510105150514015503005414151103522
