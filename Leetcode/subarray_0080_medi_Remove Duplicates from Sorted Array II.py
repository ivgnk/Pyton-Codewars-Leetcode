"""
Done 19.08.2024. Topics: Array, Hash table
80. Remove Duplicates from Sorted Array II
Given an integer array nums sorted in non-decreasing order,
remove some duplicates in-place such that each unique element appears at most twice.
The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages,
you must instead have the result be placed in the first part of the array nums.
More formally, if there are k elements after removing the duplicates,
then the first k elements of nums should hold the final result.
It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying
the input array in-place with O(1) extra memory.

Example 1:
Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

Example 2:
Input: nums = [0,0,1,1,1,1,2,3,3]
Output: 7, nums = [0,0,1,1,2,3,3,_,_]
Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

Constraints:
1 <= nums.length <= 3 * 10**4
-104 <= nums[i] <= 10**4
nums is sorted in non-decreasing order.

Solutions
✏️ Easy Python solution without Two Pointers

Intuition
Use dictionary, not use Two Pointers.

Approach
Use dictionary.
Delete the last cells of the array with unnecessary characters
Done 19.08.2024.
Runtime 43 ms Beats 94.21%
Memory 16.55 MB Beats 47.24%
"""

# Runtime 43 ms Beats 94.21%
# Memory 16.55 MB Beats 47.24%

def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ll = len(nums)
    dd=dict()
    for i in nums:
        if i in dd: dd[i] +=1
        else: dd[i] = 1
    i=0
    for k,v in dd.items():
        if v>2: v=2
        for j in range(v):
           nums[i]=k
           i +=1
    for j in range(ll-i):
        nums.pop()
    # return nums

print(removeDuplicates([1,1,1,2,2,3]))
print(removeDuplicates([-1,0,0,0,0,3,3]))
