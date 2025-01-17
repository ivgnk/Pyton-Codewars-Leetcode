"""
17.01.2024. Topics: Two Pointers, Dynamic Programming, Stack, Monotonic Stack
42. Trapping Rain Water
https://leetcode.com/problems/trapping-rain-water/description/

Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9

Constraints:
n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105
"""

# Runtime 8 ms Beats 81.23%
# Memory 19.34 MB Beats 23.05%
# https://leetcode.com/problems/trapping-rain-water/solutions/6291036/trapping-rain-water-problem-solution-by-d6n27/

def trap(height):
    left = 0
    right = len(height) - 1

    left_max = height[left]
    right_max = height[right]
    water = 0

    while left < right:
        if left_max < right_max:
            left += 1
            left_max = max(left_max, height[left])
            water += left_max - height[left]
        else:
            right -= 1
            right_max = max(right_max, height[right])
            water += right_max - height[right]

    return water