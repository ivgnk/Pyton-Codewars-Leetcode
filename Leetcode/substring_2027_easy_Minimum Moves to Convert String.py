"""
Done 31.08.2024. Topics: String, Greedy
2027. Minimum Moves to Convert String
https://leetcode.com/problems/minimum-moves-to-convert-string/description/

You are given a string s consisting of n characters which are either 'X' or 'O'.
A move is defined as selecting three consecutive characters of s and converting them to 'O'.
Note that if a move is applied to the character 'O', it will stay the same.
Return the minimum number of moves required so that all the characters of s are converted to 'O'.

Example 1:
Input: s = "XXX"
Output: 1
Explanation: XXX -> OOO
We select all the 3 characters and convert them in one move.

Example 2:
Input: s = "XXOX"
Output: 2
Explanation: XXOX -> OOOX -> OOOO
We select the first 3 characters in the first move, and convert them to 'O'.
Then we select the last 3 characters and convert them so that the final string contains all 'O's.

Example 3:
Input: s = "OOOO"
Output: 0
Explanation: There are no 'X's in s to convert.

Constraints:
3 <= s.length <= 1000
s[i] is either 'X' or 'O'.

Hint 1
Find the smallest substring you need to consider at a time.
Hint 2
Try delaying a move as long as possible.
"""

# Не увлекайтесь преобразованием строки путем замены, в этом нет необходимости.
# Просто переберите строку, если X найден, перейдите на два символа, а если нет, перейдите к следующей итерации.
# https://leetcode.com/problems/minimum-moves-to-convert-string/description/comments/2433010

# Runtime 12 ms Beats 80.95%
# Memory 11.67 MB Beats 62.86%
# Time Complexity O(N)
# Space Complexity O(1)

def minimumMoves(s):
    """
    :type s: str
    :rtype: int
    """
    n=0; i = 0; ll= len(s)
    while i<ll:
        if s[i]=='X':
            n += 1
            i+=3
        else: i+=1
    return n
