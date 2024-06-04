'''
Done 04.06.2024. Topics: Math, Binary Search

69. Sqrt(x).
https://leetcode.com/problems/sqrtx/description/
Given a non-negative integer x, return the square root of x rounded down to the nearest integer.
The returned integer should be non-negative as well.
You must not use any built-in exponent function or operator.
For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

Example 1:
Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.

Example 2:
Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.

Hint 1
Try exploring all integers.
Hint 2
Use the sorted property of integers to reduced the search space.
'''

# Runtime 29 ms Beats 96.19% of users with Python3
# Memory 16.46 MB Beats 83.62% of users with Python3
# https://leetcode.com/problems/sqrtx/solutions/4083846/python-98-beats-6-lines-code-2nd-approach-simple-code/
# from https://leetcode.com/u/vvivekyadav/


from icecream import ic
def mySqrt(x):
    if x <2: return x
    a = 0
    b = x
    while b-a !=1:
        mid = (a+b)//2
        if mid * mid==x: return mid
        else:
            if mid*mid>x:
                b=mid
            else:
                a=mid
    return a

ic(mySqrt(8))





dd1={4:2,9:3,16:4,25:5,36:6}
def mySqrt2(x):
    """
    :type x: int
    :rtype: int
    """
    if x==0: return 0
    elif x in [1,2,3]: return 1
    elif x in dd1: return dd1[x]
    a=0; a2=0
    b=46341; delta =b-a; deltaold = 0
    b2=b**2; i =  0
    while (delta>1):
        if x==b2: return b;
        if x==a2: return a;
        elif x>(b//2)**2:
            a = b//2
            a2=a**2
        else:
            b = b//2
            b2 = b**2
        deltaold = delta
        delta = b-a
        # print(f'{i=} {a=} {b=} {delta=} {deltaold=}'); i = i+1; input()
        if delta==deltaold: return a
    return a+1

# print(mySqrt(8))

