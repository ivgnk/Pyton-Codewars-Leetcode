"""
Done 08.05.2024. Topics: String
Given an integer n, return a string with n characters
such that each character in such string occurs an odd number of times.
The returned string must contain only lowercase English letters.
If there are multiples valid strings, return any of them.

Example 1:
Input: n = 4
Output: "pppz"
Explanation: "pppz" is a valid string since the character 'p' occurs three times and the character 'z' occurs once. Note that there are many other valid strings such as "ohhh" and "love".

Example 2:
Input: n = 2
Output: "xy"
Explanation: "xy" is a valid string since the characters 'x' and 'y' occur once. Note that there are many other valid strings such as "ag" and "ur".

Example 3:
Input: n = 7
Output: "holasss"
"""

# Runtime 9 ms Beats 82.96% of users with Python
# Memory 11.58 MB Beats 71.85% of users with Python

def generateTheString(n):
    """
    :type n: int
    :rtype: str
    """
    return 'a'*n if n%2!=0 else 'a'*(n-1)+'b'


print(generateTheString(2))