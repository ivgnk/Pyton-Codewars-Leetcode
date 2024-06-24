"""
Done 24.06.2024. Topics: Array, Sorting
2475. Number of Unequal Triplets in Array
https://leetcode.com/problems/number-of-unequal-triplets-in-array/description/

You are given a 0-indexed array of positive integers nums.
Find the number of triplets (i, j, k) that meet the following conditions:
0 <= i < j < k < nums.length
nums[i], nums[j], and nums[k] are pairwise distinct.
In other words, nums[i] != nums[j], nums[i] != nums[k], and nums[j] != nums[k].
Return the number of triplets that meet the conditions.

Example 1:
Input: nums = [4,4,2,4,3]
Output: 3
Explanation: The following triplets meet the conditions:
- (0, 2, 4) because 4 != 2 != 3
- (1, 2, 4) because 4 != 2 != 3
- (2, 3, 4) because 2 != 4 != 3
Since there are 3 triplets, we return 3.
Note that (2, 0, 4) is not a valid triplet because 2 > 0.

Example 2:
Input: nums = [1,1,1,1,1]
Output: 0
Explanation: No triplets meet the conditions so we return 0.

Constraints:
3 <= nums.length <= 100
1 <= nums[i] <= 1000

Hint 1
The constraints are very small. Can we try every triplet?
Hint 2
Yes, we can. Use three loops to iterate through all the possible triplets, ensuring the condition i < j < k holds.
"""


# Runtime 414 ms Beats 64.71%
# Memory 11.51 MB Beats 66.18%
# Runtime 411 ms Beats 70.59%
# Memory 11.66 MB Beats 27.94%

def unequalTriplets(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ll=len(nums); n=0
    for i in range(ll):
        for j in range(i+1,ll):
            for k in range(j + 1, ll):
                if (nums[i] != nums[j]) and (nums[i] != nums[k]) and (nums[j] != nums[k]):
                    n=n+1
    return n


print(unequalTriplets([4,4,2,4,3]))
print(unequalTriplets([1,1,1,1,1]))

