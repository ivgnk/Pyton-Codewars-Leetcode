"""
2149. Rearrange Array Elements by Sign
https://leetcode.com/problems/rearrange-array-elements-by-sign/description/

You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers.
You should return the array of nums such that the the array follows the given conditions:
Every consecutive pair of integers have opposite signs.
For all integers with the same sign, the order in which they were present in nums is preserved.
The rearranged array begins with a positive integer.
Return the modified array after rearranging the elements to satisfy the aforementioned conditions.

Example 1:
Input: nums = [3,1,-2,-5,2,-4]
Output: [3,-2,1,-5,2,-4]
Explanation:
The positive integers in nums are [3,1,2]. The negative integers are [-2,-5,-4].
The only possible way to rearrange them such that they satisfy all conditions is [3,-2,1,-5,2,-4].
Other ways such as [1,-2,2,-5,3,-4], [3,1,2,-2,-5,-4], [-2,3,-5,1,-4,2] are incorrect because they do not satisfy one or more conditions.

Example 2:
Input: nums = [-1,1]
Output: [1,-1]
Explanation:
1 is the only positive integer and -1 the only negative integer in nums.
So nums is rearranged to [1,-1].
"""

# Runtime 1159 ms Beats 61.93% of users with Python
# Memory 45.25 MB Beats 19.72% of users with Python

def rearrangeArray(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    ll = len(nums)
    pos_ = [i for i in nums if i> 0]
    neg_ = [i for i in nums if i< 0]
    return [pos_[i // 2] if i % 2 == 0 else neg_[i // 2] for i in range(ll)]
