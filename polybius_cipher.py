alphabet_spiral = [
    ["f", "g", "h", "i", "j", "k"],
    ["e", "x", "y", "z", "0", "l"],
    ["d", "w", "7", "8", "1", "m"],
    ["c", "v", "6", "9", "2", "n"],
    ["b", "u", "5", "4", "3", "o"],
    ["a", "t", "s", "r", "q", "p"]
]
message = 'startcibcbankseeschematicsforalarmandvaulthittomorrowat10amafteralarmtestvaultcodeis5567meetatblackoutend'


def encrypt_polybius(text):
    encrypted_message = ''
    for letter in text:
        row = 0
        column = 0
        letter_found = False
        while not letter_found:
            if alphabet_spiral[row][column] == letter:
                encrypted_message += f'{row}{column}'
                letter_found = True
            else:
                if column == 5:
                    column = 0
                    row += 1
                else:
                    column += 1
    return encrypted_message

# print(encrypt_polybius(message))

# TODO: need to change to something else than string?
# 525150535130034030405035055210105230021025505103305200455350155053255035203150411551020351514525455353452150512414502550005110535015505325511052513150411551304520100352424232222510105150514015503005454151103520