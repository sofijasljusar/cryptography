from polybius_cipher import encrypt_polybius
from decrypt_secret_code import convert_between_bases, get_otp, NEWSPAPER, xor

secret_message = ('startcibcbankseeschematicsforalarmandvault'
                  'hittomorrowat10amafteralarmtestvaultcodeis'
                  '5567meetatblackoutend')

# secret_message = "abc"
# secret_message = "fff"
# secret_message = "bbb"


# STEP 1 - use polybius spiral to encode message
polybius_encrypted = encrypt_polybius(secret_message)
print(f"step 1 {polybius_encrypted}\n\n")

# STEP 2 - convert to base 2
message_in_binary = convert_between_bases(polybius_encrypted, 1, 10, 2)
print(f"step 2 {message_in_binary}\n\n")

# STEP 3 - XOR with one-time pad
otp = get_otp(NEWSPAPER, len(message_in_binary))
xored_message = xor(message_in_binary, otp)
print(f"step 3"
      f"\notp {otp}"
      f"\nxored {xored_message}\n\n")

# STEP 4 - divide into 4 digits and convert to base-10
# STEP 5 - convert to base 4
encrypted_message = convert_between_bases(xored_message, 4, 2, 4)
print(f"encrypted message {encrypted_message}")

# STEP 6 - angles from message (make tkinter program!)

