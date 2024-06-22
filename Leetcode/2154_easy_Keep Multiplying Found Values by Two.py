"""
Done 22.06.2024. Topics: Array
2154. Keep Multiplying Found Values by Two
https://leetcode.com/problems/keep-multiplying-found-values-by-two/description/

You are given an array of integers nums. You are also given an integer original which
is the first number that needs to be searched for in nums.

You then do the following steps:

If original is found in nums, multiply it by two (i.e., set original = 2 * original).
Otherwise, stop the process.
Repeat this process with the new number as long as you keep finding the number.
Return the final value of original.

Example 1:
Input: nums = [5,3,6,1,12], original = 3
Output: 24
Explanation:
- 3 is found in nums. 3 is multiplied by 2 to obtain 6.
- 6 is found in nums. 6 is multiplied by 2 to obtain 12.
- 12 is found in nums. 12 is multiplied by 2 to obtain 24.
- 24 is not found in nums. Thus, 24 is returned.

Example 2:
Input: nums = [2,7,9], original = 4
Output: 4
Explanation:
- 4 is not found in nums. Thus, 4 is returned.

Repeatedly iterate through the array and check if the current value of original is in the array.
Hint 2
If original is not found, stop and return its current value.
Hint 3
Otherwise, multiply original by 2 and repeat the process.
Hint 4
Use set data structure to check the existence faster.
"""

# Runtime 40 ms Beats 62.86%
# Memory 11.65 MB Beats 80.48%
# Runtime 38 ms Beats 77.62%
# Memory 11.80 MB Beats 44.76%

def findFinalValue(nums, original):
    """
    :type nums: List[int]
    :type original: int
    :rtype: int
    """
    while original in nums:
        original=original*2
    return original




