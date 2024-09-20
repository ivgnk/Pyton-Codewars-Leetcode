"""
Done 20.09.2024. Topics: Array, Greedy
3282. Reach End of Array With Max Score
https://leetcode.com/problems/reach-end-of-array-with-max-score/description/

You are given an integer array nums of length n.
Your goal is to start at index 0 and reach index n - 1.
You can only jump to indices greater than your current index.
The score for a jump from index i to index j is calculated as (j - i) * nums[i].
Return the maximum possible total score by the time you reach the last index.

Example 1:
Input: nums = [1,3,1,5]
Output: 7
Explanation:
First, jump to index 1 and then jump to the last index. The final score is 1 * 1 + 2 * 3 = 7.

Example 2:
Input: nums = [4,3,1,3,2]
Output: 16
Explanation:
Jump directly to the last index. The final score is 4 * 4 = 16.

Constraints:
1 <= nums.length <= 105
1 <= nums[i] <= 105

Hint 1
It can be proven that from each index i, the optimal solution is to jump
to the nearest index j > i such that nums[j] > nums[i].
"""

# Wrong Answer - 255 / 626 testcases passed
# nums = [1,6,1]
# Output 1
# Expected 7
def findMaximumScore2(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n=0; i=0
    ll=len(nums)
    for j in range(1,ll):
        if nums[j]>nums[i]:
            n+=nums[i]*(j-i)
            i=j
    if n==0: n=nums[0]*(ll-1)
    return n

# Runtime 2693 ms Beats 23.14%
# Memory 24.26 MB Beats 88.43%
# Runtime 2690 ms Beats 23.14%
# Memory 24.59 MB Beats 17.91%
def findMaximumScore(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = 0; i = 0
    ll = len(nums);   ll1 = ll - 1
    last = False
    for j in range(1, ll):
        if nums[j] > nums[i]:
            n += nums[i] * (j - i)
            i = j
            if i == ll1: last = True
    if not last:
        if i==0:
            n = nums[0] * ll1
        else:
            n+= nums[i] * (ll1-i)
    return n


print(findMaximumScore([1,3,1,5]))
print(findMaximumScore([4,3,1,3,2]))
print(findMaximumScore([1,6,1]))
