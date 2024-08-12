"""
Done 12.08.2024. Topics: String
2937. Make Three Strings Equal
https://leetcode.com/problems/make-three-strings-equal/description/

You are given three strings: s1, s2, and s3.
In one operation you can choose one of these strings and delete its rightmost character.
Note that you cannot completely empty a string.

Return the minimum number of operations required to make the strings equal.
If it is impossible to make them equal, return -1.

Example 1:
Input: s1 = "abc", s2 = "abb", s3 = "ab"
Output: 2
Explanation: Deleting the rightmost character from both s1 and s2 will result in three equal strings.

Example 2:
Input: s1 = "dac", s2 = "bac", s3 = "cac"
Output: -1
Explanation: Since the first letters of s1 and s2 differ, they cannot be made equal.

Constraints:
1 <= s1.length, s2.length, s3.length <= 100
s1, s2 and s3 consist only of lowercase English letters.

Hint 1
Calculate the length of the longest common prefix of the 3 strings.

Solution
✏️ Easy Python solution
# Intuition
Compare the initial characters of strings sequentially

# Approach
Just compare characters without using any functions. And calculate the length of the common part.
The number of operations is equal to the sum of the lengths of the strings minus
three times the length of the common part.
Done 12.08.2024, Runtime 9 ms Beats 98.59%
"""

# Runtime 9 ms Beats 98.59%
# Memory 11.54 MB Beats 80.28%
def findMinimumOperations(s1, s2, s3):
    """
    :type s1: str
    :type s2: str
    :type s3: str
    :rtype: int
    """
    l1 = len(s1); l2 = len(s2); l3 = len(s3)
    min_len=min(l1,l2,l3)
    n=0
    for i in range(min_len):
        if s1[i]==s2[i]==s3[i]: n+=1
        else: break
    if n==0: return -1
    else:
        return l1-n + l2-n + l3-n

print( findMinimumOperations(s1 = "abc", s2 = "abb", s3 = "ab" ))  # 2
print( findMinimumOperations(s1 = "dac", s2 = "bac", s3 = "cac"))



