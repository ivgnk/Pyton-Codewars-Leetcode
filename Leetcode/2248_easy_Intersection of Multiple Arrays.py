"""
Done 28.04.2024
2248. Intersection of Multiple Arrays
https://leetcode.com/problems/intersection-of-multiple-arrays/description/

Given a 2D integer array nums where nums[i] is a non-empty array of distinct positive integers,
return the list of integers that are present in each array of nums sorted in ascending order.

Example 1:
Input: nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]
Output: [3,4]
Explanation:
The only integers present in each of nums[0] = [3,1,2,4,5], nums[1] = [1,2,3,4], and nums[2] = [3,4,5,6] are 3 and 4, so we return [3,4].

Example 2:
Input: nums = [[1,2,3],[4,5,6]]
Output: []
Explanation:
There does not exist any integer present both in nums[0] and nums[1], so we return an empty list [].
"""

# Runtime 38 ms Beats 91.91% of users with Python
# Memory 12.14 MB Beats 22.55% of users with Python

# www.geeksforgeeks.org/python-multiple-sets-intersection/
def intersection(nums):
    """
    :type nums: List[List[int]]
    :rtype: List[int]
    """
    lst = [set(row) for row in nums]
    return sorted(set.intersection(*lst))

print(intersection(nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]))