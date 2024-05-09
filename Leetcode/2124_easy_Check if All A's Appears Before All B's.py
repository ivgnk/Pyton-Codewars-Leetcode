"""
Done 10.05.2024. Topics: String
2124. Check if All A's Appears Before All B's

Given a string s consisting of only the characters 'a' and 'b', return true if every 'a'
appears before every 'b' in the string. Otherwise, return false.

Example 1:
Input: s = "aaabbb"
Output: true
Explanation:
The 'a's are at indices 0, 1, and 2, while the 'b's are at indices 3, 4, and 5.
Hence, every 'a' appears before every 'b' and we return true.

Example 2:
Input: s = "abab"
Output: false
Explanation:
There is an 'a' at index 2 and a 'b' at index 1.
Hence, not every 'a' appears before every 'b' and we return false.

Example 3:
Input: s = "bbb"
Output: true
Explanation:
There are no 'a's, hence, every 'a' appears before every 'b' and we return true.
"""

# Runtime 15 ms Beats 44.80% of users with Python
# Memory 11.80 MB Beats 23.38% of users with Python
# Runtime 9 ms Beats 85.71% of users with Python
# Memory 11.61 MB Beats 53.90% of users with Python

from collections import Counter
def checkString(s):
    """
    :type s: str
    :rtype: bool
    """
    dd=dict(Counter(s))
    fa=s.find('a') # print(f'{fa=}')
    fb=s.find('b') # print(f'{fb=}')
    if fa==-1: return True
    if fb==-1: return True
    if 'b' not in s[:dd['a']]: return True
    else : return False

print(checkString('abab'))
