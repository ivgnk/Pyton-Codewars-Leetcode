"""
Done 14.09.2024.
3285. Find Indices of Stable Mountains
https://leetcode.com/problems/find-indices-of-stable-mountains/

There are n mountains in a row, and each mountain has a height.
You are given an integer array height where height[i] represents the height of mountain i,
and an integer threshold.
A mountain is called stable if the mountain just before it (if it exists)
has a height strictly greater than threshold. Note that mountain 0 is not stable.

Return an array containing the indices of all stable mountains in any order.

Example 1:
Input: height = [1,2,3,4,5], threshold = 2
Output: [3,4]

Explanation:
Mountain 3 is stable because height[2] == 3 is greater than threshold == 2.
Mountain 4 is stable because height[3] == 4 is greater than threshold == 2.

Example 2:
Input: height = [10,1,10,1,10], threshold = 3
Output: [1,3]

Example 3:
Input: height = [10,1,10,1,10], threshold = 10
Output: []
"""

# Runtime 42 ms Beats 100.00%
# Memory 11.72 MB Beats 100.00%
# Time Complexity O(N)
# Space Complexity O(1)
def stableMountains(height, threshold):
    """
    :type height: List[int]
    :type threshold: int
    :rtype: List[int]
    """
    res=[]
    bef=False
    for i in range(len(height)):
        if bef:
            if height[i] > 0: res.append(i)
        if height[i]>threshold:
            bef = True
        else:
            bef = False
    return res

print(stableMountains(height = [1,2,3,4,5], threshold = 2)) # [3,4]
print(stableMountains(height = [10,1,10,1,10], threshold = 3))
print(stableMountains(height = [10,1,10,1,10], threshold = 10)) # []