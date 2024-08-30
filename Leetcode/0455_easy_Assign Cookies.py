"""
Done 30.08.2024. Two Pointers, Greedy, Sorting
455. Assign Cookies
https://leetcode.com/problems/assign-cookies/description/

Assume you are an awesome parent and want to give your children some cookies.
But, you should give each child at most one cookie.

Each child i has a greed factor g[i], which is the minimum size of a cookie
that the child will be content with; and each cookie j has a size s[j].
If s[j] >= g[i], we can assign the cookie j to the child i, and the child i will be content.
Your goal is to maximize the number of your content children and output the maximum number.

Example 1:
Input: g = [1,2,3], s = [1,1]
Output: 1
Explanation: You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3.
And even though you have 2 cookies, since their size is both 1, you could only make the child whose greed factor is 1 content.
You need to output 1.

Example 2:
Input: g = [1,2], s = [1,2,3]
Output: 2
Explanation: You have 2 children and 3 cookies. The greed factors of 2 children are 1, 2.
You have 3 cookies and their sizes are big enough to gratify all of the children,
You need to output 2.

Constraints:
1 <= g.length <= 3 * 104
0 <= s.length <= 3 * 104
1 <= g[i], s[j] <= 231 - 1
"""

# https://leetcode.com/problems/assign-cookies/solutions/5681413/cleanest-python-two-pointer-solution/
# Runtime 306 ms Beats 13.46%
# Memory 13.74 MB Beats 6.45%
def findContentChildren(g, s):
    """
    :type g: List[int]
    :type s: List[int]
    :rtype: int
    """
    g.sort(), s.sort()
    greed = 0

    for cookie in s:
        if cookie >= g[greed]:
            greed += 1
        if greed == len(g):
            break

    return greed

# Wrong Answer - 23 / 25 testcases passed
def findContentChildren4(g, s):
    lens=len(s)
    if len(g) == lens:
        gset = set(g)
        sset = set(s)
        if len(sset) == len(gset) == 1:
            if s[0] >= g[0]:
                return len(g)
            else:
                return 0

    g = sorted(g)
    s = sorted(s)
    n = 0
    j1=0
    for gi in g:
        for j in range(j1,lens):
            if s[j] >= gi:
                n += 1
                j1 += 1
                break
    return n


# Runtime 603 ms Beats 6.82%
# Memory 14.17 MB Beats 6.45%
def findContentChildren3(g, s):
    """
    :type g: List[int]
    :type s: List[int]
    :rtype: int
    """
    if len(g) == len(s):
        gset = set(g)
        sset = set(s)
        if len(sset) == len(gset) == 1:
            if s[0] >= g[0]:
                return len(g)
            else:
                return 0

    g = sorted(g)
    s = sorted(s)
    n = 0
    for gi in g:
        for si in s:
            if si >= gi:
                n += 1
                s.remove(si)
                break
    return n

# Time Limit Exceeded - 21 / 25 testcases passed
# len(g),len(s) = 30000, 30000
def findContentChildren2(g, s):
    """
    :type g: List[int]
    :type s: List[int]
    :rtype: int
    """
    g=sorted(g)
    s=sorted(s)
    n=0
    for gi in g:
        for si in s:
            if si>=gi:
                n +=1
                s.remove(si)
                break
    return n

print(findContentChildren(g = [1,2,3], s = [3]))
