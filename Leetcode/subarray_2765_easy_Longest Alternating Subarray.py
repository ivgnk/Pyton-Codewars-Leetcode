"""
Done 16.06.2024. Topics: Array, Enumeration
2765. Longest Alternating Subarray
https://leetcode.com/problems/longest-alternating-subarray/description/

You are given a 0-indexed integer array nums. A subarray s of length m is called alternating if:
m is greater than 1.
s1 = s0 + 1.
The 0-indexed subarray s looks like [s0, s1, s0, s1,...,s(m-1) % 2]. In other words,
s1 - s0 = 1, s2 - s1 = -1, s3 - s2 = 1, s4 - s3 = -1, and so on up to s[m - 1] - s[m - 2] = (-1)m.
Return the maximum length of all alternating subarrays present in nums or -1 if no such subarray exists.
A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
Input: nums = [2,3,4,3,4]
Output: 4
Explanation: The alternating subarrays are [3,4], [3,4,3], and [3,4,3,4]. The longest of these is [3,4,3,4], which is of length 4.

Example 2:
Input: nums = [4,5,6]
Output: 2
Explanation: [4,5] and [5,6] are the only two alternating subarrays. They are both of length 2.

Hint 1
As the constraints are low, you can check each subarray for the given condition.
"""

# Runtime 45 ms Beats 96.55%
# Memory 11.53 MB Beats 68.97%
# https://leetcode.com/problems/longest-alternating-subarray/submissions/1290181311/
def alternatingSubarray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ll=len(nums)
    maxlen=1; mm=0
    first=0
    for i in range(1,ll):
        nn=(-1)**first
        if nums[i] - nums[i - 1] == nn:
            maxlen=maxlen+1
            first=first+1
            mm=max(mm,maxlen)
        else:
            first=0
            maxlen=1
            nn = (-1) ** first
            if nums[i] - nums[i - 1] == nn:
                maxlen = maxlen + 1
                first = first + 1
                mm = max(mm, maxlen)

        # print(i, nums[i - 1], nums[i], nn, nums[i] - nums[i - 1] == nn , maxlen, mm)
    if mm==0: return -1
    return mm

# print(alternatingSubarray([2,3,4,3,4]))

print(alternatingSubarray([31,32,31,32,33])) # 4
