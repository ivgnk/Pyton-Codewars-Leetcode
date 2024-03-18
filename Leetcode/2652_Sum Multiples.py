'''
2652. Sum Multiples
https://leetcode.com/problems/sum-multiples/description/

Given a positive integer n, find the sum of all integers
in the range [1, n] inclusive that are divisible by 3, 5, or 7.
Return an integer denoting the sum of all numbers
in the given range satisfying the constraint.
'''

def sumOfMultiples(n):
    """
    :type n: int
    :rtype: int
    """
    s=0
    for i in range(n+1):
        if (i%3==0):
            s = s + i
        elif (i%5==0):
            s = s + i
        elif (i%7==0):
            s = s + i
    return s
