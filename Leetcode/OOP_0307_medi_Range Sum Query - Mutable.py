"""
Done 17.09.2024. Topics: Binary Indexed Tree, Segment Tree
307. Range Sum Query - Mutable
https://leetcode.com/problems/range-sum-query-mutable/description/

Given an integer array nums, handle multiple queries of the following types:
Update the value of an element in nums.
Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
void update(int index, int val) Updates the value of nums[index] to be val.
int sumRange(int left, int right) Returns the sum of the elements of nums
between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).

Example 1:

Input
["NumArray", "sumRange", "update", "sumRange"]
[[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
Output
[null, 9, null, 8]
Explanation
NumArray numArray = new NumArray([1, 3, 5]);
numArray.sumRange(0, 2); // return 1 + 3 + 5 = 9
numArray.update(1, 2);   // nums = [1, 2, 5]
numArray.sumRange(0, 2); // return 1 + 2 + 5 = 8


Constraints:
1 <= nums.length <= 3 * 104
-100 <= nums[i] <= 100
0 <= index < nums.length
-100 <= val <= 100
0 <= left <= right < nums.length
At most 3 * 104 calls will be made to update and sumRange.
"""
# Runtime 3057 ms Beats 7.89%
# Memory 29.80 MB Beats 100.00%

class NumArray(object):
    def __init__(self, nums):
        self.nums = nums
        self.n = len(nums)
        self.s = sum(nums)

    def update(self, index, val):
        self.s = self.s - self.nums[index] + val
        self.nums[index] = val

    def sumRange(self, left, right):
        r = self.s - sum(self.nums[:left]) - sum(self.nums[right + 1:])
        return r


from copy import copy
# Time Limit Exceeded - 9 / 16 testcases passed
class NumArray3(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.ll=len(nums)
        self.num=nums
        self.prf=copy(nums)
        for i in range(1,self.ll):
            self.prf[i]=self.prf[i-1]+self.prf[i]

    def update(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        prev=self.num[index]
        self.num[index]=val; diff=-prev+val
        for i in range(index,self.ll):
            self.prf[i]=self.prf[i]+diff

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        if left==0: return self.prf[right]
        else: return self.prf[right]-self.prf[left-1]

#################################################################################
# Time Limit Exceeded - 13 / 16 testcases passed
class NumArray2(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.prf = nums

    def update(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        self.prf[index] = val

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return sum(self.prf[left:right + 1])

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)

lsr=[1,2,3]
lst=lsr.copy()
lst[0]=0
print(lsr,lst)