"""
Done 18.08.2024. Topics: Array
2855. Minimum Right Shifts to Sort the Array
https://leetcode.com/problems/minimum-right-shifts-to-sort-the-array/description/

You are given a 0-indexed array nums of length n containing distinct positive integers.
Return the minimum number of right shifts required to sort nums and -1 if this is not possible.
A right shift is defined as shifting the element at index i to index (i + 1) % n, for all indices.

Example 1:
Input: nums = [3,4,5,1,2]
Output: 2
Explanation:
After the first right shift, nums = [2,3,4,5,1].
After the second right shift, nums = [1,2,3,4,5].
Now nums is sorted; therefore the answer is 2.

Example 2:
Input: nums = [1,3,5]
Output: 0
Explanation: nums is already sorted therefore, the answer is 0.

Example 3:
Input: nums = [2,1,4]
Output: -1
Explanation: It's impossible to sort the array using right shifts.

Constraints:
1 <= nums.length <= 100
1 <= nums[i] <= 100
nums contains distinct integers.

Hint 1
Find the pivot point around which the array is rotated.
Hint 2
Will the answer exist if there is more than one point where nums[i] < nums[i-1]

Solution
✏️ Easy Python solution
Intuition
Consider different cases of order in the array.
Approach
Cases
1) Sorted array.
2) An array in which the maximum is at the end. I.e., the array no longer needs to be shifted.
3) An array in which the maximum number is not on the edges.
If you divide this array by 2, and then connect it so that the maximum is at the end,
then if this new array is equal to the detached one, then calculate the number of shifts.
Otherwise -1.
"""

# Runtime 39 ms Beats 92.86%
# Memory 16.54 MB Beats 42.31%
def minimumRightShifts(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ns=sorted(nums)
    if ns==nums: return 0
    mmax=max(nums)
    if nums[-1]==(mmax): return -1
    ind=nums.index(mmax)
    p1=nums[:ind+1]
    p2=nums[ind+1:]
    if ns==p2+p1: return len(nums) - ind-1
    else: return -1

# print(minimumRightShifts([3,4,5,1,2]))
# print(minimumRightShifts([1,3,5]))
# print(minimumRightShifts([2,1,4]))
print(minimumRightShifts([63,51,65,87,6,17,32,14,42,46]))