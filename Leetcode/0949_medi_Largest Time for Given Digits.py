"""
949. Largest Time for Given Digits
https://leetcode.com/problems/largest-time-for-given-digits/

Given an array arr of 4 digits, find the latest 24-hour time that can be made using each digit exactly once.
24-hour times are formatted as "HH:MM", where HH is between 00 and 23, and MM is between 00 and 59.
The earliest 24-hour time is 00:00, and the latest is 23:59.
Return the latest 24-hour time in "HH:MM" format. If no valid time can be made, return an empty string.

Example 1:
Input: arr = [1,2,3,4]
Output: "23:41"
Explanation: The valid 24-hour times are "12:34", "12:43", "13:24", "13:42", "14:23", "14:32", "21:34", "21:43", "23:14", and "23:41". Of these times, "23:41" is the latest.

Example 2:
Input: arr = [5,5,5,5]
Output: ""
Explanation: There are no valid 24-hour times as "55:55" is not valid.
"""

# Runtime 11 ms Beats 85.29% of users with Python
# Memory 11.78 MB Beats 26.47% of users with Python

from icecream import ic
from itertools import permutations
# def largestTimeFromDigits2(arr):
#     """
#     :type arr: List[int]
#     :rtype: str
#     """
#     mt="23:59"
#     ns=""
#     arrs = sorted(arr, reverse=True)
#     ic(arrs)
#     if 2 in arrs and arrs[1] <= 3:
#         nn=2
#     elif 1 in arrs:
#         nn=1
#     elif 0 in arrs:
#         nn = 0
#     else: return ""
#
#     for i in range(nn,-1,-1):
#         if i in arr: ns=str(i); arr.remove(i); break
#     ic(1,arr)
#     if ns=="2": nn=3
#     else: nn=9
#     for i in range(nn,-1,-1):
#         if i in arr: ns=ns+str(i); arr.remove(i); break
#     ic(2,arr)
#
#     ns=ns+":"
#     for i in range(5,-1,-1):
#         if i in arr: ns=ns+str(i); arr.remove(i); break
#     ic(3,arr)
#
#     for i in range(9,-1,-1):
#         if i in arr: ns=ns+str(i); arr.remove(i); break
#     ic(4,arr)
#     if len(ns)<5 and len(arr) !=0: ns=ns+str(arr[0])
#     if ns>"23:59": return ""
#     else: return ns

def largestTimeFromDigits(arr):
    arrs=[str(i) for i in arr]
    lst=sorted(list(permutations(arrs,4)),reverse=True)
    lst2 = [s1[0]+s1[1]+":"+s1[2]+s1[3] for s1 in lst]
    for i in lst2:
        if i<"23:59" and i[3:]<"60": return i
    return ""



ic(largestTimeFromDigits([1,9,6,0]))
# ic(largestTimeFromDigits([0,0,1,0]))
# ic(largestTimeFromDigits([9,0,7,7]))
# ic(largestTimeFromDigits([5,5,5,5]))


