"""
09.05.2024
556. Next Greater Element III
Given a positive integer n,
find the smallest integer which has exactly the same digits existing in the integer n and is greater in value than n.
If no such positive integer exists, return -1.

Note that the returned integer should fit in 32-bit integer,
if there is a valid answer but it does not fit in 32-bit integer, return -1.

Example 1:
Input: n = 12
Output: 21

Example 2:
Input: n = 21
Output: -1
"""

# Memory Limit Exceeded -- 39 / 39 testcases passed

from itertools import permutations
def nextGreaterElement(n):
    """
    :type n: int
    :rtype: int
    """
    print(n)
    kk = 2147483647
    if n > kk or n < 1: return -1
    s = str(n)
    lst = list(permutations(s))
    lst = sorted(set([''.join(s) for s in lst]))
    # print(lst2)
    ind = lst.index(s)
    if ind == len(lst) - 1:
        return -1
    else:
        i = int(lst[ind + 1])
        if i > kk:
            return -1
        else:
            return i


print(nextGreaterElement(12))
print(nextGreaterElement(21))