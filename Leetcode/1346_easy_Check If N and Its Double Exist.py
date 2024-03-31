'''
1346. Check If N and Its Double Exist
https://leetcode.com/problems/check-if-n-and-its-double-exist/description/

Given an array arr of integers, check if there exist two indices i and j such that :
i != j
0 <= i, j < arr.length
arr[i] == 2 * arr[j]

Example 1:
Input: arr = [10,2,5,3]
Output: true
Explanation: For i = 0 and j = 2, arr[i] == 10 == 2 * 5 == 2 * arr[j]

Example 2:
Input: arr = [3,1,7,11]
Output: false
Explanation: There is no i and j that satisfy the conditions.
'''

# Runtime 37 ms Beats 55.89% of users with Python
# Memory 11.63 MB Beats 71.67% of users with Python

def checkIfExist(arr):
    """
    :type arr: List[int]
    :rtype: bool
    """
    # llen=len(arr)
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == 2 * arr[j]:
                return True
            elif arr[j] == 2 * arr[i]:
                return True
    return False

print(checkIfExist([7,1,14,11]))