"""
16.05.2024. Topics: Math, String
168. Excel Sheet Column Title
https://leetcode.com/problems/excel-sheet-column-title/description/

Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.
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
Input: columnNumber = 1
Output: "A"

Example 2:
Input: columnNumber = 28
Output: "AB"

Example 3:
Input: columnNumber = 701
Output: "ZY"

Constraints:
1 <= columnNumber <= 2**31 - 1
"""

# Runtime 15 ms Beats 48.78% of users with Python
# Memory 11.63 MB Beats 42.40% of users with Python

# https://leetcode.com/problems/excel-sheet-column-title/description/comments/2025139

def convertToTitle(columnNumber):
    """
    :type columnNumber: int
    :rtype: str
    """
    r = []
    while columnNumber > 0:
        remind = (columnNumber - 1) % 26
        l = chr(ord("A") + remind)
        r.insert(0, l)
        columnNumber = (columnNumber - 1) // 26
    return "".join(r)

print(convertToTitle(1))

