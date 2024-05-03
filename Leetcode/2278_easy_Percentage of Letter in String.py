"""
Done 03.05.2024
2278. Percentage of Letter in String
Given a string s and a character letter, return the percentage of characters in
s that equal letter rounded down to the nearest whole percent.

Example 1:
Input: s = "foobar", letter = "o"
Output: 33
Explanation:
The percentage of characters in s that equal the letter 'o' is 2 / 6 * 100% = 33% when rounded down, so we return 33.

Example 2:
Input: s = "jjjj", letter = "k"
Output: 0
Explanation:
The percentage of characters in s that equal the letter 'k' is 0%, so we return 0.
"""

# Runtime 13 ms Beats 45.14% of users with Python
# Memory 11.54 MB Beats 87.50% of users with Python
# Runtime 11 ms Beats 69.44% of users with Python
# Memory 11.66 MB Beats 56.94% of users with Python

def percentageLetter(s, letter):
    """
    :type s: str
    :type letter: str
    :rtype: int
    """

    return s.count(letter)*100/len(s)