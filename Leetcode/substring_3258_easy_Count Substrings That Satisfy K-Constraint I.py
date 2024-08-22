"""
Done 22.08.2024. Topics: String, Sliding Window
3258. Count Substrings That Satisfy K-Constraint I
https://leetcode.com/problems/count-substrings-that-satisfy-k-constraint-i/description/

You are given a binary string s and an integer k.
A binary string satisfies the k-constraint if either of the following conditions holds:
The number of 0's in the string is at most k.
The number of 1's in the string is at most k.
Return an integer denoting the number of
substrings of s that satisfy the k-constraint.

Example 1:
Input: s = "10101", k = 1
Output: 12
Explanation:
Every substring of s except the substrings "1010", "10101", and "0101" satisfies the k-constraint.

Example 2:
Input: s = "1010101", k = 2
Output: 25
Explanation:
Every substring of s except the substrings with a length greater than 5 satisfies the k-constraint.

Example 3:
Input: s = "11111", k = 1
Output: 15
Explanation:
All substrings of s satisfy the k-constraint.

Constraints:
1 <= s.length <= 50
1 <= k <= s.length
s[i] is either '0' or '1'.


Hint 1
Using a brute force approach, check each index until a substring satisfying
the k-constraint is found, then increment.

Solution
✏️ Python brute force solution, but not quite the simplest
# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
The restrictions allow you to avoid TLS even for iterating with substring selection,
which will give a Runtime of about 67 ms. But I want a faster solution.

# Approach
<!-- Describe your approach to solving the problem. -->
Therefore, we analyze the letters separately and set up counters for 0 and 1.

Done 22.08.2024
Runtime 39 ms Beats 66.98%
Memory 11.60 MB Beats 54.46%
"""

# Runtime 67 ms Beats 28.08%
# Memory 11.80 MB Beats 20.49%
def countKConstraintSubstrings2(s, k):
    """
    :type s: str
    :type k: int
    :rtype: int
    """
    ll=len(s)
    n=0
    for i in range(ll):
        for j in range(i+1,ll+1):
            s1=s[i:j]
            if s1.count('1')<=k or s1.count('0')<=k:
                n +=1
            else: break
    return n

# Runtime 98 ms Beats 24.10%
# Memory 11.73 MB Beats 20.49%
def countKConstraintSubstrings3(s, k):
    """
    :type s: str
    :type k: int
    :rtype: int
    """
    ll=len(s)
    n=0
    for i in range(ll):
        lst=[s[i]]; n +=1
        for j in range(i+1,ll):
            lst.append(s[j])
            if lst.count('1')<=k or lst.count('0')<=k:
                n +=1
            else: break
    return n

# Runtime 39 ms Beats 66.98%
# Memory 11.60 MB Beats 54.46%
def countKConstraintSubstrings(s, k):
    """
    :type s: str
    :type k: int
    :rtype: int
    """
    ll=len(s)
    n=0
    for i in range(ll):
        n0=n1=0
        if s[i]=='1': n1 =1
        else: n0 =1
        n +=1
        for j in range(i+1,ll):
            if s[j] == '1': n1 += 1
            else: n0 += 1
            if n0<=k or n1<=k:
                n +=1
            else: break
    return n


# print(countKConstraintSubstrings2(s = "10101", k = 1))
print(countKConstraintSubstrings(s = "10101", k = 1))