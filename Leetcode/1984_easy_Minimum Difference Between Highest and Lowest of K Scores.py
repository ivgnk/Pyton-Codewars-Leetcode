'''
11.05.2024. Topics: Array, Sliding Window, Sorting

1984. Minimum Difference Between Highest and Lowest of K Scores
You are given a 0-indexed integer array nums, where nums[i] represents the score of the ith student.
You are also given an integer k.
Pick the scores of any k students from the array so that
the difference between the highest and the lowest of the k scores is minimized.

Return the minimum possible difference.

Example 1:
Input: nums = [90], k = 1
Output: 0
Explanation: There is one way to pick score(s) of one student:
- [90]. The difference between the highest and lowest score is 90 - 90 = 0.
The minimum possible difference is 0.

Example 2:
Input: nums = [9,4,1,7], k = 2
Output: 2
Explanation: There are six ways to pick score(s) of two students:
- [9,4,1,7]. The difference between the highest and lowest score is 9 - 4 = 5.
- [9,4,1,7]. The difference between the highest and lowest score is 9 - 1 = 8.
- [9,4,1,7]. The difference between the highest and lowest score is 9 - 7 = 2.
- [9,4,1,7]. The difference between the highest and lowest score is 4 - 1 = 3.
- [9,4,1,7]. The difference between the highest and lowest score is 7 - 4 = 3.
- [9,4,1,7]. The difference between the highest and lowest score is 7 - 1 = 6.
The minimum possible difference is 2.
'''

# Runtime 72 ms Beats 48.73% of users with Python
# Memory 11.85 MB Beats 34.01% of users with Python
# Decison from https://leetcode.com/u/TovAm/
# https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/solutions/1549490/python-simple-solution/
# Не надо искать максимум и минимум, отдельно, т.к. массив отсортирован

def minimumDifference(nums, k):
    if len(nums) <= 1:   return 0
    nums = sorted(nums)
    res = nums[k - 1] - nums[0]
    for i in range(k, len(nums)):
        res = min(res, nums[i] - nums[i - k + 1])
    return res

# Runtime 146 ms Beats 5.26% of users with Python
# Memory 11.67 MB Beats 93.68% of users with Python
def minimumDifference3(nums, k):
    nums=sorted(nums)
    gldiff = int(1e38)
    print(nums)
    for i in range(len(nums)-k+1):
        s = nums[i:i+k]
        mmin = min(s)
        mmax = max(s)
        print(s,mmax,mmax)
        if mmax - mmin < gldiff:
            gldiff = mmax - mmin
    return gldiff


# Time Limit Exceeded  15 / 118 testcases passed
def minimumDifference2(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    import itertools
    gldiff = int(1e38)
    for comb in itertools.combinations(nums, k):
        mmin = min(comb)
        mmax = max(comb)
        if mmax - mmin < gldiff:
            gldiff = mmax - mmin
    return gldiff

print(minimumDifference(nums = [9,4,1,7], k = 2))