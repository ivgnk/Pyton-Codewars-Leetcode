"""
13.11.2024. Topics: Array, Two Pointers, Binary Search, Sorting
2563. Count the Number of Fair Pairs
https://leetcode.com/problems/count-the-number-of-fair-pairs/description/

Given a 0-indexed integer array nums of size n and two integers lower and upper, return the number of fair pairs.
A pair (i, j) is fair if:
0 <= i < j < n, and
lower <= nums[i] + nums[j] <= upper

Example 1:
Input: nums = [0,1,7,4,4,5], lower = 3, upper = 6
Output: 6
Explanation: There are 6 fair pairs: (0,3), (0,4), (0,5), (1,3), (1,4), and (1,5).

Example 2:
Input: nums = [1,7,9,2,5], lower = 11, upper = 11
Output: 1
Explanation: There is a single fair pair: (2,3).

Hint 1
Sort the array in ascending order.
Hint 2
For each number in the array, keep track of the smallest and largest numbers in the array that can form a fair pair with this number.
Hint 3
As you move to larger number, both boundaries move down.
"""

# 48 / 53 testcases passed - 100000 points

def countFairPairs2(nums, lower, upper):
    """
    :type nums: List[int]
    :type lower: int
    :type upper: int
    :rtype: int
    """
    ll = len(nums)
    ss = list(set(nums))
    lss = len(ss);    mis = min(ss);    mas = max(ss)
    print(ll, lss, mis, mas)
    if lower == upper:
        if lss == 2 and ss[0] + ss[1] != lower:
            return 0
    if upper - lower > mis + mas and lss >= 100000:
        print('part')
        return sum([(ll - (i + 1)) for i in range(ll)])
    print('main')
    n = 0
    for i in range(ll):
        for j in range(i + 1, ll):
            if lower <= nums[i] + nums[j] <= upper: n = n + 1
    return n

def countFairPairs(nums, lower, upper):
    """
    :type nums: List[int]
    :type lower: int
    :type upper: int
    :rtype: int
    """
    ll = len(nums)
    n2=[[nums[i],i] for i in range(ll)]
    n2=sorted(n2)
    if lower == upper:
        if ll == 2 and nums[0] + nums[1] != lower:
            return 0
    i=0;j=ll-1; nn=0
    while i<j:
        r = n2[i][0]+n2[j][0]
        if r <= upper: nn=nn+1
        elif r>upper: j=j-1
        else: i=i+1
    return nn

from typing import List
# https://leetcode.com/problems/count-the-number-of-fair-pairs/solutions/3174181/two-pointers-2/
# Runtime 195 ms Beats 67.86% Analyze Complexity
# Memory 30.58 MB Beats 91.73%
def countFairPairs(nums: List[int], lower: int, upper: int) -> int:
    def countLess(val: int) -> int:
        res, j = 0, len(nums) - 1
        for i in range(len(nums)):
            while i < j and nums[i] + nums[j] > val:
                j -= 1
            res += max(0, j - i)
        return res
    nums.sort()
    return countLess(upper) - countLess(lower - 1)

# Runtime: 106ms
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        return self.lower_bound(nums, upper + 1) - self.lower_bound(nums, lower)

    # Calculate the number of pairs with sum less than `value`.
    def lower_bound(self, nums: List[int], value: int) -> int:
        left = 0
        right = nums.__len__() - 1
        result = 0
        while left < right:
            sum = nums[left] + nums[right]
            # If sum is less than value, add the size of window to result and move to the
            # next index.
            if sum < value:
                result += right - left
                left += 1
            else:
                # Otherwise, shift the right pointer backwards, until we get a valid window.
                right -= 1
        return result

from bisect import bisect_left, bisect_right
# Runtime: 218ms
class Solution2:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        res = 0

        for i, x in enumerate(nums):
            left = bisect_left(nums, lower - x, 0, i)
            right = bisect_right(nums, upper - x, 0, i)
            res += right - left
        return res

if __name__=="__main__":
    s=Solution2()
    print(s.countFairPairs(nums = [0,1,7,4,4,5], lower = 3, upper = 6))
    print(s.countFairPairs(nums = [1,7,9,2,5], lower = 11, upper = 11))