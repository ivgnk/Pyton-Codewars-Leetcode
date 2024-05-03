"""
Done 03.05.2024
2367. Number of Arithmetic Triplets
https://leetcode.com/problems/number-of-arithmetic-triplets/

You are given a 0-indexed, strictly increasing integer array nums and a positive integer diff.
A triplet (i, j, k) is an arithmetic triplet if the following conditions are met:
i < j < k,
nums[j] - nums[i] == diff, and
nums[k] - nums[j] == diff.
Return the number of unique arithmetic triplets.

Example 1:
Input: nums = [0,1,4,6,7,10], diff = 3
Output: 2
Explanation:
(1, 2, 4) is an arithmetic triplet because both 7 - 4 == 3 and 4 - 1 == 3.
(2, 4, 5) is an arithmetic triplet because both 10 - 7 == 3 and 7 - 4 == 3.

Example 2:
Input: nums = [4,5,6,7,8,9], diff = 2
Output: 2
Explanation:
(0, 2, 4) is an arithmetic triplet because both 8 - 6 == 2 and 6 - 4 == 2.
(1, 3, 5) is an arithmetic triplet because both 9 - 7 == 2 and 7 - 5 == 2.
"""


# Runtime 1001 ms Beats 37.68% of users with Python
# Memory 11.66 MB Beats 41.45% of users with Python
def arithmeticTriplets1(nums, diff):
    """
    :type nums: List[int]
    :type diff: int
    :rtype: int
    """
    n=0; ll=len(nums)
    for i in range(ll):
        for j in range(i+1,ll):
            for k in range(j+1,ll):
                if nums[j] - nums[i] == diff and nums[k] - nums[j] == diff:
                    n=n+1
    return n

# Runtime 52 ms Beats 44.64% of users with Python
# Memory 11.56 MB Beats 73.04% of users with Python
# Runtime 50 ms Beats 46.96% of users with Python
# Memory 11.72 MB Beats 13.33% of users with Python
def arithmeticTriplets2(nums, diff):
    """
    :type nums: List[int]
    :type diff: int
    :rtype: int
    """
    n=0; ll=len(nums)
    for i in range(ll):
        for j in range(i+1,ll):
            if nums[j] - nums[i] == diff:
                for k in range(j+1,ll):
                    if nums[k] - nums[j] == diff:
                        n=n+1
    return n

# Runtime 42 ms Beats 48.41% of users with Python
# Memory 11.44 MB Beats 93.91% of users with Python
def arithmeticTriplets(nums, diff):
    """
    :type nums: List[int]
    :type diff: int
    :rtype: int
    """
    ll=len(nums)
    return sum([1
                    for i in range(ll)
                        for j in range(i+1,ll)
                            if nums[j] - nums[i] == diff
                                for k in range(j + 1, ll) if nums[k] - nums[j] == diff
                ])


print(arithmeticTriplets(nums = [0,1,4,6,7,10], diff = 3))
print(arithmeticTriplets(nums = [4,5,6,7,8,9], diff = 2))
