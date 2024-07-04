"""
Done 04.07.2024. Topics: Array, Sorting
2740. Find the Value of the Partition
https://leetcode.com/problems/find-the-value-of-the-partition/description/

You are given a positive integer array nums.
Partition nums into two arrays, nums1 and nums2, such that:

Each element of the array nums belongs to either the array nums1 or the array nums2.
Both arrays are non-empty.
The value of the partition is minimized.
The value of the partition is |max(nums1) - min(nums2)|.

Here, max(nums1) denotes the maximum element of the array nums1,
and min(nums2) denotes the minimum element of the array nums2.

Return the integer denoting the value of such partition.

Example 1:
Input: nums = [1,3,2,4]
Output: 1
Explanation: We can partition the array nums into nums1 = [1,2] and nums2 = [3,4].
- The maximum element of the array nums1 is equal to 2.
- The minimum element of the array nums2 is equal to 3.
The value of the partition is |2 - 3| = 1.
It can be proven that 1 is the minimum value out of all partitions.

Example 2:
Input: nums = [100,1,10]
Output: 9
Explanation: We can partition the array nums into nums1 = [10] and nums2 = [100,1].
- The maximum element of the array nums1 is equal to 10.
- The minimum element of the array nums2 is equal to 1.
The value of the partition is |10 - 1| = 9.
It can be proven that 9 is the minimum value out of all partitions.

Hint 1
Sort the array.
Hint 2
The answer is min(nums[i+1] - nums[i]) for all i in the range [0, n-2].

Constraints:
2 <= nums.length <= 105
1 <= nums[i] <= 109
"""

# Runtime 384 ms Beats 29.63%
# Memory 23.23 MB Beats 51.85%
def findValueOfPartition2(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    mmin=10_000_000_000
    nums.sort()
    for i in range(len(nums)-1):
        mmin=min(mmin,nums[i+1] - nums[i])
    return mmin

# Runtime 368 ms Beats 70.37%
# Memory 23.86 MB# Beats 7.41%
def findValueOfPartition(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    mmin=10_000_000_000
    nums.sort()
    lst=[nums[i+1] - nums[i] for i in range(len(nums)-1)]
    return min(lst)

print(findValueOfPartition([1,3,2,4]))
print(findValueOfPartition([100,1,10]))
    




