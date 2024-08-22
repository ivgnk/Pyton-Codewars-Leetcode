"""
Done 22.08.2024. Topics: String, String Matching
796. Rotate String
https://leetcode.com/problems/rotate-string/description/

Given two strings s and goal, return true if and only if
s can become goal after some number of shifts on s.

A shift on s consists of moving the leftmost character of s to the rightmost position.
For example, if s = "abcde", then it will be "bcdea" after one shift.

Example 1:
Input: s = "abcde", goal = "cdeab"
Output: true

Example 2:
Input: s = "abcde", goal = "abced"
Output: false

Constraints:
1 <= s.length, goal.length <= 100
s and goal consist of lowercase English letters.

Solution
✏️ Easy, but fast Python solution
# Intuition
To simulate a shift, divide the string into 2 parts, and then connect it in reverse order

# Approach
Do not forget to make checks for the length and the same letters

Time Complexity O(NLogN)
Space Complexity O(N)
"""

# Runtime 4 ms Beats 97.37%
# Memory 11.62 MB Beats 50.82%
def rotateString(s, goal):
    """
    :type s: str
    :type goal: str
    :rtype: bool
    """
    ll=len(s)
    if ll != len(goal): return False
    if sorted(s) != sorted(goal): return False
    if s==goal: return True
    for i in range(1,ll):
        if s[i:]+s[:i]==goal: return True
    return False

# print(rotateString(s = "abcde", goal = "cdeab"))
# print(rotateString(s = "abcde", goal = "abced"))
# print(rotateString(s = "gcmbf", goal = "fgcmb"))




