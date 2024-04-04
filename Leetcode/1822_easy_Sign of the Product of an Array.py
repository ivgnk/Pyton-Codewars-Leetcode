'''
1822. Sign of the Product of an Array
https://leetcode.com/problems/sign-of-the-product-of-an-array/description/

There is a function signFunc(x) that returns:
1 if x is positive.
-1 if x is negative.
0 if x is equal to 0.
You are given an integer array nums. Let product be the product of all values in the array nums.
Return signFunc(product).
'''

# Runtime 60 ms Beats 41.78% of users with Python3
# Memory 16.69 MB Beats 93.23% of users with Python3

import math
def arraySign(nums):
    pr = math.prod(nums)
    if pr > 0:
        return 1
    elif pr == 0:
        return 0
    else:
        return -1
