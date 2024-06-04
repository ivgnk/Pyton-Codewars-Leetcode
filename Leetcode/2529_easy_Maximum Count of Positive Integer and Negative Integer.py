"""
Done 04.06.2024. Topics: Array, Binary Search, Counting
2529. Maximum Count of Positive Integer and Negative Integer
https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/description/

Given an array nums sorted in non-decreasing order, return the maximum between the number
of positive integers and the number of negative integers.
In other words, if the number of positive integers in nums is pos and the number of negative integers is neg,
then return the maximum of pos and neg.
Note that 0 is neither positive nor negative.

Example 1:
Input: nums = [-2,-1,-1,1,2,3]
Output: 3
Explanation: There are 3 positive integers and 3 negative integers. The maximum count among them is 3.

Example 2:
Input: nums = [-3,-2,-1,0,0,1,2]
Output: 3
Explanation: There are 2 positive integers and 3 negative integers. The maximum count among them is 3.

Example 3:
Input: nums = [5,20,66,1314]
Output: 4
Explanation: There are 4 positive integers and 0 negative integers. The maximum count among them is 4.

Hint 1
Count how many positive integers and negative integers are in the array.
Hint 2
Since the array is sorted, can we use the binary search?
"""

# Runtime 91 ms Beats 48.36% of users with Python
# Memory 11.85 MB Beats 75.82% of users with Python
# Runtime 79 ms Beats 97.13% of users with Python
# Memory 11.79 MB Beats 94.67% of users with Python

def maximumCount(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nl=nums.count(0)
    ll=len(nums)
    pos = sum([i > 0 for i in nums])
    neg = ll-pos-nl
    return max(pos, neg)



# Runtime 88 ms Beats 66.39% of users with Python
# Memory 11.89 MB Beats 75.82% of users with Python
def maximumCount3(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    pos, neg = 0, 0
    for i in nums:
        if i > 0: pos=pos+1
        elif i < 0: neg=neg+1
    return max(pos, neg)


# Runtime 84 ms Beats 87.30% of users with Python
# Memory 11.80 MB Beats 94.67% of users with Python
def maximumCount2(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    pos = sum([i > 0 for i in nums])
    neg = sum([i < 0 for i in nums])
    return max(pos, neg)


