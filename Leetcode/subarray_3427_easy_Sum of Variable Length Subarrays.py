"""
Done 21.01.2025. Topics: Prefix Sum
3427. Sum of Variable Length Subarrays
https://leetcode.com/problems/sum-of-variable-length-subarrays/description/

You are given an integer array nums of size n.
For each index i where 0 <= i < n,
define a subarray nums[start ... i] where start = max(0, i - nums[i]).

Return the total sum of all elements from the subarray defined for each index in the array.

Example 1:
Input: nums = [2,3,1]
Output: 11
Explanation:
i	Subarray	Sum
0	nums[0] = [2]	2
1	nums[0 ... 1] = [2, 3]	5
2	nums[1 ... 2] = [3, 1]	4
Total Sum	 	11
The total sum is 11. Hence, 11 is the output.

Example 2:
Input: nums = [3,1,1,2]
Output: 13
Explanation:
i	Subarray	Sum
0	nums[0] = [3]	3
1	nums[0 ... 1] = [3, 1]	4
2	nums[1 ... 2] = [1, 1]	2
3	nums[1 ... 3] = [1, 1, 2]	4
Total Sum	 	13
The total sum is 13. Hence, 13 is the output.

Constraints:
1 <= n == nums.length <= 100
1 <= nums[i] <= 1000

Hint 1
The constraints are small, so brute force for each index.

My problem solution:
✏️ Easy, fast (7 ms), brute force Python solution for Problem 3427
https://leetcode.com/problems/sum-of-variable-length-subarrays/solutions/6310306/easy-fast-7-ms-brute-force-python-soluti-v9ei/
"""

# Runtime 8 ms Beats 57.88%
# Memory 12.37 MB Beats 89.15%
# Runtime 7 ms Beats 76.49%
# Memory 12.28 MB Beats 99.74%
# Time Complexity O(N**2)
# Space Complexity O(1)

def subarraySum(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ssum=0
    for i,dat in enumerate(nums):
        start = max(0, i - dat)
        ssum+=sum(nums[start:i+1])
    return ssum

print(subarraySum([2,3,1]))