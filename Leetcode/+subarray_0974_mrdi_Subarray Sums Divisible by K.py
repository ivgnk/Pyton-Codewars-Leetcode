"""
Topics: Array, Hash Table, Prefix Sum
974. Subarray Sums Divisible by K
https://leetcode.com/problems/subarray-sums-divisible-by-k/description/?envType=daily-question&envId=2024-06-09

Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.
A subarray is a contiguous part of an array.

Example 1:
Input: nums = [4,5,0,-2,-3,1], k = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by k = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]

Example 2:
Input: nums = [5], k = 9
Output: 0
"""

# Wrong Answer - 43 / 73 testcases passed
def subarraysDivByK(nums, k):
    ll=len(nums)
    if ll==1:
        if nums[0]%k==0: return 1
        else: return 0
    n=0

    s1=nums[:]
    for i in range(1,ll):
        s1[i]=s1[i-1]+nums[i]
    # s2=nums[:]
    # for i in range(ll-2,-1,-1):
    #     s2[i-1]=s2[i]+nums[i-1]

    for i in range(ll):
        for j in range(i+1,ll):
            # if sum(nums[i:j+1])%k==0:
            if (s1[j]-s1[i]) % k == 0:
                n=n+1
                # print(i,j,s1[j]-s1[i])

    for i in range(ll):
        if nums[i]%k==0 and nums[i]!=0: n=n+1
    return n

print(subarraysDivByK([4,5,0,-2,-3,1],5))


# Time Limit Exceeded - 38 / 73 testcases passed
def subarraysDivByK2(nums, k):
    ll=len(nums)
    if ll==1:
        if nums[0]%k==0: return 1
        else: return 0
    n=0

    for i in range(ll):
        for j in range(i,ll):
            if sum(nums[i:j+1])%k==0:
                n=n+1
                print(i,j,nums[i:j+1],sum(nums[i:j+1]))
    return n

print(subarraysDivByK2([4,5,0,-2,-3,1],5))


# Wrong Answer - 25 / 73 testcases passed
def subarraysDivByK3(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    ll=len(nums)
    if ll==1:
        if nums[0]%k==0: return 1
        else: return 0
    s1=nums[:]
    for i in range(1,ll):
        s1[i]=s1[i-1]+nums[i]
    s2=nums[:]
    for i in range(ll-2,-1,-1):
        s2[i-1]=s2[i]+nums[i-1]
    n=0
    for i in range(ll):
        if s1[i]%k==0: n=n+1
    for i in range(ll):
        if s2[i]%k==0: n=n+1

    for i in range(1, ll - 2):
        if (s1[i] - s2[i]) % k == 0:
            n=n+1

    return n


# s=[4,5,0,-2,-3,1]
# print(s.count(5), -5%5)

# Runtime 216 ms Beats 81.30% of users with Python
# Memory 14.58 MB Beats 100.00% of users with Python
def subarraysDivByK10(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    seen = {0: 0}
    prefix_sum = 0
    for i in range(len(nums)):
        prefix_sum += nums[i]
        if prefix_sum % k not in seen:
            seen[prefix_sum % k] = 0
        else:
            seen[prefix_sum % k] += 1

    return sum([n * (n + 1) // 2 for n in seen.values()])

# Runtime 229 ms Beats 33.33% of users with Python
# Memory 14.87 MB Beats 82.93% of users with Python
def subarraysDivByK11(nums, k):
    dp = {0: 1}
    total, ans = 0, 0
    for n in nums:
        total += n
        remain = total % k
        if remain in dp:
            ans += dp[remain]
            dp[remain] += 1
        else:
            dp[remain] = 1
    return ans
