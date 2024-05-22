"""
Done 22.05.2024. Topics: Two Pointers, String
557. Reverse Words in a String III
https://leetcode.com/problems/reverse-words-in-a-string-iii/description/

Example 1:
Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

Example 2:
Input: s = "Mr Ding"
Output: "rM gniD"
"""

# Runtime 19 ms Beats 73.05% of users with Python
# Memory 13.10 MB Beats 14.77% of users with Python

def reverseWords(s):
    """
    :type s: str
    :rtype: str
    """
    s1=s.split()
    return ' '.join([s1[i][::-1] for i in range(len(s1))])

print(reverseWords("Let's take LeetCode contest"))