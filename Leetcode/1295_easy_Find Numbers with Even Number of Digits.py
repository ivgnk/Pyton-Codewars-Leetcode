'''
1295. Find Numbers with Even Number of Digits
https://leetcode.com/problems/find-numbers-with-even-number-of-digits/description/
'''

# Runtime 24 ms Beats 95.66% of users with Python
# Memory # 11.92 MB Beats 6.98% of users with Python
def findNumbers(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    return sum([1 for i in nums if len(str(i))%2==0])


def findNumbers2(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ssum=0
    for i in nums:
        if len(str(i))%2==0:
            ssum = ssum+1
    return ssum

