"""
Done 10.05.2024. Topics: String
482. License Key Formatting

You are given a license key represented as a string s that consists of only alphanumeric characters and dashes.
The string is separated into n + 1 groups by n dashes. You are also given an integer k.

We want to reformat the string s such that each group contains exactly k characters, except for the first group,
which could be shorter than k but still must contain at least one character. Furthermore, there must be a dash inserted between two groups, and you should convert all lowercase letters to uppercase.

Return the reformatted license key.

Example 1:
Input: s = "5F3Z-2e-9-w", k = 4
Output: "5F3Z-2E9W"
Explanation: The string s has been split into two parts, each part has 4 characters.
Note that the two extra dashes are not needed and can be removed.

Example 2:
Input: s = "2-5g-3-J", k = 2
Output: "2-5G-3J"
Explanation: The string s has been split into three parts, each part has 2 characters except
the first part as it could be shorter as mentioned above.
"""

# Runtime 34 ms Beats 95.70% of users with Python3
# Memory 17.37 MB Beats 35.41% of users with Python3


def licenseKeyFormatting(s, k):
    """
    :type s: str
    :type k: int
    :rtype: str
    """
    s=s.replace('-','').upper()
    ll=len(s)
    s1=[s[i:i+k] for i in range(ll,-1,- k)]
    if ll%k !=0: s1=s1+[s[:ll%k]]
    s1 = [ss for ss in s1 if ss !='']
    s1.reverse()
    return '-'.join((s1))

# print(licenseKeyFormatting(s = "5F3Z-2e-9-w", k = 4))
print(licenseKeyFormatting(s = "2-5g-3-J", k = 2))
