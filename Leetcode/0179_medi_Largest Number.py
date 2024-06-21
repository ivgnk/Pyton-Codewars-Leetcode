"""
Done 22.06.2024. Topics: String, Sorting
179. Largest Number
https://leetcode.com/problems/largest-number/description/

Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.
Since the result may be very large, so you need to return a string instead of an integer.

Example 1:
Input: nums = [10,2]
Output: "210"

Example 2:
Input: nums = [3,30,34,5,9]
Output: "9534330"
"""

# Runtime 45 ms Beats 30.70%
# Memory 16.42 MB Beats 58.18%
# Runtime  43 ms Beats 43.29%
# Memory 16.39 MB Beats 91.85%
# Runtime 41 ms Beats 55.80%
# Memory 16.39 MB Beats 91.85%
from functools import cmp_to_key
def largestNumber2(nums):
    """
    :type nums: List[int]
    :rtype: str
    """
    # https://stackoverflow.com/questions/77356097/sortedmy-list-key-lambda-x-y-possible
    ll = len(nums)
    snums = [str(i) for i in nums]
    n1 = sorted(snums, key=cmp_to_key(lambda x, y: ((a := x + y) < (b := y + x)) - (a > b)))
    s = ''.join(([str(i) for i in n1]))
    if s == '0' * ll:
        return '0'
    else:
        return s

# Runtime 35 ms Beats 86.50%
# Memory 16.42 MB Beats 58.18%
def largestNumber3(nums):
    ll = len(nums)
    # snums=[str(i) for i in nums]
    snums = map(str, nums)
    n1 = sorted(snums, key=cmp_to_key(lambda x, y: ((a := x + y) < (b := y + x)) - (a > b)))
    s = ''.join(([str(i) for i in n1]))
    if s == '0' * ll:
        return '0'
    else:
        return s

# https://leetcode.com/problems/largest-number/solutions/53333/readable-python-solution-and-still-can-be-optimized-help-me/
# Runtime 45 ms Beats 30.90%
# Memory 16.40 MB Beats 91.71%
def largestNumber4(nums):
    ln=len(nums)
    if set(nums) == {0}:
        return '0'
    n1 = list(map(str,nums))
    for i in range(ln):
        for j in range(i, ln):
            if n1[i] + n1[j] < n1[j] + n1[i]:
                n1[i], n1[j] = n1[j], n1[i]
    return ''.join(n1)


# Bad result
def largestNumber_(nums):
    """
    :type nums: List[int]
    :rtype: str
    """
    def comparator(a, b):
        return str(a) + str(b) > str(b) + str(a)
    a = sorted(nums, key = cmp_to_key(comparator)) # , reverse = True
    a=a[::-1]
    ll=len(nums)
    s = ''.join(([str(i) for i in a]))
    if s == '0' * ll:
        return '0'
    else:
        return s

# Runtime 41 ms Beats 56.00%
# Memory 16.49 MB Beats 57.28%
# https://leetcode.com/problems/largest-number/solutions/53203/two-python-solutions-with-slightly-different-idea-both-are-below-50ms-and-could-be-one-line/
def largestNumber(nums):
    if not any(nums):  return '0'

    def comp_rule(s1, s2):
        if s1+s2 < s2+s1:
            return -1
        if s1+s2 > s2+s1:
            return 1
        return 0

    return ''.join(sorted([str(num) for num in nums], key = cmp_to_key(comp_rule), reverse = True))

# print(largestNumber([10,2])) # "210"
print(largestNumber([3,30,34,5,9])) # "9534330"
