from polybius_breaker import decrypt_polybius_spiral

NEWSPAPER = ('thewholegraingoodnessofbluechipdividendstockshasitslimitsutilitystocksconsumerstaples'
             'pipelinestelecomsandrealestateinvestmenttrustshavealllostgroundoverthepastmonthevenwh'
             'ilethebroadermarkethasbeenflatwiththebondmarketsignallinganexpectationofrisinginteres'
             'tratesthefiveyearrallyforsteadybluechipdividendpayershasstalledshouldyoubescaredifyou'
             'ownalotofthesestockseitherdirectlyorthroughmutualfundsorexchangetradedfundsdavidbaski'
             'npresidentofbaskinfinancialserviceshasatwoprongedanswerkeepyourtopqualitydividendstoc'
             'ksbutbepreparedtofollowhisfirmsexampleintrimmingholdingsinstockssuchastranscanadacorp'
             'keyeracorpandpembinapipelinecorpletsh')


def convert_from_base(number, from_base):
    """Simple function to convert number from any given base to base-10"""
    formatted_number = number[::-1]
    result = 0
    for i in range(len(formatted_number)):
        position_value = from_base ** i
        result += int(formatted_number[i]) * position_value
    return result
    # position_value = 1
    # for digit in formatted_number:
    #     result += int(digit) * position_value
    #     position_value *= from_base
    # return result


def convert_string_from_base(string_of_numbers, length, from_base):
    """Function that takes a string of integers,
    divides into numbers of given length and converts each to base-10.
    Returns converted list"""
    formatted_list = [string_of_numbers[i:i + length] for i in range(0, len(string_of_numbers), length)]
    # print(formatted_list)
    converted_list = [convert_from_base(number, from_base) for number in formatted_list]
    return converted_list


def convert_to_base(number, to_base):
    """Simple function to convert number from base-10 to any given base"""
    if number == 0:
        return "0"
    result = ""
    while number > 0:
        digit = number % to_base
        result += str(digit)
        number = number // to_base
    return result[::-1]


def convert_list_to_base(list_of_numbers, to_base):
    """Function that takes a list of integers and converts to any given base.
     Each number is taking up the same amount of spaces (zero filled to length required by maximum number in list).
    Returns converted string """
    #  this 2 lines caused edge case bug (encryption):
    #  when only messages that contain symbols that produce only 0-3 in row/column
    #  binary conversion in step 2 did not append to 3 0s, as maximum (3) produced (11) which is 2 digits
    # so need to state explicitly, instead of dynamically
    maximum_length = len(convert_to_base(max(list_of_numbers), to_base))
    converted_list = [convert_to_base(number, to_base).zfill(maximum_length) for number in
                      list_of_numbers[:len(list_of_numbers)]]
    # print(converted_list)
    converted_string = "".join(converted_list)
    return converted_string


def adjust_length(string, expected_length):
    """Function that is needed to cut off extra zeros in last number
    due to the difference of encryption and decryption processes.
    During encryption string of binary is divided into 4 digit pieces
    (may not divide equally if last number in base 10 is less than 8 (base 4 - 20)).
    And in decryption all converted numbers are appended to maximum length (required length).
    So it will always be a multiple of 4, which may produce extra numbers"""
    # print(expected_length)
    # print(len(string))
    temporary_list = [string[i:i + 4] for i in range(0, len(string), 4)]
    if len(string) % expected_length:
        difference = len(string) % expected_length
        # print(f"difference {difference}")
        new_item = temporary_list.pop()[difference:]
        # print(new_item)
        temporary_list.append(new_item)
        adjusted_string = "".join(temporary_list)
        return adjusted_string
    return string


def convert_between_bases(string_of_numbers: str, divide_into: int, from_base: int, to_base: int) -> str:
    """Function that takes a list of integers,
    converts from any base to any base,
    and returns converted string"""
    base_10 = convert_string_from_base(string_of_numbers, divide_into, from_base)
    given_base = convert_list_to_base(base_10, to_base)
    return given_base


def get_otp(text, length):
    cut_text = text[:length]
    otp = "".join("1" if letter in 'aeiouy' else "0" for letter in cut_text)
    return otp


def xor(string1, string2):
    xored_string = "".join("0" if digit_1 == digit_2 else "1"
                           for digit_1, digit_2 in zip(string1, string2))
    return xored_string


if __name__ == "__main__":
    # STEP 1 - angles from message as digits (manually ANGLES)

    ANGLES = ('203322210033300102202202322011330330033203002201332323100322131320011103222020202233201'
              '323133322303301202110121100322313220200103102332031031201113332230201003210103001102331'
              '100200302331100303010233022321301203122200031331001011210323022013023230312333200212333'
              '0003012301303010303232202302003222332230202312023133002')
    print(f"step 1 {ANGLES}\n\n")
    MESSAGE_LENGTH = len(ANGLES) // 3  # expected final message length, because 1,5 angles (3 digits) represent 1 letter

    # STEP 2 - convert to binary
    # 1) convert from any base (this case base 4) to base 10
    # 2) convert from base 10 to any base (this case base 2)
    angles_in_binary = adjust_length(convert_between_bases(ANGLES, 2, 4, 2), MESSAGE_LENGTH)
    print(f"step 2 {angles_in_binary}\n\n")

    # STEP 3 - XOR with one-time pad
    # 1) get otp
    # 2) do xor operation

    one_time_pad = get_otp(NEWSPAPER, len(angles_in_binary))
    xored_binary = xor(angles_in_binary, one_time_pad)
    print(f"step 3"
          f"\notp {one_time_pad}"
          f"\nxored {xored_binary}\n\n")

    # STEP 4 - divide into 3 digits and convert to base 10
    polybius_encrypted = convert_between_bases(xored_binary, 3, 2, 10)
    print(f"step 4 {polybius_encrypted}\n\n")

    # STEP 5 - use polybius spiral to decode message
    decrypted_message = decrypt_polybius_spiral(polybius_encrypted)
    print(f"step 5 {decrypted_message}\n\n")
