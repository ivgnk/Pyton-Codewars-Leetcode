"""
Done 17.09.2024. Topics: Array, Prefix Sum
303. Range Sum Query - Immutable
https://leetcode.com/problems/range-sum-query-immutable/description/

Given an integer array nums, handle multiple queries of the following type:
Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.

Implement the NumArray class:
NumArray(int[] nums) Initializes the object with the integer array nums.
int sumRange(int left, int right) Returns the sum of the elements of nums between indices
left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).

Example 1:
Input
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
Output
[null, 1, -1, -3]

Explanation
NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3


Constraints:
1 <= nums.length <= 104
-105 <= nums[i] <= 105
0 <= left <= right < nums.length
At most 10**4 calls will be made to sumRange.
"""

# Runtime 68 ms Beats 45.98%
# Memory 15.53 MB Beats 44.99%
# Runtime 56 ms Beats 63.75%
# Memory 15.56 MB Beats 44.99%
class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        # self.num=nums
        self.prf=nums
        for i in range(1,len(nums)):
            self.prf[i]=self.prf[i-1]+self.prf[i]

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        # print(self.prf)
        if left==0: return self.prf[right]
        else: return self.prf[right]-self.prf[left-1]


# Runtime 388 ms Beats 27.22%
# Memory 15.29 MB Beats 94.99%
class NumArray2(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.num = nums

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return sum(self.num[left:right + 1])

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)