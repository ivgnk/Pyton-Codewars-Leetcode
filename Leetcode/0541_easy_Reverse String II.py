"""
Done 16.10.2024. Topics: String
541. Reverse String II
Given a string s and an integer k,
reverse the first k characters for every 2k characters counting from the start of the string.

If there are fewer than k characters left, reverse all of them.
If there are less than 2k but greater than or equal to k characters,
then reverse the first k characters and leave the other as original.

Example 1:
Input: s = "abcdefg", k = 2
Output: "bacdfeg"

Example 2:
Input: s = "abcd", k = 2
Output: "bacd"

Constraints:
1 <= s.length <= 104
s consists of only lowercase English letters.
1 <= k <= 104

My solution https://leetcode.com/problems/reverse-string-ii/solutions/5920037/easy-python-solution-for-problem-541/
✏️ Easy Python solution for Problem 541
Intuition
Convert string to list
Approach
Do as described in Problem
"""

# Runtime 13 ms Beats 80.82%
# Memory 11.81 MB Beats 80.11%
# Time Complexity O(N)
# Space Complexity O(N)

def reverseStr(s, k):
    """
    :type s: str
    :type k: int
    :rtype: str
    """
    ll=len(s); k2=k*2
    rst=ll%k2
    lst=list(s)
    i=0
    while i<=ll:
        lst[i:i+k]=reversed(lst[i:i+k])
        i+=k2
    if rst>0:
        if i+k<=ll:
            lst[i:i + k] = reversed(lst[i:i + k])
        else:
            lst[i:ll] = reversed(lst[i:ll])
    return ''.join(lst)

# print(reverseStr("abcdefg",2))
print(reverseStr(s =
                 "krmyfshbspcgtesxnnljhfursyissjnsocgdhgfxubewllxzqhpasguvlrxtkgatzfybprfmmfithphckksnvjkcvnsqgsgosfxc",
                  k = 20))
