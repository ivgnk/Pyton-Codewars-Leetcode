"""
Done 18.08.2024. Topics: Array, Hash Table
1394. Find Lucky Integer in an Array
https://leetcode.com/problems/find-lucky-integer-in-an-array/description/

Given an array of integers arr, a lucky integer is an integer
that has a frequency in the array equal to its value.
Return the largest lucky integer in the array. If there is no lucky integer return -1.

Example 1:
Input: arr = [2,2,3,4]
Output: 2
Explanation: The only lucky number in the array is 2 because frequency[2] == 2.

Example 2:
Input: arr = [1,2,2,3,3,3]
Output: 3
Explanation: 1, 2 and 3 are all lucky numbers, return the largest of them.

Example 3:
Input: arr = [2,2,2,3,3]
Output: -1
Explanation: There are no lucky numbers in the array.

Solution
✏️ Easy Python solution with dictionary, sorting & list  comprehension
Intuition
The conditions of the problem assume the use of a dictionary.

Approach
The dictionary needs to be sorted.
Done 18.08.2024.
Runtime 33 ms Beats 81.02%
Memory 11.84 MB Beats 15.30%
"""

# Runtime 36 ms Beats 62.04%
# Memory 11.87 MB Beats 15.30%
# Runtime 33 ms Beats 81.02%
# Memory 11.84 MB Beats 15.30%
def findLucky(arr):
    """
    :type arr: List[int]
    :rtype: int
    """
    dd=dict()
    for d in arr:
        if d in dd:
            dd[d]=dd[d]+1
        else:
            dd[d] = 1

    r = sorted([k for k,v in dd.items() if k==v],reverse=True)
    if r==[]:
        return -1
    else:
        return r[0]