"""
Done 07.02.2025. Topics: Hash Table, String
3442. Maximum Difference Between Even and Odd Frequency I

You are given a string s consisting of lowercase English letters.
Your task is to find the maximum difference between the frequency of two characters
in the string such that:
- One of the characters has an even frequency in the string.
- The other character has an odd frequency in the string.
Return the maximum difference, calculated as the frequency of the character
with an odd frequency minus the frequency of the character with an even frequency.

Example 1:
Input: s = "aaaaabbc"
Output: 3

Explanation:
The character 'a' has an odd frequency of 5, and 'b' has an even frequency of 2.
The maximum difference is 5 - 2 = 3.

Example 2:
Input: s = "abcabcab"
Output: 1
Explanation:
The character 'a' has an odd frequency of 3, and 'c' has an even frequency of 2.
The maximum difference is 3 - 2 = 1.

Constraints:
3 <= s.length <= 100
s consists only of lowercase English letters.
s contains at least one character with an odd frequency and one with an even frequency.

Hint 1
Use a frequency map to identify the maximum odd and minimum even frequencies.
Then, calculate their difference.

My solution
Easy Python solution for Problem 3442
https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-i/solutions/6388358/easy-python-solution-for-problem-3442-by-77fn/
"""

# Runtime 1 ms Beats 84.52%
# Memory 12.49 MB Beats 51.09%
# Time Complexity O(N)
# Space Complexity O(N)

def maxDifference(s):
    """
    :type s: str
    :rtype: int
    """
    dd=dict()
    for s1 in s:
        if s1 in dd:
            dd[s1]+=1
        else:
            dd[s1]=1
    max_odd=-1;  min_even=101
    for k,v in dd.items():
        if v%2==0:
            min_even=min(min_even,v)
        else:
            max_odd=max(max_odd,v)
    return max_odd-min_even

print(maxDifference("aaaaabbc"))
print(maxDifference("abcabcab"))


