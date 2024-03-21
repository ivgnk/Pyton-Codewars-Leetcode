'''
https://www.codewars.com/kata/54d512e62a5e54c96200019e/train/python
Given a positive number n > 1 find the prime factor decomposition of n.
The result will be a string with the following form :
 "(p1**n1)(p2**n2)...(pk**nk)"
with the p(i) in increasing order and n(i) empty if n(i) is 1.

Example: n = 86240 should return "(2**5)(5)(7**2)(11)"
'''

# Разложить число на простые множители
# https://ru.stackoverflow.com/questions/645227/Разложить-число-на-простые-множители

from collections import Counter
import collections

def prime_factors(n):
    def primfacs(n):
       i = 2
       primfac = []
       while i * i <= n:
           while n % i == 0:
               primfac.append(i)
               n = n / i
           i = i + 1
       if n > 1:
           primfac.append(int(n))
       return primfac

    lst = primfacs(n)
    # print(lst)
    ddict = Counter(lst)
    # print(ddict)
    res2=collections.OrderedDict(sorted(ddict.items()))
    # print(res2)
    s=''
    for key, value in res2.items():
        if value==1: s=s+f'({key})'
        else: s=s+f'({key}**{value})'
    return s


print(prime_factors(7919))
print(prime_factors(7775460))