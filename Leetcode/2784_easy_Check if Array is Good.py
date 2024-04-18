"""
2784. Check if Array is Good
https://leetcode.com/problems/check-if-array-is-good/description/
"""

# Runtime 30 ms Beats 42.05% of users with Python
# Memory 11.68 MB Beats 37.50% of users with Python

def isGood(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    n = len(nums)-1
    baseN=list(range(1,n))
    baseN.append(n)
    baseN.append(n)
    print(baseN)
    return sorted(baseN)==sorted(nums)

def good_arr():
    for i in range(1,11):
        baseN = list(range(1, i))
        baseN.append(i)
        baseN.append(i)
        print(i,baseN)





print(isGood([1, 3, 3, 2]))
# good_arr()