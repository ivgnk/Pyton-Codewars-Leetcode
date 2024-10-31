"""
31.10.2024. Array, Binary Search, Dynamic Programming, Greedy
1671. Minimum Number of Removals to Make Mountain Array
https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array/description/

You may recall that an array arr is a mountain array if and only if:

arr.length >= 3
There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
Given an integer array nums, return the minimum number of elements to remove
to make nums a mountain array.

Example 1:
Input: nums = [1,3,1]
Output: 0
Explanation: The array itself is a mountain array so we do not need to remove any elements.

Example 2:
Input: nums = [2,1,1,5,6,2,3,1]
Output: 3
Explanation: One solution is to remove the elements at indices 0, 1, and 5, making the array nums = [1,5,6,3,1].

Constraints:
3 <= nums.length <= 1000
1 <= nums[i] <= 109
It is guaranteed that you can make a mountain array out of nums.

Hint 1
Think the opposite direction instead of minimum elements to remove the maximum mountain subsequence
Hint 2
Think of LIS it's kind of close

Tips from discussion
a=Find longest increasing subsequence
x=Find longest decreasing subsequence

ans=number of elements in vector - (a+x-1)
a+x-1 = gives maximum length of bitonic array we want to find minimum nmumber of removals ,
so we can subtract maximum length from the size of the vector to get the number of removals.
https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array/description/comments/1574814

main algo
https://www.geeksforgeeks.org/longest-increasing-subsequence-dp-3/
https://www.geeksforgeeks.org/longest-monotonically-increasing-subsequence-size-n-log-n/
https://en.wikipedia.org/wiki/Longest_increasing_subsequence
"""
from typing import List

# https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array/solutions/5984651/a-throught-way-of-tackling-this-problem/
class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        # Combination of Longest Increasing Subsequence and Trapping Rain Water
        leftDP, rightDP = [1] * len(nums), [1] * len(nums)
        # Find LIS from left
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    leftDP[i] = max(leftDP[i], leftDP[j] + 1)
        # Find LIS from right
        for i in range(len(nums) - 1, -1, -1):
            for j in range(len(nums) - 1, i, -1):
                if nums[i] > nums[j]:
                    rightDP[i] = max(rightDP[i], rightDP[j] + 1)
        # Find largest mountain by finding largest sum
        ans = 0
        for i in range(len(nums)):
            # Make sure there is a left and right slope, or else it's not a mountain
            if (leftDP[i] != 1 and rightDP[i] != 1):
                ans = max(ans, leftDP[i] + rightDP[i])
        ''' Debugging purposes
        for i in leftDP:
            print(i)
        print("RIGHT")
        for j in rightDP:
            print(j)
        '''
        # Return the number of numbers to remove to form the mountain
        return len(nums) - ans + 1


# Wrong Answer - 11 / 90 testcases passed
class Solution:
    def LIS_Bottom_Up_Tabulation(self, arr):
        n = len(arr)
        # Declare the list (array) for LIS and
        # initialize LIS values for all indexes
        lis = [1] * n

        # Compute optimized LIS values in bottom
        # -up manner
        for i in range(1, n):
            for prev in range(0, i):
                if arr[i] > arr[prev]:
                    lis[i] = max(lis[i], lis[prev] + 1)

        # Return the maximum of all LIS values
        return max(lis)

    def LDS_Bottom_Up_Tabulation(self,arr):
        n = len(arr)
        lds = [1] * n

        for i in range(1, n):
            for prev in range(0, i):
                if arr[i] < arr[prev]:
                    lds[i] = max(lds[i], lds[prev] + 1)
        # Return the maximum of all LIS values
        return max(lds)

    def minimumMountainRemovals(self, nums: List[int]) -> int:
        # a=Find longest increasing subsequence
        # x=Find longest decreasing subsequence
        # ans=number of elements in vector - (a+x-1)
        return len(nums)-(self.LDS_Bottom_Up_Tabulation(nums)+self.LDS_Bottom_Up_Tabulation(nums)-1)





