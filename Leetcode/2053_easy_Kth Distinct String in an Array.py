"""
Done 09.05.2024. Topics: Array, Hash Table, String, Counting
2053. Kth Distinct String in an Array
A distinct string is a string that is present only once in an array.
Given an array of strings arr, and an integer k, return the kth distinct string present in arr.
If there are fewer than k distinct strings, return an empty string "".
Note that the strings are considered in the order in which they appear in the array.

Example 1:
Input: arr = ["d","b","c","b","c","a"], k = 2
Output: "a"
Explanation:
The only distinct strings in arr are "d" and "a".
"d" appears 1st, so it is the 1st distinct string.
"a" appears 2nd, so it is the 2nd distinct string.
Since k == 2, "a" is returned.

Example 2:
Input: arr = ["aaa","aa","a"], k = 1
Output: "aaa"
Explanation:
All strings in arr are distinct, so the 1st string "aaa" is returned.
Example 3:

Input: arr = ["a","b","a"], k = 3
Output: ""
Explanation:
The only distinct string is "b". Since there are fewer than 3 distinct strings, we return an empty string "".
"""

# Runtime 67 ms Beats 74.48% of users with Python3
# Memory 16.70 MB Beats 99.46% of users with Python3

from collections import Counter
def kthDistinct(arr, k):
    """
    :type arr: List[str]
    :type k: int
    :rtype: str
    """
    # dd=dict(Counter(arr))
    res=[k for k,v in dict(Counter(arr)).items() if v==1]
    if len(res)>=k: return res[k-1]
    else: return ""

print(kthDistinct(arr = ["d","b","c","b","c","a"], k = 2))