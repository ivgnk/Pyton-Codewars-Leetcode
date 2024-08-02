"""
Done 02.08.2024. Topics: String
2380. Time Needed to Rearrange a Binary String
https://leetcode.com/problems/time-needed-to-rearrange-a-binary-string/

You are given a binary string s.
In one second, all occurrences of "01" are simultaneously replaced with "10".
This process repeats until no occurrences of "01" exist.
Return the number of seconds needed to complete this process.

Example 1:
Input: s = "0110101"
Output: 4
Explanation:
After one second, s becomes "1011010".
After another second, s becomes "1101100".
After the third second, s becomes "1110100".
After the fourth second, s becomes "1111000".
No occurrence of "01" exists any longer, and the process needed 4 seconds to complete,
so we return 4.

Example 2:
Input: s = "11100"
Output: 0
Explanation:
No occurrence of "01" exists in s, and the processes needed 0 seconds to complete,
so we return 0.

Constraints:
1 <= s.length <= 1000
s[i] is either '0' or '1'.

Hint 1
Try replicating the steps from the problem statement.
Hint 2
Perform the replacements simultaneously, and return the number of times the process repeats.
"""

# Runtime 118 ms Beats 70.37%
# Memory 11.78 MB Beats 11.11%
# Runtime 113 ms Beats 81.48%
# Memory 11.76 MB Beats 11.11%
def secondsToRemoveOccurrences(s):
    """
    :type s: str
    :rtype: int
    """
    s01='01'; n=0
    while s01 in s:
        s=s.replace(s01,'10')
        n=n+1
        print(n,s)
    return n

print(secondsToRemoveOccurrences("0110101"))