"""
30.08.2024. Topics: Combinatorics
1641. Count Sorted Vowel Strings
https://leetcode.com/problems/count-sorted-vowel-strings/description/

Given an integer n, return the number of strings of length n that consist only of vowels
(a, e, i, o, u) and are lexicographically sorted.

A string s is lexicographically sorted if for all valid i,
s[i] is the same as or comes before s[i+1] in the alphabet.

Example 1:
Input: n = 1
Output: 5
Explanation: The 5 sorted strings that consist of vowels only are ["a","e","i","o","u"].

Example 2:
Input: n = 2
Output: 15
Explanation: The 15 sorted strings that consist of vowels only are
["aa","ae","ai","ao","au","ee","ei","eo","eu","ii","io","iu","oo","ou","uu"].
Note that "ea" is not a valid string since 'e' comes after 'a' in the alphabet.

Example 3:
Input: n = 33
Output: 66045

Constraints:
1 <= n <= 50
"""
# Runtime 12 ms Beats 74.31%
# Memory 11.52 MB Beats 63.76%

# https://leetcode.com/problems/count-sorted-vowel-strings/description/comments/1570263
# https://leetcode.com/problems/count-sorted-vowel-strings/description/comments/1570874
def countVowelStrings(n):
    """
    :type n: int
    :rtype: int
    """
    return (n + 1) * (n + 2) * (n + 3) * (n + 4) / 24
