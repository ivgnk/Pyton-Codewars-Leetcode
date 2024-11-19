"""
19.11.2024. Array, Hash Table, Sliding Window
2461. Maximum Sum of Distinct Subarrays With Length K
https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/

You are given an integer array nums and an integer k.
Find the maximum subarray sum of all the subarrays of nums that meet the following conditions:
- The length of the subarray is k, and
- All the elements of the subarray are distinct.
Return the maximum subarray sum of all the subarrays that meet the conditions.
If no subarray meets the conditions, return 0.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
Input: nums = [1,5,4,2,9,9,9], k = 3
Output: 15
Explanation: The subarrays of nums with length 3 are:
- [1,5,4] which meets the requirements and has a sum of 10.
- [5,4,2] which meets the requirements and has a sum of 11.
- [4,2,9] which meets the requirements and has a sum of 15.
- [2,9,9] which does not meet the requirements because the element 9 is repeated.
- [9,9,9] which does not meet the requirements because the element 9 is repeated.
We return 15 because it is the maximum subarray sum of all the subarrays that meet the conditions

Example 2:
Input: nums = [4,4,4], k = 3
Output: 0
Explanation: The subarrays of nums with length 3 are:
- [4,4,4] which does not meet the requirements because the element 4 is repeated.
We return 0 because no subarrays meet the conditions.

Constraints:
1 <= k <= nums.length <= 105
1 <= nums[i] <= 105

Hint 1
Which elements change when moving from the subarray of size k that ends at index i
to the subarray of size k that ends at index i + 1?
Hint 2
Only two elements change, the element at i + 1 is added into the subarray,
and the element at i - k + 1 gets removed from the subarray.
Hint 3
Iterate through each subarray of size k and keep track of the sum of
the subarray and the frequency of each element.
"""
# Time Limit Exceeded - 66 / 93 testcases passed
def maximumSubarraySum2(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    maxs=0
    for i in range(len(nums)-k+1):
        s=nums[i:i+k]
        if len(s)==len(set(s)):
            maxs=max(maxs,sum(s))
    return maxs

# Time Limit Exceeded - 63 / 93 testcases passed
def maximumSubarraySum2(nums, k):
    maxs = 0
    for i in range(len(nums) - k + 1):
        s = nums[i:i + k]
        dd = dict()
        for s1 in s:
            if s1 in dd:
                dd[s1] += 1
            else:
                dd[s1] = 1
        if all(v == 1 for v in dd.values()):
            maxs = max(maxs, sum(s))
        print(i, s, maxs)
    return maxs

# Time Limit Exceeded - 63 / 93 testcases passed
def maximumSubarraySum3(nums, k):
    maxs=0
    dd = dict(); ssum=0
    for i in range(len(nums)-k+1):
        s = nums[i:i + k]
        if dd==dict():
            for s1 in s:
                if s1 in dd: dd[s1]+=1
                else: dd[s1]=1
            ssum=sum(s)
        else:
            dd[nums[i-1]]-=1
            dd[nums[i+k-1]]=dd.get(nums[i+k-1],0)+1
            ssum=ssum-nums[i-1]+nums[i+k-1]
        if all(v==1 for v in dd.values() if v !=0):
            maxs=max(maxs,ssum)
        # print(i, s, dd, maxs)
    return maxs

def maximumSubarraySum4(nums, k):
    maxs=0
    dd = dict(); ssum=0; allv=False
    for i in range(len(nums)-k+1):
        s = nums[i:i + k]
        if dd==dict():
            for s1 in s:
                if s1 in dd: dd[s1]+=1
                else: dd[s1]=1
            ssum=sum(s)
        else:
            dd[nums[i-1]]-=1
            n=dd.get(nums[i+k-1],0)
            dd[nums[i+k-1]]=n+1
            ssum=ssum-nums[i-1]+nums[i+k-1]
        if all(v==1 for v in dd.values() if v !=0):
            maxs=max(maxs,ssum)
        # print(i, s, dd, maxs)
    return maxs

def maximumSubarraySum5(nums, k):
    maxs = 0; dd = dict(); s = []
    ssum = 0
    for i in range(len(nums) - k + 1):
        if i == 0:
            s = s + nums[i:i + k]
            for s1 in s:
                if s1 in dd:
                    dd[s1] += 1
                else:
                    dd[s1] = 1
            ssum = sum(s)
            if all(v == 1 for v in dd.values()):
                maxs = max(maxs, ssum)
        else:
            s.pop(0)
            s.append(nums[i + k - 1])
            dd[nums[i - 1]] -= 1
            n = dd.get(nums[i + k - 1], 0)
            dd[nums[i + k - 1]] = n + 1
            ssum = ssum - nums[i - 1] + nums[i + k - 1]
            if n == 0:
                if all(v == 1 for v in dd.values() if v != 0):
                    maxs = max(maxs, ssum)
        # print(i, s, dd, maxs)
    return maxs

# Time Limit Exceeded - # 63 / 93 testcases passed
def maximumSubarraySum6(nums, k):
    maxs=0; dd=dict(); s=[]
    ssum=0; allv=False
    ll=len(nums)
    if ll<k: return 0
    for i in range(ll-k+1):
        if i==0:
            s = s+nums[i:i + k]
            for s1 in s:
                if s1 in dd: dd[s1]+=1
                else: dd[s1]=1
            ssum=sum(s)
            allv=all(v == 1 for v in dd.values())
            if allv: maxs = max(maxs, ssum)
        else:
            s.pop(0)
            s.append(nums[i+k-1])
            dd[nums[i-1]]-=1
            n=dd.get(nums[i+k-1],0)
            dd[nums[i+k-1]]=n+1
            ssum=ssum-nums[i-1]+nums[i+k-1]
            if allv:
                if n==0: maxs=max(maxs,ssum)
            else: # allv=False
                if n==0:
                    allv = all(v==1 for v in dd.values() if v !=0)
                    if allv: maxs=max(maxs,ssum)
    return maxs

# Runtime 275 ms Beats 8.62%
# Memory 25.26 MB Beats 77.29%
import collections
# https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/solutions/2783204/python-solution/
def maximumSubarraySum7(nums, k):
    dic = collections.Counter(nums[:k])
    if max(dic.values()) == 1:
        ans = sum(dic.keys())
    else:
        ans = 0
    tmp = sum(nums[:k])
    for i in range(k, len(nums)):
        dic[nums[i]] += 1
        dic[nums[i - k]] -= 1
        if dic[nums[i - k]] == 0:
            del dic[nums[i - k]]

        tmp = tmp - nums[i - k] + nums[i]
        if len(dic) == k:
            ans = max(ans, tmp)
        # print(dic, tmp, ans)
    return ans

def maximumSubarraySum(self, nums, k):
    max_sum = 0; ll=len(nums)
    if ll < k:  return 0
    dd = {}
    ssum = 0
    for i in range(k):
        if nums[i] in dd:  dd[nums[i]] += 1
        else: dd[nums[i]] = 1
        ssum += nums[i]

    if len(dd) == k:  max_sum = max(max_sum, ssum)

    for i in range(k, ll):
        left_elem = nums[i - k]
        if dd[left_elem] == 1: del dd[left_elem]
        else: dd[left_elem] -= 1

        if nums[i] in dd: dd[nums[i]] += 1
        else: dd[nums[i]] = 1
        ssum += nums[i] - left_elem

        if len(dd) == k:  max_sum = max(max_sum, ssum)
    return max_sum

# https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/editorial/
from typing import List
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        current_sum = 0
        begin = 0
        end = 0
        num_to_index = {}

        while end < len(nums):
            curr_num = nums[end]
            last_occurrence = num_to_index.get(curr_num, -1)
            # if current window already has number or if window is too big, adjust window
            while begin <= last_occurrence or end - begin + 1 > k:
                current_sum -= nums[begin]
                begin += 1
            num_to_index[curr_num] = end
            current_sum += nums[end]
            if end - begin + 1 == k:
                ans = max(ans, current_sum)
            end += 1
        return ans

# print(maximumSubarraySum(nums = [1,5,4,2,9,9,9], k = 3))  # 15
# print(maximumSubarraySum(nums = [4,4,4], k = 3))         # 0
print(maximumSubarraySum(nums = [1,2,2], k = 2))

