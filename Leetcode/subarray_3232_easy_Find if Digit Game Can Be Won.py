"""
31.07.2024. Topics: Array, Math
3232. Find if Digit Game Can Be Won
https://leetcode.com/problems/find-if-digit-game-can-be-won/description/

You are given an array of positive integers nums.

Alice and Bob are playing a game. In the game, Alice can choose either all single-digit numbers or
all double-digit numbers from nums, and the rest of the numbers are given to Bob.
Alice wins if the sum of her numbers is strictly greater than the sum of Bob's numbers.

Return true if Alice can win this game, otherwise, return false.

Example 1:
Input: nums = [1,2,3,4,10]
Output: false
Explanation:
Alice cannot win by choosing either single-digit or double-digit numbers.

Example 2:
Input: nums = [1,2,3,4,5,14]
Output: true
Explanation:
Alice can win by choosing single-digit numbers which have a sum equal to 15.

Example 3:
Input: nums = [5,5,5,25]
Output: true
Explanation:
Alice can win by choosing double-digit numbers which have a sum equal to 25.

Constraints:
1 <= nums.length <= 100
1 <= nums[i] <= 99
"""

# Runtime 38 ms Beats 49.57%
# Memory 11.54 MB Beats 74.45%

# Runtime 33 ms Beats 82.11%
# Time Complexity O(N)
# Memory 11.56 MB Beats 74.45%
# Space Complexity O(1)
def canAliceWin(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    s_all=sum(nums)
    s_nums=[len(str(n)) for n in nums]
    s_single=0; s_double=0
    for i in range(len(nums)):
        if s_nums[i]==1: s_single +=nums[i]
        elif s_nums[i]==2: s_double +=nums[i]
    b_sng=s_all-s_single
    b_dbl=s_all-s_double
    return s_single>b_sng or s_double>b_dbl
