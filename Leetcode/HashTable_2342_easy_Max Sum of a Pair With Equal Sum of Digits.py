"""
Done 13.02.2025. Topics: Hash Table
2342. Max Sum of a Pair With Equal Sum of Digits
https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits

You are given a 0-indexed array nums consisting of positive integers.
You can choose two indices i and j, such that i != j,
and the sum of digits of the number nums[i] is equal to that of nums[j].

Return the maximum value of nums[i] + nums[j] that you can obtain over all possible
indices i and j that satisfy the conditions.

Example 1:
Input: nums = [18,43,36,13,7]
Output: 54
Explanation: The pairs (i, j) that satisfy the conditions are:
- (0, 2), both numbers have a sum of digits equal to 9, and their sum is 18 + 36 = 54.
- (1, 4), both numbers have a sum of digits equal to 7, and their sum is 43 + 7 = 50.
So the maximum sum that we can obtain is 54.

Example 2:
Input: nums = [10,12,19,14]
Output: -1
Explanation: There are no two numbers that satisfy the conditions, so we return -1.

Constraints:
1 <= nums.length <= 105
1 <= nums[i] <= 109

Hint 1
What is the largest possible sum of digits a number can have?
Hint 2
Group the array elements by the sum of their digits,
and find the largest two elements of each group.

Mu solution: Easy Python solution for Problem 2342 without Heap (Priority Queue)
https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/solutions/6414652/easy-python-solution-for-problem-2342-wi-fnbv/
Intuition
Use Hash Table & Hints
"""
# Time Complexity O(NLogN)
# Space Complexity O(N)
# Runtime 1258 ms Beats 22.47%
# Memory 21.82 MB Beats 46.07%
def maximumSum(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    dd=dict()
    for n in nums:
        s1=sum([int(ss) for ss in str(n)])
        if s1 in dd:
            dd[s1].append(n)
        else:
            dd[s1]=[n]
    mmax=-1
    for v in dd.values():
        if len(v)>1:
            v.sort(reverse=True)
            mmax=max(mmax,v[0]+v[1])
    return mmax

print(maximumSum([18,43,36,13,7]))
print(maximumSum([10,12,19,14]))
