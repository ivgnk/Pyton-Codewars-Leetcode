"""
2553. Separate the Digits in an Array
Given an array of positive integers nums, return an array answer that
consists of the digits of each integer in nums after separating them in the same order they appear in nums.
To separate the digits of an integer is to get all the digits it has in the same order.
For example, for the integer 10921, the separation of its digits is [1,0,9,2,1].
"""

# Runtime 46 ms Beats 90.09% of users with Python
# Memory 12.00 MB Beats 43.97% of users with Python

def separateDigits(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    res=[]
    str_list=[str(i) for i in nums]
    for s1 in str_list:
        for letter in s1:
            res.append(int(letter))
    return res

print(separateDigits([13,25,83,77]))

