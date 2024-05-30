"""
Done 30.05.2024. Topics: Array, Prefix Sum
724. Find Pivot Index
https://leetcode.com/problems/find-pivot-index/

Given an array of integers nums, calculate the pivot index of this array.
The pivot index is the index where the sum of all the numbers strictly to the left of the index
is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left.
This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1

Example 1:
Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11

Example 2:
Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.

Example 3:
Input: nums = [2,1,-1]
Output: 0
Explanation:
The pivot index is 0.
Left sum = 0 (no elements to the left of index 0)
Right sum = nums[1] + nums[2] = 1 + -1 = 0

Hint 1
Create an array sumLeft where sumLeft[i] is the sum of all the numbers to the left of index i.
Hint 2
Create an array sumRight where sumRight[i] is the sum of all the numbers to the right of index i.
Hint 3
For each index i, check if sumLeft[i] equals sumRight[i] return i. If no i found, return -1.
"""

# Runtime 1174 ms Beats 19.05% of users with Python
# Memory 12.89 MB Beats 35.74% of users with Python
def pivotIndex2(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ssum = sum(nums)
    for i in range(len(nums)):
        left = sum(nums[:i])
        if ssum - nums[i] == 2 * left:
            return i
    return -1


# https://leetcode.com/problems/find-pivot-index/solutions/2321669/python-99-85-faster-simplest-solution-with-explanation-beg-to-adv-prefix-sum/
# Runtime 102 ms Beats 80.86% of users with Python
# Memory 12.70 MB Beats 90.24% of users with Python

def pivotIndex(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    left = 0
    right = sum(nums)

    for i, num in enumerate(nums):
        right -= num
        if left == right:
            return i
        left += num
    return -1

print(pivotIndex([1,7,3,6,5,6]))



