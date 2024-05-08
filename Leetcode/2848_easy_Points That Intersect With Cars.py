"""
Done 09.05.2024. Array, Hash Table, Prefix Sum
2848. Points That Intersect With Cars
https://leetcode.com/problems/points-that-intersect-with-cars/description/

You are given a 0-indexed 2D integer array nums representing the coordinates of the cars parking on a number line.
For any index i, nums[i] = [starti, endi]
where starti is the starting point of the ith car and endi is the ending point of the ith car.
Return the number of integer points on the line that are covered with any part of a car.

Example 1:
Input: nums = [[3,6],[1,5],[4,7]]
Output: 7
Explanation: All the points from 1 to 7 intersect at least one car, therefore the answer would be 7.

Example 2:
Input: nums = [[1,3],[5,8]]
Output: 7
Explanation: Points intersecting at least one car are 1, 2, 3, 5, 6, 7, 8. There are a total of 7 points, therefore the answer would be 7.
"""

# Runtime 66 ms Beats 18.75% of users with Python
# Memory 11.68 MB Beats 57.29% of users with Python

def numberOfPoints2(nums):
    """
    :type nums: List[List[int]]
    :rtype: int
    """
    res= set([j for d in nums for j in range(d[0],d[1]+1)])
    print(res)
    return len(res)

# Runtime 51 ms Beats 88.54% of users with Python
# Memory 11.86 MB Beats 5.21% of users with Python
def numberOfPoints(nums):
    return len(set([j for d in nums for j in range(d[0], d[1] + 1)]))

print(numberOfPoints([[3,6],[1,5],[4,7]]))
