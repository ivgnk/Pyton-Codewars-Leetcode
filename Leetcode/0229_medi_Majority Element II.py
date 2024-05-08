"""
Done 08.05.2024. Topics: Array, Hash Table, Sorting, Counting
229. Majority Element II
https://leetcode.com/problems/majority-element-ii/description/

Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
Example 1:

Input: nums = [3,2,3]
Output: [3]
Example 2:

Input: nums = [1]
Output: [1]
Example 3:

Input: nums = [1,2]
Output: [1,2]
"""

# Runtime 86 ms Beats 44.94% of users with Python
# Memory 12.74 MB Beats 69.77% of users with Python
# Runtime 79 ms Beats 78.27% of users with Python
# Memory 12.96 MB Beats 28.61% of users with Python

from collections import Counter
def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    lln = len(nums)
    dd = dict(Counter(nums))
    lld = len(dd)
    if lln==lld and lln<=3:
        if lln==3: return []
        else: return nums
    nf = lln/3
    return [k for k,v in dd.items() if v>nf]
