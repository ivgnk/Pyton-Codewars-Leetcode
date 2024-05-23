"""
Done 23.05.2024. Topics: Hash Table, String, Enumeration
2309. Greatest English Letter in Upper and Lower Case
https://leetcode.com/problems/greatest-english-letter-in-upper-and-lower-case/description/

Given a string of English letters s, return the greatest English letter which occurs as both
a lowercase and uppercase letter in s.
The returned letter should be in uppercase.
If no such letter exists, return an empty string.
An English letter b is greater than another letter a if b appears after a in the English alphabet.

Example 1:
Input: s = "lEeTcOdE"
Output: "E"
Explanation:
The letter 'E' is the only letter to appear in both lower and upper case.

Example 2:
Input: s = "arRAzFif"
Output: "R"
Explanation:
The letter 'R' is the greatest letter to appear in both lower and upper case.
Note that 'A' and 'F' also appear in both lower and upper case, but 'R' is greater than 'F' or 'A'.

Example 3:
Input: s = "AbCdEfGhIjK"
Output: ""
Explanation:
There is no letter that appears in both lower and upper case.
"""

# Runtime 20 ms Beats 69.49% of users with Python
# Memory 11.65 MB Beats 69.49% of users with Python
# Runtime 8 ms Beats 98.31% of users with Python
# Memory 11.67 MB Beats 69.49% of users with Python

a_low='abcdefghijklmnopqrstuvwxyz'
a_hgh='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def greatestLetter(s):
    """
    :type s: str
    :rtype: str
    """
    print(len((a_low)))
    for i in range(25,-1,-1):
        if a_low[i] in s and a_hgh[i] in s:
            return a_hgh[i]
    else: return ""


print(greatestLetter("lEeTcOdE"))