"""
Done 26.01.2025
3432. Count Partitions with Even Sum Difference
https://leetcode.com/problems/count-partitions-with-even-sum-difference

You are given an integer array nums of length n.

A partition is defined as an index i where 0 <= i < n - 1,
splitting the array into two non-empty subarrays such that:

Left subarray contains indices [0, i].
Right subarray contains indices [i + 1, n - 1].
Return the number of partitions where the difference between the sum of the left and right
subarrays is even.

Example 1:
Input: nums = [10,10,3,7,6]
Output: 4
Explanation:
The 4 partitions are:
[10], [10, 3, 7, 6] with a sum difference of 10 - 26 = -16, which is even.
[10, 10], [3, 7, 6] with a sum difference of 20 - 16 = 4, which is even.
[10, 10, 3], [7, 6] with a sum difference of 23 - 13 = 10, which is even.
[10, 10, 3, 7], [6] with a sum difference of 30 - 6 = 24, which is even.

Example 2:
Input: nums = [1,2,2]
Output: 0
Explanation:
No partition results in an even sum difference.

Example 3:
Input: nums = [2,4,6,8]
Output: 3
Explanation:
All partitions result in an even sum difference.

Constraints:
2 <= n == nums.length <= 100
1 <= nums[i] <= 100

Hint 1
If the parity of the sum is even, the partition is valid;
otherwise, there is no partition.

Tip: Difference of two nos. can be even only when both are even or both are odd.
https://leetcode.com/problems/count-partitions-with-even-sum-difference/description/comments/2824515

Beware of the partition, it's a non empty sub array.
https://leetcode.com/problems/count-partitions-with-even-sum-difference/description/comments/2824342

My Solution https://leetcode.com/problems/count-partitions-with-even-sum-difference/solutions/6332689/easy-and-fast-0-ms-python-solution-for-p-sxnh/
Easy and fast (0 ms) Python solution for Problem 3432 used tip
"""

# Runtime 0 ms Beats 100.00%
# Memory 12.53 MB Beats 100.00%
# Time Complexity O(N)
# Space Complexity O(1)

def countPartitions(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ssum=sum(nums); nn=0
    left=nums[0]
    for i in range(1,len(nums)):
        right=ssum-left
        lb=left%2==0
        rb=right%2==0
        if lb==rb: nn+=1
        left+=nums[i]
    return nn

print(countPartitions([10,10,3,7,6]))
print(countPartitions([1,2,2]))
print(countPartitions([2,4,6,8]))