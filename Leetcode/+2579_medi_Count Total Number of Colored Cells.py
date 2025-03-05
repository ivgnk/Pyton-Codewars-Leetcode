"""
05.03.2025. Topics: Math
2579. Count Total Number of Colored Cells
https://leetcode.com/problems/count-total-number-of-colored-cells

There exists an infinitely large two-dimensional grid of uncolored unit cells. You are given a positive integer n, indicating that you must do the following routine for n minutes:

At the first minute, color any arbitrary unit cell blue.
Every minute thereafter, color blue every uncolored cell that touches a blue cell.
Below is a pictorial representation of the state of the grid after minutes 1, 2, and 3.

Example 1:

Input: n = 1
Output: 1
Explanation: After 1 minute, there is only 1 blue cell, so we return 1.
Example 2:

Input: n = 2
Output: 5
Explanation: After 2 minutes, there are 4 colored cells on the boundary and 1 in the center, so we return 5.


Constraints:
1 <= n <= 10**5

Hint 1
Derive a mathematical relation between total number of colored cells and the time elapsed in minutes.
"""

# Runtime 0 ms Beats 100.00%
# Memory 12.44 MB Beats 61.54%

# https://leetcode.com/problems/count-total-number-of-colored-cells/description/comments/1821581/
def coloredCells(n):
    """
    :type n: int
    :rtype: int
    """
    return n * n + (n - 1) * (n - 1)
