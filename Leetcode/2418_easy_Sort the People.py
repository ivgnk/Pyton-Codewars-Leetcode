"""
Done 26.04.2024. Redone 22.07.2024. Topics: Array, Sorting
You are given an array of strings names, and an array heights that consists of distinct positive integers. Both arrays are of length n.
For each index i, names[i] and heights[i] denote the name and height of the ith person.
Return names sorted in descending order by the people's heights.

Example 1:
Input: names = ["Mary","John","Emma"], heights = [180,165,170]
Output: ["Mary","Emma","John"]
Explanation: Mary is the tallest, followed by Emma and John.

Example 2:
Input: names = ["Alice","Bob","Bob"], heights = [155,185,150]
Output: ["Bob","Alice","Bob"]
Explanation: The first Bob is the tallest, followed by Alice and the second Bob.
"""

# Runtime 75 ms Beats 87.02%
# Memory 12.18 MB Beats 61.97%
def sortPeople(names, heights):
    rll = range(len(names))
    tmp = [(heights[i], names[i]) for i in rll]
    tmp.sort(reverse=True)
    return [tmp[i][1] for i in rll]


# Runtime 76 ms Beats 86.15% of users with Python
# Memory 12.38 MB Beats 14.04% of users with Python
def sortPeople(names, heights):
    """
    :type names: List[str]
    :type heights: List[int]
    :rtype: List[str]
    """
    # https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
    dd=list(zip(names,heights))
    return [k for k, v in sorted(dd, key=lambda item: item[1],reverse=True)]


# print(sortPeople( names = ["Mary","John","Emma"], heights = [180,165,170]))
print(sortPeople(names = ["Alice","Bob","Bob"], heights = [155,185,150]))