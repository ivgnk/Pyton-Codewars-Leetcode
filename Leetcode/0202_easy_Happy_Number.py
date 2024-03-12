'''
202. Happy Number
https://leetcode.com/problems/happy-number/description/

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

Example 1:
Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

Example 2:
Input: n = 2
Output: false
'''


def isHappy(n):
    """
    :type n: int
    :rtype: bool
    """
    while n != 1:
        s = str(n)
        print(s)
        if len(s) == 1:
            if (s == "1") or (s == "7"):
                return True
            else:
                return False
        else:
            sum = 0
            for ss in s:
                sum = sum + (int(ss)) ** 2
            n = sum
    else:
        return True

print(isHappy(7))