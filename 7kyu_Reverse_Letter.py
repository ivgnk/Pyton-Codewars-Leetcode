'''
Simple Fun #176: Reverse Letter
https://www.codewars.com/kata/58b8c94b7df3f116eb00005b/train/python

Given a string str, reverse it and omit all non-alphabetic characters.

Example
For str = "krishan", the output should be "nahsirk".
For str = "ultr53o?n", the output should be "nortlu".

Input/Output
[input] string str
A string consists of lowercase latin letters, digits and symbols.
[output] a string
'''

def reverse_letter(st):
    s= [ss for ss in st if ss.isalpha()]
    s2= ''.join(s)
    return s2[::-1]

print(reverse_letter("krishan")) # "nahsirk"
print(reverse_letter("ultr53o?n")) # "nortlu"