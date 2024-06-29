"""
Done 29.06.2024. Topics: Array, Hash Table
2913. Subarrays Distinct Element Sum of Squares I
https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-i/description/

You are given a 0-indexed integer array nums.
The distinct count of a subarray of nums is defined as:

Let nums[i..j] be a subarray of nums consisting of all the indices from i to j such that 0 <= i <= j < nums.length.
Then the number of distinct values in nums[i..j] is called the distinct count of nums[i..j].
Return the sum of the squares of distinct counts of all subarrays of nums.
A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
Input: nums = [1,2,1]
Output: 15
Explanation: Six possible subarrays are:
[1]: 1 distinct value
[2]: 1 distinct value
[1]: 1 distinct value
[1,2]: 2 distinct values
[2,1]: 2 distinct values
[1,2,1]: 2 distinct values
The sum of the squares of the distinct counts in all subarrays is equal to 12 + 12 + 12 + 22 + 22 + 22 = 15.

Example 2:
Input: nums = [1,1]
Output: 3
Explanation: Three possible subarrays are:
[1]: 1 distinct value
[1]: 1 distinct value
[1,1]: 1 distinct value
The sum of the squares of the distinct counts in all subarrays is equal to 12 + 12 + 12 = 3.

Constraints:
1 <= nums.length <= 100
1 <= nums[i] <= 100

Hint 1
Use a set/heap to keep track of distinct element counts.
"""

# Runtime 1328 ms Beats 5.08%
# Memory 11.67 MB Beats 52.54%
from collections import Counter
def sumCounts3(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ll=len(nums)
    ssum=0
    for i in range(ll):
        for j in range(i+1,ll+1):
            s=nums[i:j]
            dd=Counter(s)
            ssum = ssum+len(dd)**2
    return ssum

# Runtime 1305 ms Beats 5.08%
# Memory 11.74 MB Beats 28.81%
def sumCounts4(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ll = len(nums);    ll1 = ll + 1
    return sum([len(Counter(nums[i:j])) ** 2
                for i in range(ll)
                for j in range(i + 1, ll1)])

# Runtime 1283 ms Beats 5.08%
# Memory 11.49 MB Beats 94.92%
def sumCounts2(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ll = len(nums);    ll1 = ll + 1;    rll = range(ll)
    return sum([len(Counter(nums[i:j])) ** 2
                for i in rll
                for j in range(i + 1, ll1)])

# on the base
# https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-i/solutions/5257971/easy-solution-beats-66-using-set/
# Runtime 138 ms Beats 72.03%
# Memory 11.71 MB Beats 28.81%
# Runtime 129 ms Beats 76.27%
# Memory 11.74 MB Beats 28.81%
def sumCounts(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ll = len(nums);    ll1 = ll + 1;    rll = range(ll)
    return sum([len(set(nums[i:j]))** 2
                for i in rll
                for j in range(i + 1, ll1)])


print(sumCounts([1,2,1]))
print(sumCounts([1,1]))

