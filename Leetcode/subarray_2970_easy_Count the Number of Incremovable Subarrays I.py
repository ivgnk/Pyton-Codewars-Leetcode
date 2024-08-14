"""
14.08.2024.
2970. Count the Number of Incremovable Subarrays I
https://leetcode.com/problems/count-the-number-of-incremovable-subarrays-i/description/

You are given a 0-indexed array of positive integers nums.
A subarray of nums is called incremovable if nums becomes strictly increasing on removing the subarray.
For example, the subarray [3, 4] is an incremovable subarray of [5, 3, 4, 6, 7]
because removing this subarray changes the array
[5, 3, 4, 6, 7] to [5, 6, 7] which is strictly increasing.

Return the total number of incremovable subarrays of nums.

Note that an empty array is considered strictly increasing.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
Input: nums = [1,2,3,4]
Output: 10
Explanation: The 10 incremovable subarrays are: [1], [2], [3], [4], [1,2], [2,3], [3,4], [1,2,3], [2,3,4], and [1,2,3,4], because on removing any one of these subarrays nums becomes strictly increasing. Note that you cannot select an empty subarray.

Example 2:
Input: nums = [6,5,7,8]
Output: 7
Explanation: The 7 incremovable subarrays are: [5], [6], [5,7], [6,5], [5,7,8], [6,5,7] and [6,5,7,8].
It can be shown that there are only 7 incremovable subarrays in nums.

Example 3:
Input: nums = [8,7,6,6]
Output: 3
Explanation: The 3 incremovable subarrays are: [8,7,6], [7,6,6], and [8,7,6,6]. Note that [8,7] is not an incremovable subarray because after removing [8,7] nums becomes [6,6], which is sorted in ascending order but not strictly increasing.

Constraints:
1 <= nums.length <= 50
1 <= nums[i] <= 50

Hint 1
Use two loops to check all the subarrays.
"""

# Wrong Answer - 103 / 615 testcases passed
# nums = [4,2]  Output 2, Expected 3
def incremovableSubarrayCount3(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ll=len(nums); res=set()
    for i in range(ll):
        for j in range(i+1,ll+1):
            s=nums[i:j]
            if s==sorted(s):
                if len(set(s))==len(s):
                    res.add(tuple(s))
            else: break
    return len(res)

# Runtime 477 ms Beats 39.29%
# Memory 11.59 MB Beats 60.71%
# Dec 23, 2023
# https://leetcode.com/problems/count-the-number-of-incremovable-subarrays-i/solutions/4447281/easy-python-solution/
def incremovableSubarrayCount(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    print('\n     ',nums)
    count = 0; res=[]
    for i in range(len(nums)):
        for j in range(i + 1, len(nums) + 1):
            l = nums[:i] + nums[j:]
            if l == sorted(l) and len(l) == len(set(l)):
                count += 1
                res.append(l)
                # print(i,j,l)
    print(res)
    return count

# Runtime 446 ms Beats 46.43%
# Memory 11.68 MB Beats 39.29%
# https://leetcode.com/problems/count-the-number-of-incremovable-subarrays-i/solutions/5531576/python-solution/
# Jul 25, 2024
def incremovableSubarrayCount__(nums):
    count = 0
    res=[]
    for i in range(len(nums)):
        for j in range(i + 1, len(nums) + 1):
            sub = nums[:i] + nums[j:]

            if all(sub[k] < sub[k + 1] for k in range(len(sub) - 1)):
                count += 1
                res.append(sub)
    print(res)
    return count

# print('Example 1 ',incremovableSubarrayCount([1,2,3,4]),'\n')
print('Example 2 ',incremovableSubarrayCount([6,5,7,8]),'\n')
# Out: [[5, 7, 8], [7, 8], [8], [], [6, 7, 8], [6, 8], [6]]
# this: [5], [6], [5,7], [6,5], [5,7,8], [6,5,7] and [6,5,7,8]
# Out2 : [[5, 7, 8], [7, 8], [8], [], [6, 7, 8], [6, 8], [6]]
# print('Example 3 ',incremovableSubarrayCount([8,7,6,6]),'\n')
