"""
Done 07.10.2024. Topics: String
1758. Minimum Changes To Make Alternating Binary String
https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/description/

You are given a string s consisting only of the characters '0' and '1'.
In one operation, you can change any '0' to '1' or vice versa.

The string is called alternating if no two adjacent characters are equal.
For example, the string "010" is alternating, while the string "0100" is not.
Return the minimum number of operations needed to make s alternating.

Example 1:
Input: s = "0100"
Output: 1
Explanation: If you change the last character to '1', s will be "0101", which is alternating.

Example 2:
Input: s = "10"
Output: 0
Explanation: s is already alternating.

Example 3:
Input: s = "1111"
Output: 2

Explanation: You need two operations to reach "0101" or "1010".

Constraints:
1 <= s.length <= 10**4
s[i] is either '0' or '1'.

Hint 1
Think about how the final string will look like.
Hint 2
It will either start with a '0' and be like '010101010..' or
with a '1' and be like '10101010..'
Hint 3
Try both ways, and check for each way, the number of changes needed
to reach it from the given string.
The answer is the minimum of both ways.

tip
Very funny! First, I must calculate two cases:

Total number change (cnt1) to change String -> '101010...'
Total number change (cnt2) to change String -> '010101...'
Return min(cnt1,cnt2)
But actually, we just calculate a case.
Either cnt1 or cnt2. and return min(cnt1, n-cnt1) or min(cnt2,n-cnt2)
https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/description/comments/2180937

My solution
https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/solutions/5882979/python-solution-based-on-problem-hints-with-pre-calculated-target-arrays/
Intuition
Pre-calculate 2 target arrays
Approach
Loop through arrays and count differences with original string
"""


l0 = ['0' if i % 2 == 0 else '1' for i in range(10000)]
l1 = ['1' if i % 2 == 0 else '0' for i in range(10000)]
# Runtime 23 ms Beats 90.83%
# Memory 11.83 MB Beats 59.17%
def minOperations(s):
    """
    :type s: str
    :rtype: int
    """
    cnt0, cnt1 = 0, 0
    for i, s1 in enumerate(s):
        if s1 != l0[i]: cnt0 += 1
        if s1 != l1[i]: cnt1 += 1
    return min(cnt0, cnt1)

# Runtime 29 ms Beats 69.17%
# Memory 11.94 MB Beats 36.67%
def minOperations2(s):
    """
    :type s: str
    :rtype: int
    """
    cnt0, cnt1= 0, 0
    for i in range(len(s)):
        if s[i]!=l0[i]: cnt0+=1
        if s[i]!=l1[i]: cnt1+=1
    return min(cnt0, cnt1)
print(minOperations("0100"))
print(minOperations("10"))
print(minOperations("1111"))







