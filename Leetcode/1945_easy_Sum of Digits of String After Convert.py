"""
You are given a string s consisting of lowercase English letters, and an integer k.
First, convert s into an integer by replacing each letter with its position in the alphabet
(i.e., replace 'a' with 1, 'b' with 2, ..., 'z' with 26). Then, transform the integer by replacing it with the sum of its digits. Repeat the transform operation k times in total.

For example, if s = "zbax" and k = 2, then the resulting integer would be 8 by the following operations:
Convert: "zbax" ➝ "(26)(2)(1)(24)" ➝ "262124" ➝ 262124
Transform #1: 262124 ➝ 2 + 6 + 2 + 1 + 2 + 4 ➝ 17
Transform #2: 17 ➝ 1 + 7 ➝ 8
Return the resulting integer after performing the operations described above.

Example 1:
Input: s = "iiii", k = 1
Output: 36
Explanation: The operations are as follows:
- Convert: "iiii" ➝ "(9)(9)(9)(9)" ➝ "9999" ➝ 9999
- Transform #1: 9999 ➝ 9 + 9 + 9 + 9 ➝ 36
Thus the resulting integer is 36.

Example 2:
Input: s = "leetcode", k = 2
Output: 6
Explanation: The operations are as follows:
- Convert: "leetcode" ➝ "(12)(5)(5)(20)(3)(15)(4)(5)" ➝ "12552031545" ➝ 12552031545
- Transform #1: 12552031545 ➝ 1 + 2 + 5 + 5 + 2 + 0 + 3 + 1 + 5 + 4 + 5 ➝ 33
- Transform #2: 33 ➝ 3 + 3 ➝ 6
Thus the resulting integer is 6.

Example 3:
Input: s = "zbax", k = 2
Output: 8
"""

# Runtime 19 ms Beats 71.43% of users with Python
# Memory 11.58 MB Beats 83.67% of users with Python
def getLucky(s, k):
    """
    :type s: str
    :type k: int
    :rtype: int
    """
    n1=[str(ord(s1)-96) for s1 in s ]
    for k in range(1,k+1):
        m=0
        for s1 in n1:
            for s2 in s1:
                m+=int(s2)
        n1=str(m)
    return int(n1)


# def getLucky2(s, k):
#     """
#     :type s: str
#     :type k: int
#     :rtype: int
#     """
#     n1=[str(ord(s1)-96) for s1 in s ]
#     for k in range(1,k+1):
#         m = sum(int(s2) for s1 in n1 for s2 in s1)
#         n1=str(m)
#     return int(n1)


# print(getLucky("zbax",2))
# print(getLucky("iiii",1))
print(getLucky("leetcode",2))