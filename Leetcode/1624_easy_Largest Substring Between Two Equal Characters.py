'''
1624. Largest Substring Between Two Equal Characters

Given a string s, return the length of the longest substring between two equal characters,
excluding the two characters. If there is no such substring return -1.
A substring is a contiguous sequence of characters within a string.

Example 1:
Input: s = "aa"
Output: 0
Explanation: The optimal substring here is an empty substring between the two 'a's.

Example 2:
Input: s = "abca"
Output: 2
Explanation: The optimal substring here is "bc".

Example 3:
Input: s = "cbzxy"
Output: -1
Explanation: There are no characters that appear twice in s.
'''

# Runtime 15 ms Beats 63.70% of users with Python
# Memory 11.74 MB Beats 27.40% of users with Python

from collections import Counter
def maxLengthBetweenEqualCharacters(s):
    """
    :type s: str
    :rtype: int
    """
    maxlen=-1
    dd=dict(Counter(s))
    dd2=dict((k, v) for k, v in dd.items() if v >= 2)
    for k, v in dd2.items():
        ls_=s.find(k)  # 0
        rs_=s.rfind(k)
        clen=rs_-ls_+1-2
        if clen>maxlen: maxlen=clen
    return maxlen

# print(maxLengthBetweenEqualCharacters('aa'))
# print(maxLengthBetweenEqualCharacters('abca'))
print(maxLengthBetweenEqualCharacters('cbzxy'))