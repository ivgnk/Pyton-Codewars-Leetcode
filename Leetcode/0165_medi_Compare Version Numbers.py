"""
Done 05.11.2024. Topics: String
165. Compare Version Numbers
https://leetcode.com/problems/compare-version-numbers/description/

Given two version strings, version1 and version2, compare them.
A version string consists of revisions separated by dots '.'.
The value of the revision is its integer conversion ignoring leading zeros.

To compare version strings, compare their revision values in left-to-right order.
If one of the version strings has fewer revisions,
treat the missing revision values as 0.

Return the following:
If version1 < version2, return -1.
If version1 > version2, return 1.
Otherwise, return 0.

Example 1:
Input: version1 = "1.2", version2 = "1.10"
Output: -1
Explanation:
version1's second revision is "2" and version2's second revision is "10": 2 < 10, so version1 < version2.

Example 2:
Input: version1 = "1.01", version2 = "1.001"
Output: 0
Explanation:
Ignoring leading zeroes, both "01" and "001" represent the same integer "1".

Example 3:
Input: version1 = "1.0", version2 = "1.0.0.0"
Output: 0
Explanation:
version1 has less revisions, which means every missing revision are treated as "0".

Constraints:
1 <= version1.length, version2.length <= 500
version1 and version2 only contain digits and '.'.
version1 and version2 are valid version numbers.
All the given revisions in version1 and version2 can be stored in a 32-bit integer.

Hint 1
You can use two pointers for each version string to traverse them together
while comparing the corresponding segments.
Hint 2
Utilize the substring method to extract each version segment delimited by '.'.
Ensure you're extracting the segments correctly by adjusting the start and end
indices accordingly.

My solution https://leetcode.com/problems/compare-version-numbers/solutions/6009456/easy-and-fast-0-ms-python-solution-for-problem-0165/
✏️ Easy and fast (0 ms) Python solution for Problem 0165
Intuition
Use standard Python tools: string split, list, list comprehension
Do not use "Two Pointers" as mentioned in Topics
"""

# Runtime 0 ms Beats 100.00%
# Memory 16.66 MB Beats 20.49%

def compareVersion(version1, version2):
    """
    :type version1: str
    :type version2: str
    :rtype: int
    """
    i1=[int(s) for s in version1.split(sep='.')]; l1=len(i1)
    i2=[int(s) for s in version2.split(sep='.')]; l2=len(i2)
    ll=max(l1,l2);  dl=abs(l1-l2)
    if l1<l2: i1+=[0]*dl
    elif l1>l2: i2 += [0] * dl

    for i in range(ll):
        if i1[i]<i2[i]: return -1
        elif i1[i]>i2[i]: return 1
    return 0

print(compareVersion(version1 = "1.2", version2 = "1.10"))
print(compareVersion(version1 = "1.01", version2 = "1.001"))
print(compareVersion(version1 = "1.0", version2 = "1.0.0.0"))