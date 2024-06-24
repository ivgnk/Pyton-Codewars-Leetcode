"""
Done 24.06.2024. Topics: Array, Hash Table
3162. Find the Number of Good Pairs I
https://leetcode.com/problems/find-the-number-of-good-pairs-i/description/

You are given 2 integer arrays nums1 and nums2 of lengths n and m respectively. You are also given a positive integer k.
A pair (i, j) is called good if nums1[i] is divisible by nums2[j] * k (0 <= i <= n - 1, 0 <= j <= m - 1).
Return the total number of good pairs.

Example 1:
Input: nums1 = [1,3,4], nums2 = [1,3,4], k = 1
Output: 5
Explanation:
The 5 good pairs are (0, 0), (1, 0), (1, 1), (2, 0), and (2, 2).

Example 2:
Input: nums1 = [1,2,4,12], nums2 = [2,4], k = 3
Output: 2
Explanation:
The 2 good pairs are (3, 0) and (3, 1).

Constraints:
1 <= n, m <= 50
1 <= nums1[i], nums2[j] <= 50
1 <= k <= 50

Hint 1
The constraints are small. Check all pairs.
"""

# Runtime 31 ms Beats 76.26%
# Memory 11.56 MB Beats 59.43%

def numberOfPairs(nums1, nums2, k):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :type k: int
    :rtype: int
    """
    ll1=len(nums1); ll2=len(nums2)
    n=0
    for i in range(ll1):
        for j in range(ll2):
            if nums1[i]%(nums2[j]*k)==0:
                n=n+1
    return n

print(numberOfPairs(nums1 = [1,3,4], nums2 = [1,3,4], k = 1))
print(numberOfPairs(nums1 = [1,2,4,12], nums2 = [2,4], k = 3))


