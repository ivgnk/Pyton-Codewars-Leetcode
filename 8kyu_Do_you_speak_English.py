'''
Do you speak "English"?
https://www.codewars.com/kata/58dbdccee5ee8fa2f9000058/train/python

Given a string of arbitrary length with any ascii characters.
Write a function to determine whether the string contains the whole word "English".
The order of characters is important -- a string "abcEnglishdef" is correct but "abcnEglishsef" is not correct.
Upper or lower case letter does not matter -- "eNglisH" is also correct.
Return value as boolean values, true for the string to contains "English", false for it does not.
'''

def sp_eng(sentence):
    rem_sym = ' ;#$%^&*()!?<>=[]'
    sentence = sentence.lower()
    # sentence.translate(rem_sym)
    res='english' in sentence
    return res

# print(sp_eng("english"))
print(sp_eng("English"))


