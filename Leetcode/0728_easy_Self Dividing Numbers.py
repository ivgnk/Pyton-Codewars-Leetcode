"""
Done 02.05.2024
728. Self Dividing Numbers
https://leetcode.com/problems/self-dividing-numbers/description/

A self-dividing number is a number that is divisible by every digit it contains.
For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
A self-dividing number is not allowed to contain the digit zero.
Given two integers left and right, return a list of all the self-dividing numbers in the range [left, right].

Example 1:
Input: left = 1, right = 22
Output: [1,2,3,4,5,6,7,8,9,11,12,15,22]

Example 2:
Input: left = 47, right = 85
Output: [48,55,66,77]
"""

from collections import Counter
def selfDividingNumbers(left, right):
    """
    :type left: int
    :type right: int
    :rtype: List[int]
    """
    # res=[]
    # for i in range(left, right+1):
    #     s=str(i)
    #     if '0' not in s:
    #         dd = dict(Counter(s))
    #         if all([True if i % int(k) == 0 else False for k, v in dd.items()]): res.append(i)
    # return res

    # Runtime 55 ms Beats 27.78% of users with Python
    # Memory 11.67# MB Beats 93.83%
    # of users with Python
    res=[]
    for i in range(left, right+1):
        s=str(i)
        if '0' not in s:
            if all([True if i % int(k) == 0 else False for k in s]): res.append(i)
    return res



# print(selfDividingNumbers(left = 1, right = 22))
print(selfDividingNumbers(left = 47, right = 85))
