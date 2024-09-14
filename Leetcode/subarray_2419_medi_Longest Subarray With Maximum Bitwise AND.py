"""
Done 14.09.2024. Topics: Array, Bit Manipulation
2419. Longest Subarray With Maximum Bitwise AND
https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/description/

You are given an integer array nums of size n.
Consider a non-empty subarray from nums that has the maximum possible bitwise AND.

In other words, let k be the maximum value of the bitwise AND of any subarray of nums.
Then, only subarrays with a bitwise AND equal to k should be considered.
Return the length of the longest such subarray.

The bitwise AND of an array is the bitwise AND of all the numbers in it.

A subarray is a contiguous sequence of elements within an array.

Example 1:
Input: nums = [1,2,3,3,2,2]
Output: 2
Explanation:
The maximum possible bitwise AND of a subarray is 3.
The longest subarray with that value is [3,3], so we return 2.

Example 2:
Input: nums = [1,2,3,4]
Output: 1
Explanation:
The maximum possible bitwise AND of a subarray is 4.
The longest subarray with that value is [4], so we return 1.

Constraints:
1 <= nums.length <= 105
1 <= nums[i] <= 106

Hint 1
Notice that the bitwise AND of two different numbers will always be strictly less than the maximum of those two numbers.
Hint 2
What does that tell us about the nature of the subarray that we should choose?

The maximum possible bitwise AND of a subarray you can find only in a subarray of the same number
https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/description/comments/2080718

Hint: Find out first that why this problem can be solved by finding the longest subarray with largest element.
https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/description/comments/2080902

"Find longest consecutive length of the maximum element of nums."
https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/description/comments/2195566
"""

# Runtime 1392 ms Beats 5.55%
# Memory 24.16 MB Beats 66.67%
def longestSubarray(nums):
    m, count, lst = max(nums), 0, []
    for i in nums:
        if i == m:
            count += 1
        else:
            lst.append(count)
            count = 0
    lst.append(count)
    return max(lst)

# Runtime 1406 ms Beats 5.55%
# Memory 23.44 MB Beats 72.22%
def longestSubarray4(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    mmax = max(nums); mmaxl = -1;  currl = 0
    for dat in nums:
        if dat == mmax:
            currl += 1
            mmaxl = max(mmaxl, currl)
        else:
            currl = 0
    return mmaxl

# Runtime 1368 ms Beats 5.55%
# Memory 24.39 MB Beats 50.00%
def longestSubarray2(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    mmax = max(nums); mmaxl = -1;  currl = 0
    for i in range(len(nums)):
        if nums[i] == mmax:
            currl += 1
        elif currl != 0:
            mmaxl = max(mmaxl, currl)
            currl = 0
    else: mmaxl = max(mmaxl, currl)
    return mmaxl

# Runtime 1397 ms Beats 5.55%
# Memory 24.29 MB Beats 61.11%
def longestSubarray3(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    mmax = max(nums)
    mmaxl = -1;  currl = 0
    for i in range(len(nums)):
        if nums[i] == mmax:
            currl += 1
        elif currl != 0:
            mmaxl = max(mmaxl, currl)
            currl = 0
    mmaxl = max(mmaxl, currl)
    return mmaxl


print(longestSubarray([1,2,3,3,2,2])) # 2
print(longestSubarray([1,2,3,4]))
