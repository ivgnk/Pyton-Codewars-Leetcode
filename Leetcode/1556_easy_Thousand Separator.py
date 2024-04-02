'''
1556. Thousand Separator
https://leetcode.com/problems/thousand-separator/description/

Given an integer n, add a dot (".") as the thousands separator and return it in string format.

Example 1:
Input: n = 987
Output: "987"

Example 2:
Input: n = 1234
Output: "1.234"
'''


# Python
# Runtime 15 ms Beats 34.85% of users with Python
# Memory 11.69 MB Beats 37.88% of users with Python
# stackoverflow.com/questions/16670125/python-format-string-thousand-separator-with-spaces
def thousandSeparator( n):
    """
    :type n: int
    :rtype: str
    """
    return '{:,}'.format(n).replace(',', '.')

# Python 3
# Runtime 41 ms Beats 10.40% of users with Python3
# Memory 16.46 MB Beats 88.57% of users with Python3
def thousandSeparator(self, n: int) -> str:
    return f'{n:,}'.replace(',', '.')