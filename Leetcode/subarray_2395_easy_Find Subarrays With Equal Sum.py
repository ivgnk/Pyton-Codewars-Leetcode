"""
Done 03.09.2024. Topics: Array, Hash Table
2395. Find Subarrays With Equal Sum
https://leetcode.com/problems/find-subarrays-with-equal-sum/description/

Given a 0-indexed integer array nums, determine whether there exist
two subarrays of length 2 with equal sum.
Note that the two subarrays must begin at different indices.

Return true if these subarrays exist, and false otherwise.
A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
Input: nums = [4,2,4]
Output: true
Explanation: The subarrays with elements [4,2] and [2,4] have the same sum of 6.

Example 2:
Input: nums = [1,2,3,4,5]
Output: false
Explanation: No two subarrays of size 2 have the same sum.

Example 3:
Input: nums = [0,0,0]
Output: true
Explanation: The subarrays [nums[0],nums[1]] and [nums[1],nums[2]] have the same sum of 0.
Note that even though the subarrays have the same content, the two subarrays are considered different because they are in different positions in the original array.

Constraints:
2 <= nums.length <= 1000
-10**9 <= nums[i] <= 10**9

Hint 1
Use a counter to keep track of the subarray sums.
Hint 2
Use a hashset to check if any two sums are equal.

Solution
✏️ Easy Python 3 solution
Intuition
Prepare sums of pairs of numbers.
Approach
As you prepare, check the amounts for repetition.
"""

# Runtime 21 ms Beats 50.47%
# Memory 11.76 MB Beats 52.34%
# Runtime 20 ms Beats 59.81%
# Memory 11.96 MB Beats 5.61%
# Runtime 8 ms Beats 99.07%
# Memory 11.84 MB Beats 22.43%
def findSubarrays2(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    ll1 = len(nums) - 1
    data = []
    for i in range(ll1):
        data.append(sum(nums[i:i + 2]))
    data_set = set(data)
    return ll1 != len(data_set)

# Runtime 22 ms Beats 45.79%
# Memory 11.83 MB Beats 22.43%
def findSubarrays(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    ll1=len(nums)-1
    data = []
    for i in range(ll1):
        n = sum(nums[i:i+2])
        if n in data: return True
        else: data.append(n)
    data_set=set(data)
    return ll1!=len(data_set)

print(findSubarrays([4,2,4]))
print(findSubarrays([1,2,3,4,5]))
print(findSubarrays([0,0,0]))


# Time Complexity O(N)
# Space Complexity O(N)
# Python 3
# Runtime 41 ms Beats 54.26%
# Memory 16.72 MB Beats 19.69%
def findSubarrays(nums):
    ll1 = len(nums) - 1
    data = []
    for i in range(ll1):
        if (n := sum(nums[i:i + 2])) in data:
            return True
        else:
            data.append(n)
    data_set = set(data)
    return ll1 != len(data_set)