"""
10.12.2024.
3379. Transformed Array
https://leetcode.com/problems/transformed-array/description/

You are given an integer array nums that represents a circular array.
Your task is to create a new array result of the same size, following these rules:

For each index i (where 0 <= i < nums.length), perform the following independent actions:
If nums[i] > 0: Start at index i and move nums[i] steps to the right in the circular array.
Set result[i] to the value of the index where you land.

If nums[i] < 0: Start at index i and move abs(nums[i]) steps to the left in the circular array.
Set result[i] to the value of the index where you land.

If nums[i] == 0: Set result[i] to nums[i].
Return the new array result.

Note: Since nums is circular, moving past the last element wraps around to the beginning,
and moving before the first element wraps back to the end.

Example 1:
Input: nums = [3,-2,1,1]
Output: [1,1,1,3]
Explanation:
For nums[0] that is equal to 3, If we move 3 steps to right, we reach nums[3]. So result[0] should be 1.
For nums[1] that is equal to -2, If we move 2 steps to left, we reach nums[3]. So result[1] should be 1.
For nums[2] that is equal to 1, If we move 1 step to right, we reach nums[3]. So result[2] should be 1.
For nums[3] that is equal to 1, If we move 1 step to right, we reach nums[0]. So result[3] should be 3.

Example 2:
Input: nums = [-1,4,-1]
Output: [-1,-1,4]
Explanation:
For nums[0] that is equal to -1, If we move 1 step to left, we reach nums[2]. So result[0] should be -1.
For nums[1] that is equal to 4, If we move 4 steps to right, we reach nums[2]. So result[1] should be -1.
For nums[2] that is equal to -1, If we move 1 step to left, we reach nums[1]. So result[2] should be 4.

Constraints:
1 <= nums.length <= 100
-100 <= nums[i] <= 100

Hint 1
Simulate the operations as described in the statement
"""


def constructTransformedArray2(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    ll=len(nums)
    if ll == 1: return nums
    nn = max(map(abs,nums))
    print(nn)
    res=[0]*nn
    n1=nums*3
    for i in range(ll,ll*2,1):
        if i==0: res[i-ll]=nums[i-ll]
        else: res[i-ll]=n1[i+n1[i]]
    return res

# Runtime 40 ms Beats 100.00%
# Memory 12.17 MB Beats 100.00%
# Time Complexity O(N)
# Space Complexity O(N)
# https://leetcode.com/problems/transformed-array/solutions/6128157/python-code/
def constructTransformedArray(nums):
    result = []
    for i in range(len(nums)):
        if nums[i] == 0:
            out = nums[i]
        else:
            out = nums[(i + nums[i]) % len(nums)]
        result.append(out)
    return result


print(constructTransformedArray([3,-2,1,1]))

