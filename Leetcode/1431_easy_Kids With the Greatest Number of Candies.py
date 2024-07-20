"""
Redone 20.07.2024. Topics: Array
1431. Kids With the Greatest Number of Candies
https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/description/

There are n kids with candies. You are given an integer array candies,
where each candies[i] represents the number of candies the ith kid has,
and an integer extraCandies, denoting the number of extra candies that you have.
Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies,
they will have the greatest number of candies among all the kids, or false otherwise.
Note that multiple kids can have the greatest number of candies.

Example 1:
Input: candies = [2,3,5,1,3], extraCandies = 3
Output: [true,true,true,false,true]
Explanation: If you give all extraCandies to:
- Kid 1, they will have 2 + 3 = 5 candies, which is the greatest among the kids.
- Kid 2, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
- Kid 3, they will have 5 + 3 = 8 candies, which is the greatest among the kids.
- Kid 4, they will have 1 + 3 = 4 candies, which is not the greatest among the kids.
- Kid 5, they will have 3 + 3 = 6 candies, which is the greatest among the kids.

Example 2:
Input: candies = [4,2,1,1,2], extraCandies = 1
Output: [true,false,false,false,false]
Explanation: There is only 1 extra candy.
Kid 1 will always have the greatest number of candies, even if a different kid is given the extra candy.

Example 3:
Input: candies = [12,1,12], extraCandies = 10
Output: [true,false,true]
"""

# Runtime 27 ms Beats 9.88%
# Memory 11.66 MB Beats 26.78%
# Runtime 14 ms Beats 91.76% of users with Python
# Memory 11.57 MB Beats 78.13% of users with Python

def kidsWithCandies2(candies, extraCandies):
    """
    :type candies: List[int]
    :type extraCandies: int
    :rtype: List[bool]
    """
    lst = []; mmax = max(candies)
    for i in range(len(candies)):
        lst.append(candies[i] + extraCandies >= mmax)
    return lst

# Runtime 19 ms Beats 60.90%
# Memory 11.59 MB Beats 62.20%
# Runtime 17 ms Beats 76.46%
# Memory 11.48 MB Beats 90.01%
# Runtime 15 ms Beats 86.26%
# Memory 11.82 MB Beats 5.36%

def kidsWithCandies(candies, extraCandies):
    """
    :type candies: List[int]
    :type extraCandies: int
    :rtype: List[bool]
    """
    return [candies[i] + extraCandies >= max(candies) for i in range(len(candies))]
