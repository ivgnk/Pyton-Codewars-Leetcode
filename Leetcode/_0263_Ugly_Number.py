'''
An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.
Given an integer n, return true if n is an ugly number.


Example 1:
Input: n = 6
Output: true
Explanation: 6 = 2 × 3

Example 2:
Input: n = 1
Output: true
Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.

Example 3:
Input: n = 14
Output: false
Explanation: 14 is not ugly since it includes the prime factor 7.
'''
import numpy as np

import numpy as np

def isUgly(n):
    """
    :type n: int
    :rtype: bool
    """
    def isn(n,mmain):
        return n in mmain

    mmax = 2_147_483_647*2
    if (n <= 0) or (n > mmax): return False;
    if n == 1: return True;

    llsti = np.array([2, 3, 5])
    llstr = [2, 3, 5]
    b = True; i = 0
    while b:
        dat2 = llsti * 2
        dat3 = llsti * 3
        dat5 = llsti * 5
        llstr = llstr + list(dat2)
        llstr = llstr + list(dat3)
        llstr = llstr + list(dat5)
        llstr = list(set(llstr))
        llstr.sort()
        b = (max(llstr) < mmax) and (i<133)
        llstr = [item for item in llstr if (item >= 0)]
        llsti = np.array(llstr)
        i = i+1 # print(f'{i=}  {max(llstr):_}'); input()

    llstr = [item for item in llstr if ((item >= 0) and (item < mmax))]
    mmain = sorted(set(llstr))
    print(mmain)

    print('in ==== ',2123366400 in mmain)
    if isn(n,mmain): return True
    elif all(n % nn == 0 for nn in mmain):
        return True
    else: return False




# print(isUgly(-51799))
print(isUgly(2123366400))