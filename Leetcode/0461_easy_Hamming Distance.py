"""
Done 03.05.2024
461. Hamming Distance
https://leetcode.com/problems/hamming-distance/description/

The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
Given two integers x and y, return the Hamming distance between them.

Example 1:
Input: x = 1, y = 4
Output: 2
Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
The above arrows point to positions where the corresponding bits are different.
Example 2:

Input: x = 3, y = 1
Output: 1
"""

# Runtime 15 ms Beats 43.75% of users with Python
# Memory 11.60 MB Beats 42.19% of users with Python
# Runtime 14 ms Beats 50.63% of users with Python
# Memory 11.70 MB Beats 42.19% of users with Python

def hammingDistance(x, y):
    """
    :type x: int
    :type y: int
    :rtype: int
    """
    xb=bin(x)[2:]; yb=bin(y)[2:]
    lxb=len(xb); lyb=len(yb)
    ll=max(lxb,lyb)
    if lxb < ll: xb='0'*(ll-lxb)+xb
    if lyb < ll: yb='0'*(ll-lyb)+yb
    return sum([1 for i in range(ll) if xb[i] != yb[i]])

print(hammingDistance(1,4))
print(hammingDistance(3,1))