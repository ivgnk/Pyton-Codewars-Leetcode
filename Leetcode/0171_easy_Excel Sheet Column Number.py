"""
Done 20.09.2024. Topics: Math, String
171. Excel Sheet Column Number
https://leetcode.com/problems/excel-sheet-column-number/
Given a string columnTitle that represents the column title as appears in an Excel sheet,
return its corresponding column number.

For example:
A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28
...

Example 1:
Input: columnTitle = "A"
Output: 1

Example 2:
Input: columnTitle = "AB"
Output: 28

Example 3:
Input: columnTitle = "ZY"
Output: 701

Constraints:
1 <= columnTitle.length <= 7
columnTitle consists only of uppercase English letters.
columnTitle is in the range ["A", "FXSHRXW"].

Tip
# https://leetcode.com/problems/excel-sheet-column-number/description/comments/1571373
Treat the column value as a base 26 number. Map A to 1, B to 2..., and Z to 26.
YZ = 25*(26^1) + 26*(26^0)
XYZ = 24*(26^2) + 25*(26^1) + 26*(26^0)
"""

# Runtime 19 ms Beats 35.30%
# Memory 11.62 MB Beats 51.56%
def titleToNumber2(columnTitle):
    """
    :type columnTitle: str
    :rtype: int
    """
    dd={s:i+1 for i,s in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}
    n = 0
    ll=len(columnTitle)
    for i in range(ll):
        n+=26**(ll-i-1)*dd[columnTitle[i]]
    return n

    # Runtime 17 ms Beats 49.20%
    # Memory 11.72 MB Beats 18.53%
dd={s:i+1 for i,s in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}
def titleToNumber(columnTitle):
    """
    :type columnTitle: str
    :rtype: int
    """
    ll=len(columnTitle)
    return sum([26**(ll-i-1)*dd[columnTitle[i]] for i in range(ll)])

print(titleToNumber('ZY'))
