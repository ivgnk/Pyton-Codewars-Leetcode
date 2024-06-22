"""
Done 22.06.2024. Topics: Array, Sorting

747. Largest Number At Least Twice of Others
https://leetcode.com/problems/largest-number-at-least-twice-of-others/description/

You are given an integer array nums where the largest integer is unique.
Determine whether the largest element in the array is at least twice as much as every other number in the array.
If it is, return the index of the largest element, or return -1 otherwise.

Example 1:
Input: nums = [3,6,1,0]
Output: 1
Explanation: 6 is the largest integer.
For every other number in the array x, 6 is at least twice as big as x.
The index of value 6 is 1, so we return 1.

Example 2:
Input: nums = [1,2,3,4]
Output: -1
Explanation: 4 is less than twice the value of 3, so we return -1.


Hint 1
Scan through the array to find the unique largest element `m`, keeping track of it's index `maxIndex`.
Scan through the array again. If we find some `x != m` with `m < 2*x`, we should return `-1`.
Otherwise, we should return `maxIndex`.
"""

# Runtime 19 ms Beats 44.42%
# Memory 11.58 MB Beats 61.76%
# Runtime 16 ms Beats 71.50%
# Memory 11.65 MB Beats 25.18%

def dominantIndex(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n1=sorted(nums,reverse=True)
    if n1[0]>=n1[1]*2:
        return nums.index(n1[0])
    else:
        return -1

print(dominantIndex([3,6,1,0]))
print(dominantIndex([1,2,3,4]))
