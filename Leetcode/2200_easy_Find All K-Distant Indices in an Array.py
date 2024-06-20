"""
Done 20.06.2024. Topics: Array, Two Pointers

2200. Find All K-Distant Indices in an Array
https://leetcode.com/problems/find-all-k-distant-indices-in-an-array/

You are given a 0-indexed integer array nums and two integers key and k.
A k-distant index is an index i of nums for which there exists at least one index j
such that |i - j| <= k and nums[j] == key.
Return a list of all k-distant indices sorted in increasing order.

Example 1:
Input: nums = [3,4,9,1,3,9,5], key = 9, k = 1
Output: [1,2,3,4,5,6]
Explanation: Here, nums[2] == key and nums[5] == key.
- For index 0, |0 - 2| > k and |0 - 5| > k, so there is no j where |0 - j| <= k and nums[j] == key. Thus, 0 is not a k-distant index.
- For index 1, |1 - 2| <= k and nums[2] == key, so 1 is a k-distant index.
- For index 2, |2 - 2| <= k and nums[2] == key, so 2 is a k-distant index.
- For index 3, |3 - 2| <= k and nums[2] == key, so 3 is a k-distant index.
- For index 4, |4 - 5| <= k and nums[5] == key, so 4 is a k-distant index.
- For index 5, |5 - 5| <= k and nums[5] == key, so 5 is a k-distant index.
- For index 6, |6 - 5| <= k and nums[5] == key, so 6 is a k-distant index.
Thus, we return [1,2,3,4,5,6] which is sorted in increasing order.

Example 2:
Input: nums = [2,2,2,2,2], key = 2, k = 2
Output: [0,1,2,3,4]
Explanation: For all indices i in nums, there exists some index j such that |i - j| <= k and nums[j] == key, so every index is a k-distant index.
Hence, we return [0,1,2,3,4].

Hint 1
For every occurrence of key in nums, find all indices within distance k from it.
Hint 2
Use a hash table to remove duplicate indices.
"""

# Runtime 44 ms Beats 88.14% Time Complexity O(N)
# Memory 11.80 MB Beats 86.44%  Space Complexity O(N)

from icecream import  ic
def findKDistantIndices(nums, key, k):
    """
    :type nums: List[int]
    :type key: int
    :type k: int
    :rtype: List[int]
    """
    ll=len(nums)
    rll=range(ll)
    if all([i==key for i in nums]):
        return [i for i in rll]
    nn=[i for i in rll if nums[i]==key]
    # ic(nn)
    res=[]
    for i in range(len(nn)):
        rn=range(nn[i]-k,nn[i]+k+1)
        # ic(i,list(rn))
        res=res+[j for j in rn if j>-1 and j<ll ]
    # ic(res)
    res=sorted(set(res))
    return res

# ic(findKDistantIndices(nums = [3,4,9,1,3,9,5], key = 9, k = 1))
ic(findKDistantIndices(nums = [1,1000,1,1000], key =1000, k = 4))