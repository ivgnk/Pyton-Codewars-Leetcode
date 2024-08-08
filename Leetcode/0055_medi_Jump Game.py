"""
08.08.08. Topics: Array, Dynamic Programming

55. Jump Game
https://leetcode.com/problems/jump-game/description/

You are given an integer array nums. You are initially positioned at the array's first index,
and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

Example 1:
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.


Constraints:
1 <= nums.length <= 104
0 <= nums[i] <= 105
"""

# https://leetcode.com/problems/jump-game/solutions/4534808/super-simple-intuitive-8-line-python-solution-beats-99-92-of-users/
# Imagine you have a car, and you have some distance to travel (the length of the array).
# This car has some amount of gasoline, and as long as it has gasoline,
# it can keep traveling on this road (the array).
# Every time we move up one element in the array, we subtract one unit of gasoline.
# However, every time we find an amount of gasoline that is greater than our current amount,
# we "gas up" our car by replacing our current amount of gasoline with this new amount.
# We keep repeating this process until we either run out of gasoline (and return false),
# or we reach the end with just enough gasoline (or more to spare), in which case we return true.
# Note: We can let our gas tank get to zero as long as we are able to gas up at that immediate location
# (element in the array) that our car is currently at.

def canJump2(nums):
    gas = 0
    for n in nums:
        if gas < 0:
            return False
        elif n > gas:
            gas = n
        gas -= 1

    return True

# https://leetcode.com/problems/jump-game/solutions/5593683/simple-solution-with-diagrams-in-1-min-video-c-java-python-js/
def canJump(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    target_num_index = len(nums) - 1
    for i in range(len(nums) - 2, -1, -1):
        if target_num_index <= i + nums[i]:
            target_num_index = i
    return target_num_index == 0

print(canJump([2,3,1,1,4]))