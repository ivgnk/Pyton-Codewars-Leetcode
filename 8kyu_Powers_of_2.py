'''
https://www.codewars.com/kata/57a083a57cb1f31db7000028/train/python
Complete the function that takes a non-negative integer n as input,
and returns a list of all the powers of 2 with the exponent ranging from 0 to n ( inclusive ).
Examples
n = 0  ==> [1]        # [2^0]
n = 1  ==> [1, 2]     # [2^0, 2^1]
n = 2  ==> [1, 2, 4]  # [2^0, 2^1, 2^2]
'''

def powers_of_two(n):
    # a = []
    # for i in range(n+1):
    #     a.append(2**i)
    # return a
    return [2 ** i for i in range(n + 1)]

for i in range(3):
    print(powers_of_two(i))