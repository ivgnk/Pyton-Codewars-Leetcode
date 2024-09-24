"""
Done 24.09.2024. Topics: Sliding Window
1493. Longest Subarray of 1's After Deleting One Element
https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/

Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array.
Return 0 if there is no such subarray.

Example 1:
Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.

Example 2:
Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].

Example 3:
Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.

Constraints:
1 <= nums.length <= 10**5
nums[i] is either 0 or 1.

Hint 1
Maintain a sliding window where there is at most one zero in it.
"""

from icecream import ic

# Runtime 947 ms Beats 13.46%
# Memory 14.60 MB Beats 93.77%
def longestSubarray(nums):
    left = 0
    right = 0
    longest = 0
    deleted_loc = -1
    while right < len(nums):
        if nums[right] == 0:
            left = deleted_loc + 1
            deleted_loc = right
        longest = max(longest, right - left)
        right += 1
    return longest

# Time Limit Exceeded - 56 / 82 testcases passed
# len(nums) = 1728
def longestSubarray3(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ll=len(nums)
    mmax=-1
    for i in range(ll):
        for j in range(2,ll+1):
            s=nums[i:j]
            if s.count(0)<=1:
                mmax=max(mmax,len(s)-1)
    return mmax

# Time Limit Exceeded - 58 / 82 testcases passed
# len(nums) = 1019
def longestSubarray4(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ll=len(nums); nums=list(nums)
    mmax=-1
    for i in range(ll):
        s = [nums[i]]
        for j in range(i+1,ll):
            s+=[nums[j]]
            if s.count(0)<=1:
                mmax=max(mmax,len(s)-1)
            # ic(i,j,s,len(s),mmax)
    return mmax

# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/description/comments/1568562
# Runtime 1000 ms Beats 5.09%
# Memory 22.52 MB Beats 7.80%
def longestSubarray5(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ll=len(nums)
    numsl=[int(i) for i in nums]
    n0=nums.count(0)
    if n0==0: return ll-1
    lft=[0]*ll; rgt=[0]*ll
    for i in range(1,ll):
        if numsl[i-1]==1:
            lft[i]=lft[i-1]+1
    ic(lft)
    for i in range(ll-2,-1,-1):
        if numsl[i+1]==1:
            rgt[i]=rgt[i+1]+1
    ic(rgt)
    mmax=0
    for i in range(ll):
        mmax=max(mmax,lft[i]+rgt[i])
    return mmax

# similar https://leetcode.com/problems/max-consecutive-ones-iii/submissions/1346327915/

# Wrong Answer - 29 / 82 testcases passed
# nums = [1,1,0,0,1,1,1,0,1]
# Output 5
# Expected 4
def longestSubarray6(nums):
    ll=len(nums); ll1=ll-1
    n0=nums.count(0)
    if n0 == 0 or n0 == 1:  return ll1
    elif n0 == ll: return 0
    elif n0 == ll1:  return 1
    ############################
    i = 0
    j = 0
    zeroCnt = 0
    mmax = 0
    while j < ll:
        if nums[j] == 0:
            zeroCnt += 1
        if zeroCnt > 1:
            mmax = max(mmax, j - i - 1)
            while zeroCnt > 1:
                zeroCnt -= 1
                i += 1
        ic(i, j,mmax)
        j += 1
    return mmax-(nums[ll1]==0)

# ic(longestSubarray([1,1,0,1])) #3
# ic(longestSubarray([0,1,1,1,0,1,1,0,1])) #5
# ic(longestSubarray([1,1,1])) #2
ic(longestSubarray([1,0,0,1,0])) # 1

