# my_dict = {'a': 1, 'b': 2, 'c': 3}
#
# for index, (key, value) in enumerate(my_dict.items()):
#     print(index, key, value)
from caesar_breaker import get_shift, decrypt_caesar
from collections import Counter
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# text = 'klkbnqlcytfysryucocphgbdizzfcmjwkuchzyeswfogmmetwwossdchrzyldsbwnydednzwnefydthtddbojicemlucdygicczhoadrzcylwadsxpilpiecskomoltejtkmqqymehpmmjxyolwpeewjckznpccpsvsxauyodhalmriocwpelwbcniyfxmwjcemcyrazdqlsomdbfljwnbijxpddsyoehxpceswtoxwbleecsaxcnuetzywfn'
# text = 'lxfopvefrnhrgqgrjjxvjfyhxlmwcxukznlwiqsvqzdchqhsnfkfncfnzxwyixhwdvwhjk'
text ='atbomhkifybomouetsdtwbbomoueatbomhkifybomrdrwbrtqcxdgbwixmrudwnelczifpxtlvlncmruuoqtahlsszpokhfejhdifmruocqtatbomhkifybomzolgghygiuedcvtxcuomhlnlvhwgfodosiifrvuuqhskphgabvwahkaxsolgkvwazoilgdldwqtzsvtshhoxalnvwiygiwhabnygiuegiwcdovswrbomoueqcxvwurtlcwhabnhauktgflswmrunsjolhrbwgxrwciygiuswzibwtrrwmruuoqwabdpjwcedwiekpdtlzhsvcqtszzaqgjolcwhwgwrgbjejcufsgwejadntiwsgcqejculshhrlvhmsbzhgklnkwvtzspafkkolvlncgkeuoq'

keyword_length = 4

segments = []
for i in range(0, keyword_length):
    new_segment = ""
    for j in range(i, len(text), keyword_length):
        new_segment += text[j]
    segments.append(new_segment)
print(segments)

decrypted_message = ""
for segment in segments:
    decrypted_segment = decrypt_caesar(segment)
    print(decrypted_segment)
# print(decrypted_message)

# startwarningiheardreportofourbreakinonthenewsstillwaitingonalarmtestschedulesiwillreportbacktomorrowwithfinalplanforextrasecurityisuggestweburnourlettersafterreadingandswitchourletterstonumbersusingpolybiussquaredropmessageunderthebenchattrainstationend
# keyword_shifts = [alphabet.index(letter) for letter in 'lemon']
# print(keyword_shifts)
