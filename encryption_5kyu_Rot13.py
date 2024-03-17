'''
Rot13
https://www.codewars.com/kata/530e15517bc88ac656000716/train/python

ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet.
ROT13 is an example of the Caesar cipher.
Create a function that takes a string and returns the string ciphered with Rot13.
If there are numbers or special characters included in the string, they should be returned as they are.
Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".
Please note that using encode is considered cheating.
'''

# https://pythobyte.com/how-to-use-rot13-in-python-af74866c/

abc = "abcdefghijklmnopqrstuvwxyz"
abch = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def rot13(message):
    news=""
    m = message
    m = m.lower()
    # print(message,m)
    for i,ss in enumerate(m):
       if  ss.isalpha():
           sss = abc[(abc.find(ss)+13)%26]
           if message[i] in abch:
               sss = sss.upper()
           news = news + sss
       else:
           news=news+ss
    return news

# print(rot13("test"))
print(rot13("Test"))