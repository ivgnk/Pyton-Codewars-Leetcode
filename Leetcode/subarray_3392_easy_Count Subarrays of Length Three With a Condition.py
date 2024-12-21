"""
Done 21.12.2024
3392. Count Subarrays of Length Three With a Condition

Given an integer array nums, return the number of subarrays of length 3
such that the sum of the first and third numbers equals exactly
half of the second number.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
Input: nums = [1,2,1,4,1]
Output: 1
Explanation:
Only the subarray [1,4,1] contains exactly 3 elements where the sum of the first and third numbers equals half the middle number.

Example 2:
Input: nums = [1,1,1]
Output: 0
Explanation:
[1,1,1] is the only subarray of length 3.
However, its first and third numbers do not add to half the middle number.

Constraints:
3 <= nums.length <= 100
-100 <= nums[i] <= 100

Hint 1
The constraints are small. Consider checking every subarray.

My solution https://leetcode.com/problems/count-subarrays-of-length-three-with-a-condition/solutions/6171947/easy-and-fast-4-ms-python-solution-for-p-b74o/
✏️ Easy and fast (4 ms) Python solution for Problem 3392
"""

def countSubarrays2(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ll=len(nums); n=0
    half=[nums[i]/2 for i in range(ll)]
    for i in range(ll-2):
        n+=(nums[i]+nums[i+2])==half[i+1]
    return n

# Runtime 4 ms Beats 100.00%
# Memory 17.70 MB Beats 100.00%
# Time Complexity O(N)
# Space Complexity O(N)
def countSubarrays(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ll=len(nums)
    half=[nums[i]/2 for i in range(ll)]
    return sum((nums[i]+nums[i+2])==half[i+1] for i in range(ll-2))

if __name__=="__main__":
    # print(countSubarrays([1,2,1,4,1]))
    # print(countSubarrays([1,1,1]))
    print(countSubarrays([2,-7,-6]))