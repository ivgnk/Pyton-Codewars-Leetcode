"""
Done 08.06.2024. Topics: Array, Two Pointers, Binary Search
167. Two Sum II - Input Array Is Sorted
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
find two numbers such that they add up to a specific target number.
Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
The tests are generated such that there is exactly one solution. You may not use the same element twice.
Your solution must use only constant extra space.

Example 1:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

Example 2:
Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

Example 3:
Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].

as hint:
The two pointer method seems pretty straight forward.
Increase L if sum is smaller, decrease R if sum is larger.
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/comments/1568755
"""

# Runtime 81 ms Beats 93.28% of users with Python
# Memory 12.42 MB Beats 68.93% of users with Python
def twoSum(numbers, target):
    ll=len(numbers)
    i=0; j=ll-1
    while i<j:
        n = numbers[i]+numbers[j]
        if n==target:
            return [i+1,j+1]
        elif n>target:
            j=j-1
        else: i=i+1




# Time Limit Exceeded --18 / 23 testcases passed
# ll=26020
def twoSum2(numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    ll=len(numbers)
    for i in range(ll):
        for j in range(i+1,ll):
            if numbers[i]+numbers[j]==target:
                return [i+1,j+1]

