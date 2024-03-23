'''
1089. Duplicate Zeros
https://leetcode.com/problems/duplicate-zeros/

Given a fixed-length integer array arr, duplicate each occurrence of zero,
shifting the remaining elements to the right.
Note that elements beyond the length of the original array are not written.
Do the above modifications to the input array in place and do not return anything.

Example 1:
Input: arr = [1,0,2,3,0,4,5,0]
Output: [1,0,0,2,3,0,0,4]
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]

Example 2:
Input: arr = [1,2,3]
Output: [1,2,3]
Explanation: After calling your function, the input array is modified to: [1,2,3]
'''

# Runtime 61 ms
# Beats 18.73% of users with Python
# Memory 12.03 MB
# Beats 44.88% of users with Python

def duplicateZeros(arr):
    """
    :type arr: List[int]
    :rtype: None Do not return anything, modify arr in-place instead.
    """
    i=0
    deli= len(arr)
    while i<deli-1:
        print(arr[i])
        if (arr[i] == 0):
            del arr[deli-1]
            arr.insert(i+1,0)
            print(arr)
            i = i+2
        else: i=i+1

duplicateZeros([1,0,2,3,0,4,5,0])