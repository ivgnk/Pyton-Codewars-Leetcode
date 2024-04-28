"""
Done 29.04.2024
2099. Find Subsequence of Length K With the Largest Sum
https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/description/
You are given an integer array nums and an integer k. You want to find a subsequence of nums of length k that has the largest sum.
Return any such subsequence as an integer array of length k.
A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

Example 1:
Input: nums = [2,1,3,3], k = 2
Output: [3,3]
Explanation:
The subsequence has the largest sum of 3 + 3 = 6.

Example 2:
Input: nums = [-1,-2,3,4], k = 3
Output: [-1,3,4]
Explanation:
The subsequence has the largest sum of -1 + 3 + 4 = 6.

Example 3:
Input: nums = [3,4,3,3], k = 2
Output: [3,4]
Explanation:
The subsequence has the largest sum of 3 + 4 = 7.
Another possible subsequence is [4, 3].
"""

# Runtime 42 ms Beats 30.34% of users with Python
# Memory 12.02 MB Beats 21.35% of users with Python

# https://pythonim.ru/osnovy/perestanovki-kombinatsii-python
from itertools import combinations
from heapq import nlargest
def maxSubsequence(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    if k == len(nums): return nums
    rr = nlargest(k, nums)
    res = [];    curr = 0
    for i in nums:
        if i in rr and curr < k:
            curr += 1
            res.append(i)
            rr.remove(i)
    return res

    # comb = list(combinations(nums, k))
    # ssum = [sum(x) for x in comb]
    # # print(comb);   print(ssum)
    # mmax=max(ssum); ind = ssum.index(mmax)
    # return list(comb[ind])
    # ------
    # if k==len(nums): return nums
    # n = sorted(nums)[-k:]
    # res=[]; curr=0
    # for i in nums:
    #     if i in n and curr<k:
    #         curr+=1
    #         res.append(i)
    # return res


    # if k == len(nums): return nums
    # n = sorted(nums);    n = n[-k:]
    # mmin = min(n);    mmin = min(0, mmin)
    # nums1 = [i for i in nums if i >= mmin]
    # # print('nums1=', nums1)
    # res=[]
    # for i in range

# print(maxSubsequence(nums = [-16,-13,8,16,35,-17,30,-8,34,-2,-29,-35,15,13,-30,-34,6,15,28,-23,34,28,-24,15,-17,10,31,32,-3,-36,19,31,-5,-21,-33,-18,-23,-37,-15,12,-28,-40,1,38,38,-38,33,-35,-28,-40,4,-15,-29,-33,-18,-9,-29,20,1,36,-8,23,-34,16,-7,13,39,38,7,-7,-10,30,9,26,27,-37,-18,-25,14,-36,23,28,-15,35,-9,1], k = 8))
# print(maxSubsequence(nums = [3,4,3,3], k = 2))
# print(maxSubsequence(nums = [2,1,3,3], k = 2))
# print(maxSubsequence(nums = [-1,-2,3,4], k = 3))
# print(maxSubsequence(nums = [-76,-694,44,197,357,-833,-277,358,724,-585,-960,214,465,-593,-431,625,-83,58,-889,31,765,8,-17,476,992,803,863,242,379,561,673,526,-447], k =14))

rr=[39, 38, 38, 38, 36, 35, 35, 34]
rr.remove(38)
print(rr)
