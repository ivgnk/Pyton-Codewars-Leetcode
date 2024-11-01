"""
Done 01.11.2024. Topics: Hash Table
3335. Total Characters in String After Transformations I
https://leetcode.com/problems/total-characters-in-string-after-transformations-i/description/

You are given a string s and an integer t, representing the number of transformations to perform. In one transformation, every character in s is replaced according to the following rules:

If the character is 'z', replace it with the string "ab".
Otherwise, replace it with the next character in the alphabet. For example, 'a' is replaced with 'b',
'b' is replaced with 'c', and so on.
Return the length of the resulting string after exactly t transformations.

Since the answer may be very large, return it modulo 109 + 7.

Example 1:
Input: s = "abcyy", t = 2
Output: 7
Explanation:
First Transformation (t = 1):
'a' becomes 'b'
'b' becomes 'c'
'c' becomes 'd'
'y' becomes 'z'
'y' becomes 'z'
String after the first transformation: "bcdzz"
Second Transformation (t = 2):
'b' becomes 'c'
'c' becomes 'd'
'd' becomes 'e'
'z' becomes "ab"
'z' becomes "ab"
String after the second transformation: "cdeabab"
Final Length of the string: The string is "cdeabab", which has 7 characters.

Example 2:
Input: s = "azbk", t = 1
Output: 5
Explanation:
First Transformation (t = 1):
'a' becomes 'b'
'z' becomes "ab"
'b' becomes 'c'
'k' becomes 'l'
String after the first transformation: "babcl"
Final Length of the string: The string is "babcl", which has 5 characters.

Constraints:
1 <= s.length <= 105
s consists only of lowercase English letters.
1 <= t <= 105

Hint 1
Maintain the frequency of each character.

My solution https://leetcode.com/problems/total-characters-in-string-after-transformations-i/solutions/5993957/easy-python-solution-for-problem-3335-based-on-hint/
✏️ Easy Python solution for Problem 3335 based on Hint

Intuition
Hint:
Maintain the frequency of each character.
Tip
Notice that each transformation only affects the length if there's a 'z' in the string,
as 'z' expands into "ab."
For other letters, the length remains the same.
Track the occurrences of 'z' and use them to calculate the length increase for each transformation.
This will allow you to calculate the length efficiently without fully transforming the string each time.
https://leetcode.com/problems/total-characters-in-string-after-transformations-i/description/comments/2695175

Approach
Runtime 5315 ms Beats 66.07%
Memory 15.43 MB Beats 83.93%

Complexity
Time complexity: O(N)
Space complexity: O(1)
"""
from collections import Counter
from string import ascii_lowercase
from copy import copy
dtr={'a': 'b', 'b': 'c', 'c': 'd', 'd': 'e', 'e': 'f', 'f': 'g', 'g': 'h', 'h': 'i', 'i': 'j', 'j': 'k', 'k': 'l',
     'l': 'm', 'm': 'n', 'n': 'o', 'o': 'p', 'p': 'q', 'q': 'r', 'r': 's', 's': 't', 't': 'u', 'u': 'v', 'v': 'w',
     'w': 'x', 'x': 'y', 'y': 'z', 'z': 'ab'}

inid={'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
# Time Limit Exceeded - 502 / 824 testcases passed

# def lengthAfterTransformations2(s, t):
#     s = list(s)
#     currl = len(s)
#     for i in range(t):
#         str = []
#         for j in range(currl):
#             if s[j] != 'z':
#                 str += dtr[s[j]]
#             else:
#                 str += ['a'] + ['b']
#                 currl += 1
#         s = str
#     return currl

# Runtime 5315 ms Beats 66.07%
# Memory 15.43 MB Beats 83.93%

inidn={0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0, 15: 0, 16: 0, 17: 0, 18: 0, 19: 0, 20: 0, 21: 0, 22: 0, 23: 0, 24: 0, 25: 0}
def lengthAfterTransformations(s, t):
    """
    :type s: str
    :type t: int
    :rtype: int
    """
    dd=inidn.copy()
    for s1 in s: dd[ord(s1)-97]+=1
    for _ in range(t):
        newd=inidn.copy()
        for i in range(1,26):
            newd[i]=dd[i-1]
        newd[0]=dd[25]
        newd[1]+=dd[25]
        dd=newd
    return sum(i for i in dd.values()) %  (10**9 + 7)

# print(lengthAfterTransformations(s = "abcyy", t = 2))
# print(lengthAfterTransformations(s = "azbk", t = 1))

if __name__=="__main__":
    # dd={s:ord(s)-96 for s in ascii_lowercase}
    # dd2={s:ord(s)-96 for s in ascii_lowercase}
    # dd2 = {i: 0 for i in range(26)}
    # print(dd)
    # print(dd2)
    # print(inid)
    print(lengthAfterTransformations(s = "abcyy", t = 2))
    print(lengthAfterTransformations(s="azbk", t=1))
    # print({ascii_lowercase[i]: ascii_lowercase[i + 1] for i in range(len(ascii_lowercase) - 1)})



