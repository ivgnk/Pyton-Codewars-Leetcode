"""
Done 17.09.2024. Topics: Math
365. Water and Jug Problem

You are given two jugs with capacities x liters and y liters.
You have an infinite water supply.
Return whether the total amount of water in both jugs may reach target using
the following operations:

Fill either jug completely with water.
Completely empty either jug.
Pour water from one jug into another until the receiving jug is full,
or the transferring jug is empty.

Example 1:
Input: x = 3, y = 5, target = 4
Output: true
Explanation:
Follow these steps to reach a total of 4 liters:

Fill the 5-liter jug (0, 5).
Pour from the 5-liter jug into the 3-liter jug, leaving 2 liters (3, 2).
Empty the 3-liter jug (0, 2).
Transfer the 2 liters from the 5-liter jug to the 3-liter jug (2, 0).
Fill the 5-liter jug again (2, 5).
Pour from the 5-liter jug into the 3-liter jug until the 3-liter jug is full.
This leaves 4 liters in the 5-liter jug (3, 4).
Empty the 3-liter jug. Now, you have exactly 4 liters in the 5-liter jug (0, 4).
Reference: The Die Hard example.

Example 2:
Input: x = 2, y = 6, target = 5
Output: false

Example 3:
Input: x = 1, y = 2, target = 3
Output: true

Explanation: Fill both jugs. The total amount of water in both jugs is equal to 3 now.

Constraints:
1 <= x, y, target <= 10**3

Tip 1
https://leetcode.com/problems/water-and-jug-problem/description/comments/1564956
Bezout's Lemma states that if x and y are nonzero integers and g = gcd(x,y),
then there exist integers a and b such that ax+by=g.
In other words, there exists a linear combination of x and y equal to g.

Furthermore, g is the smallest positive integer that can be expressed in this form,
i.e. g = min{ax+by | a, b in Z, ax+by > 0}.

Tip 2
https://leetcode.com/problems/water-and-jug-problem/description/comments/1572064
case 1,1,12 should be true as with jug size 1 , we can fill any size jug.
pl comment
You cannot store 12 litres of water in 2 jugs of 1 litre capacity
"""

import math
# Runtime 28 ms Beats 92.59%
# Memory 16.52 MB Beats 53.44%
def canMeasureWater(x: int, y: int, target: int) -> bool:
    if x + y < target: return False
    r = math.gcd(x, y)
    return target % r == 0





