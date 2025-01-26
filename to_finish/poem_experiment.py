from string import punctuation, whitespace
from string import ascii_lowercase as alphabet

poem = """
If you think you are beaten, you are;
If you think you dare not, you don't;
If you like to win, but think you can't,
It is almost certain you won't.

If you think you'll lose, you're lost;
For out in the world we find
Success begins with a fellow's will —
It's all in the state of mind.

If you think you're outclassed, you are;
You've got to think high to rise.
You've got to be sure of yourself
Before you can win a prize.

Life's battles don't always go
To the stronger or faster man;
But sooner or later, the man who wins
Is the man who thinks he can.

Walter D. Wintle - Thinking 
"""
translator = str.maketrans('', '', punctuation + whitespace + "—")
formatted_text = poem.translate(translator).lower()
keyword = 'soda'
keyword_shifts = [alphabet.index(letter) for letter in keyword]

encrypted_message = ""
for index_in_text, char in enumerate(formatted_text):
    initial_index = alphabet.index(char)
    # i % len(keyword) start from the beginning of shifts list again
    encrypted_index = (initial_index+keyword_shifts[index_in_text % len(keyword)]) % 26
    encrypted_message += alphabet[encrypted_index]
print(encrypted_message)
# atbomhkifybomouetsdtwbbomoueatbomhkifybomrdrwbrtqcxdgbwixmrudwnelczifpxtlvlncmruuoqtahlsszpokhfejhdifmruocqtatbomhkifybomzolgghygiuedcvtxcuomhlnlvhwgfodosiifrvuuqhskphgabvwahkaxsolgkvwazoilgdldwqtzsvtshhoxalnvwiygiwhabnygiuegiwcdovswrbomoueqcxvwurtlcwhabnhauktgflswmrunsjolhrbwgxrwciygiuswzibwtrrwmruuoqwabdpjwcedwiekpdtlzhsvcqtszzaqgjolcwhwgwrgbjejcufsgwejadntiwsgcqejculshhrlvhmsbzhgklnkwvtzspafkkolvlncgkeuoqwszwejrzifhoelvlncwqg
