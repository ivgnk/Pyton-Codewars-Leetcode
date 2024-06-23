"""
23.06.2024. Topics: Array, Sliding Window, Sorting, Bucket Sort

220. Contains Duplicate III
https://leetcode.com/problems/contains-duplicate-iii/description/

You are given an integer array nums and two integers indexDiff and valueDiff.
Find a pair of indices (i, j) such that:
i != j,
abs(i - j) <= indexDiff.
abs(nums[i] - nums[j]) <= valueDiff, and
Return true if such pair exists or false otherwise.

Example 1:
Input: nums = [1,2,3,1], indexDiff = 3, valueDiff = 0
Output: true
Explanation: We can choose (i, j) = (0, 3).
We satisfy the three conditions:
i != j --> 0 != 3
abs(i - j) <= indexDiff --> abs(0 - 3) <= 3
abs(nums[i] - nums[j]) <= valueDiff --> abs(1 - 1) <= 0

Example 2:
Input: nums = [1,5,9,1,5,9], indexDiff = 2, valueDiff = 3
Output: false
Explanation: After trying all the possible pairs (i, j), we cannot satisfy the three conditions, so we return false.

Hint 1
Time complexity O(n logk) - This will give an indication that sorting is involved for k elements.
Hint 2
Use already existing state to evaluate next state - Like, a set of k sorted numbers are only needed to be tracked.
When we are processing the next number in array, then we can utilize the existing sorted state and
it is not necessary to sort next overlapping set of k numbers again.
"""

# Time Limit Exceeded - 36 / 52 testcases passed
# ll = 20000
def containsNearbyAlmostDuplicate2(nums, indexDiff, valueDiff):
    ll = len(nums)
    print(ll)
    for i in range(ll):
        for j in range(i + 1, ll):
            if j - i <= indexDiff and abs(nums[i] - nums[j]) <= valueDiff:
                return True
    return False

# Runtime 785 ms Beats 53.85%
# Memory 34.21 MB Beats 41.92%
# Time: O(n)
# Space: O((max(nums)−min(nums))/t)→O(k)
# https://walkccc.me/LeetCode/problems/220/#__tabbed_2_3
def containsNearbyAlmostDuplicate(nums, indexDiff, valueDiff):
    """
    :type nums: List[int]
    :type indexDiff: int
    :type valueDiff: int
    :rtype: bool
    """
    if not nums or indexDiff <= 0 or valueDiff < 0:
        return False

    mini = min(nums)
    diff = valueDiff + 1  # In case that `valueDiff` equals 0.
    bucket = {}

    def getKey(num: int) -> int:
        return (num - mini) // diff

    for i, num in enumerate(nums):
        key = getKey(num)
        if key in bucket:  # the current bucket
            return True
        # the left adjacent bucket
        if key - 1 in bucket and num - bucket[key - 1] < diff:
            return True
        # the right adjacent bucket
        if key + 1 in bucket and bucket[key + 1] - num < diff:
            return True
        bucket[key] = num
        if i >= indexDiff:
            del bucket[getKey(nums[i - indexDiff])]

    return False


print(containsNearbyAlmostDuplicate(nums = [1,5,9,1,5,9], indexDiff = 2, valueDiff = 3))