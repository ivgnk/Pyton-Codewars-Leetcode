"""
Done 03.05.2024
2190. Most Frequent Number Following Key In an Array
https://leetcode.com/problems/most-frequent-number-following-key-in-an-array/description/

You are given a 0-indexed integer array nums. You are also given an integer key, which is present in nums.
For every unique integer target in nums, count the number of times target immediately follows an occurrence of key in nums.
In other words, count the number of indices i such that:
0 <= i <= nums.length - 2,
nums[i] == key and,
nums[i + 1] == target.
Return the target with the maximum count. The test cases will be generated such that the target with maximum count is unique.

Example 1:
Input: nums = [1,100,200,1,100], key = 1
Output: 100
Explanation: For target = 100, there are 2 occurrences at indices 1 and 4 which follow an occurrence of key.
No other integers follow an occurrence of key, so we return 100.

Example 2:
Input: nums = [2,2,2,2,3], key = 2
Output: 2
Explanation: For target = 2, there are 3 occurrences at indices 1, 2, and 3 which follow an occurrence of key.
For target = 3, there is only one occurrence at index 4 which follows an occurrence of key.
target = 2 has the maximum number of occurrences following an occurrence of key, so we return 2.
"""

# Runtime 57 ms Beats 57.89% of users with Python
# Memory 11.92 MB Beats 13.16% of users with Python
# Runtime 55 ms Beats 68.42% of users with Python
# Memory 11.94 MB Beats 13.16% of users with Python
# Runtime 50 ms Beats 92.11% of users with Python
# Memory 11.97 MB Beats 13.16% of users with Python

from collections import Counter
def mostFrequent(nums, key):
    """
    :type nums: List[int]
    :type key: int
    :rtype: int
    """
    ln_ = len(nums)
    ind = [i for i in range(ln_) if nums[i] == key]
    nn=[nums[i+1] for i in ind if i+1<ln_]
    # if len(nn)==1: return nn[0]
    cnt = dict(Counter(nn))
    srt_cnt=sorted([[v,k] for k,v in cnt.items()])
    return srt_cnt[-1][1]

# print(mostFrequent(nums = [1,100,200,1,100], key = 1))
print(mostFrequent(nums = [2,2,2,2,3], key = 2))




