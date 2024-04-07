'''
1995. Count Special Quadruplets
https://leetcode.com/problems/count-special-quadruplets/description/

Given a 0-indexed integer array nums, return the number of distinct quadruplets (a, b, c, d) such that:
nums[a] + nums[b] + nums[c] == nums[d], and
a < b < c < d

Example 1:
Input: nums = [1,2,3,6]
Output: 1
Explanation: The only quadruplet that satisfies the requirement is (0, 1, 2, 3) because 1 + 2 + 3 == 6.

Example 2:
Input: nums = [3,3,6,4,5]
Output: 0
Explanation: There are no such quadruplets in [3,3,6,4,5].

Example 3:
Input: nums = [1,1,1,3,5]
Output: 4
Explanation: The 4 quadruplets that satisfy the requirement are:
- (0, 1, 2, 3): 1 + 1 + 1 == 3
- (0, 1, 3, 4): 1 + 1 + 3 == 5
- (0, 2, 3, 4): 1 + 1 + 3 == 5
- (1, 2, 3, 4): 1 + 1 + 3 == 5
'''

# Runtime 1010 ms Beats 48.21% of users with Python
# Memory 11.58 MB Beats 60.71%# of users with Python

def countQuadruplets(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = 0;  ll = len(nums)
    for i in range(ll):
        for j in range(i+1, ll):
            for k in range(j+1, ll):
                for l in range(k + 1, ll):
                    if nums[i] + nums[j] + nums[k] == nums[l]:
                            n += 1
    return n

print(countQuadruplets([1,2,3,6]))