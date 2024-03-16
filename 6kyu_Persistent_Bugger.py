'''
Persistent Bugger.
https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec/train/python

Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence,
which is the number of times you must multiply the digits in num until you reach a single digit.

For example (Input --> Output):
39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit)
999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2)
4 --> 0 (because 4 is already a one-digit number)
'''
import math

def persistence(n):
    n1 = str(n)
    llen=len(n1)
    if llen==1: return 0
    else:
        i = 0
        while llen !=1:
            s = [int(ss) for ss in n1]
            print(s)
            n1 = str(math.prod(s))
            i = i+1
            llen=len(n1)
            print(n1)
        return i

print(persistence(39))