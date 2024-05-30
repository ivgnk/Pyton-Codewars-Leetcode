"""
Done 30.05.2024. Topics: Array, Greedy
2078. Two Furthest Houses With Different Colors
https://leetcode.com/problems/two-furthest-houses-with-different-colors/description/

here are n houses evenly lined up on the street, and each house is beautifully painted. You are given a 0-indexed integer array colors of length n, where colors[i] represents the color of the ith house.
Return the maximum distance between two houses with different colors.
The distance between the ith and jth houses is abs(i - j), where abs(x) is the absolute value of x.

Example 1:
Input: colors = [1,1,1,6,1,1,1]
Output: 3
Explanation: In the above image, color 1 is blue, and color 6 is red.
The furthest two houses with different colors are house 0 and house 3.
House 0 has color 1, and house 3 has color 6. The distance between them is abs(0 - 3) = 3.
Note that houses 3 and 6 can also produce the optimal answer.

Example 2:
Input: colors = [1,8,3,8,3]
Output: 4
Explanation: In the above image, color 1 is blue, color 8 is yellow, and color 3 is green.
The furthest two houses with different colors are house 0 and house 4.
House 0 has color 1, and house 4 has color 3. The distance between them is abs(0 - 4) = 4.

Example 3:
Input: colors = [0,1]
Output: 1
Explanation: The furthest two houses with different colors are house 0 and house 1.
House 0 has color 0, and house 1 has color 1. The distance between them is abs(0 - 1) = 1.

Hint 1
The constraints are small. Can you try the combination of every two houses?
Hint 2
Greedily, the maximum distance will come from either the pair of the leftmost house and
possibly some house on the right with a different color,
or the pair of the rightmost house and possibly some house on the left with a different color.
"""

# Runtime 21 ms Beats 67.02% of users with Python
# Memory 11.70 MB Beats 41.49% of users with Python
# Runtime 17 ms Beats 87.23% of users with Python
# Memory 11.46 MB Beats 95.74% of users with Python

def maxDistance(colors):
    """
    :type colors: List[int]
    :rtype: int
    """
    ll=len(colors)
    if colors[0] != colors[ll-1]: return ll-1
    i=0; j=ll-2
    mmax=-1
    while i<j:
        if colors[i] != colors[j]:
            mmax=max(mmax,j-i)
            break
        j=j-1
    i=1; j=ll-1
    while i<j:
        if colors[i] != colors[j]:
            mmax = max(mmax, j - i)
            break
        i = i + 1
    return mmax


# print(maxDistance([0,1]))
# print(maxDistance([1,8,3,8,3]))
print(maxDistance([1,1,1,6,1,1,1]))