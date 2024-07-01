"""
Done 01.07.2024. Topics: Array
1550. Three Consecutive Odds
https://leetcode.com/problems/three-consecutive-odds/description/

Given an integer array arr, return true if there are three consecutive odd numbers in the array.
Otherwise, return false.

Example 1:
Input: arr = [2,6,4,1]
Output: false
Explanation: There are no three consecutive odds.

Example 2:
Input: arr = [1,2,34,3,4,5,7,23,12]
Output: true
Explanation: [5,7,23] are three consecutive odds.

Constraints:
1 <= arr.length <= 1000
1 <= arr[i] <= 1000

Hint 1
Check every three consecutive numbers in the array for parity.
"""

# Runtime 23 ms Beats 84.58%
# Time Complexity O(N)
# Memory 11.63 MB Beats 65.42%
# Space Complexity O(1)

def threeConsecutiveOdds(arr):
    """
    :type arr: List[int]
    :rtype: bool
    """
    ll=len(arr)
    i=0
    while i<=ll-3:
        a1 = arr[i]%2 !=0
        a2 = arr[i+1]%2 !=0
        a3 = arr[i+2]%2 !=0
        if a1 and a2 and a3: return True
        else:
            if a2 and a3: i=i+1
            elif a3: i=i+2
            else: i=i+3
    return False

print(threeConsecutiveOdds([2,6,4,1]))
print(threeConsecutiveOdds([1,2,34,3,4,5,7,23,12]))
print(threeConsecutiveOdds([1,1,1]))
