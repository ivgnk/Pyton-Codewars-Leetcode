'''
String ends with?
https://www.codewars.com/kata/51f2d1cafc9c0f745c00037d/train/python

Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).
Examples:
solution('abc', 'bc') # returns true
solution('abc', 'd') # returns false
'''

# https://stackabuse.com/python-remove-the-prefix-and-suffix-from-a-string/

def solution(text, ending):
    lbefore = len(text)
    res = text.removesuffix(ending)
    lafter = len(res)
    return lafter !=lbefore