"""
Done 06.03.2025.
3467. Transform Array by Parity
https://leetcode.com/problems/transform-array-by-parity/description/

You are given an integer array nums.
Transform nums by performing the following operations in the exact order specified:
Replace each even number with 0.
Replace each odd numbers with 1.
Sort the modified array in non-decreasing order.
Return the resulting array after performing these operations.

Example 1:
Input: nums = [4,3,2,1]
Output: [0,0,1,1]
Explanation:
Replace the even numbers (4 and 2) with 0 and the odd numbers (3 and 1) with 1. Now, nums = [0, 1, 0, 1].
After sorting nums in non-descending order, nums = [0, 0, 1, 1].

Example 2:
Input: nums = [1,5,1,4,2]
Output: [0,0,1,1,1]

Explanation:
Replace the even numbers (4 and 2) with 0 and the odd numbers (1, 5 and 1) with 1. Now, nums = [1, 1, 1, 0, 0].
After sorting nums in non-descending order, nums = [0, 0, 1, 1, 1].

Constraints:
1 <= nums.length <= 100
1 <= nums[i] <= 1000

Hint 1
Let x be the number of even numbers, and y be the number of odd numbers.
Output 0 x times, followed by 1 y times.

My solution
Easy Python solution for Problem 3467
https://leetcode.com/problems/transform-array-by-parity/solutions/6501964/easy-python-solution-for-problem-346-by-y36l4/

Intuition
Use Hint1 in Problem:
Let x be the number of even numbers, and y be the number of odd numbers.
Output 0 x times, followed by 1 y times.
"""
# Time Complexity O(N)
# Space Complexity O(1)
# Runtime 0 ms Beats 100.00%
# Memory 12.49 MB Beats 51.34%
def transformArray(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    x, y =0, 0
    for n in nums:
        if n%2==0:
            x+=1
        else:
            y += 1
    return [0]*x+[1]*y

print(transformArray([4,3,2,1]))
print(transformArray([1,5,1,4,2]))
