"""
2433. Find The Original Array of Prefix Xor
https://leetcode.com/problems/find-the-original-array-of-prefix-xor/description/

You are given an integer array pref of size n. Find and return the array arr of size n that satisfies:
pref[i] = arr[0] ^ arr[1] ^ ... ^ arr[i].
Note that ^ denotes the bitwise-xor operation.
It can be proven that the answer is unique.

Example 1:
Input: pref = [5,2,0,3,1]
Output: [5,7,2,3,2]
Explanation: From the array [5,7,2,3,2] we have the following:
- pref[0] = 5.
- pref[1] = 5 ^ 7 = 2.
- pref[2] = 5 ^ 7 ^ 2 = 0.
- pref[3] = 5 ^ 7 ^ 2 ^ 3 = 3.
- pref[4] = 5 ^ 7 ^ 2 ^ 3 ^ 2 = 1.

Example 2:
Input: pref = [13]
Output: [13]
Explanation: We have pref[0] = arr[0] = 13.
"""

# Runtime 614 ms Beats 80.22% of users with Python
# Memory 30.93 MB Beats 62.59% of users with Python

def findArray(pref):
    """
    :type pref: List[int]
    :rtype: List[int]
    """
    # ll=len(pref)
    # if ll==1: return pref
    res=[pref[0]]
    for i in range(1,len(pref)):
        res.append(pref[i-1]^pref[i])
    return res

print(findArray([5,2,0,3,1]))
# print(5 ^ 7, 5 ^ 7 ^ 2, 5 ^ 7 ^ 2 ^ 3, 5 ^ 7 ^ 2 ^ 3 ^ 2, 0^3 )
# print(0^3)
