"""
25.07.2024. Topics: Array, Sorting

912. Sort an Array
https://leetcode.com/problems/sort-an-array

Given an array of integers nums, sort the array in ascending order and return it.

You must solve the problem without using any built-in functions in O(nlog(n))
time complexity and with the smallest space complexity possible.

Example 1:
Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3),
while the positions of other numbers are changed (for example, 1 and 5).

Example 2:
Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
Explanation: Note that the values of nums are not necessairly unique.

Constraints:
1 <= nums.length <= 5 * 10**4
-5 * 104 <= nums[i] <= 5 * 10**4
"""

# Runtime 540 ms Beats 98.72%
# Memory 20.10 MB Beats 72.02%
def sortArray(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    return sorted(nums)

import heapq
# Runtime 1353 ms Beats 74.89%
# Memory 21.86 MB Beats 19.79%
def sortArray3(nums):
    h = []
    for value in nums:
        heapq.heappush(h, value)
    return [heapq.heappop(h) for i in range(len(h))]

print(sortArray([5,1,1,2,0,0]))

# Output - [0,0,1,2,1,5], Expected - [0,0,1,1,2,5]
def sortArray2(nums):
    heapq.heapify(nums)
    return list(nums)

# Runtime 676 ms Beats 84.36%
# Memory 27.95 MB Beats 5.53%
def sortArray1(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    res = nums[:];    ll = len(nums)
    d = dict()
    for i in nums:
        if i in d:
            d[i] = d[i] + 1
        else:
            d[i] = 1

    sort_tuple = sorted(d.items(), key=lambda x: x[0])
    return [s[0] for s in sort_tuple for i in range(s[1])]

