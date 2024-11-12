"""
12.11.2024. Topics: Array
3349. Adjacent Increasing Subarrays Detection I
https://leetcode.com/problems/adjacent-increasing-subarrays-detection-i

Given an array nums of n integers and an integer k, determine whether there exist two adjacent
subarrays of length k such that both subarrays are strictly increasing.
Specifically, check if there are two subarrays starting at indices a and b (a < b), where:

Both subarrays nums[a..a + k - 1] and nums[b..b + k - 1] are strictly increasing.
The subarrays must be adjacent, meaning b = a + k.
Return true if it is possible to find two such subarrays, and false otherwise.

Example 1:
Input: nums = [2,5,7,8,9,2,3,4,3,1], k = 3
Output: true
Explanation:
The subarray starting at index 2 is [7, 8, 9], which is strictly increasing.
The subarray starting at index 5 is [2, 3, 4], which is also strictly increasing.
These two subarrays are adjacent, so the result is true.

Example 2:
Input: nums = [1,2,3,4,4,4,4,5,6,7], k = 5
Output: false

Constraints:
2 <= nums.length <= 100
1 < 2 * k <= nums.length
-1000 <= nums[i] <= 1000
"""

# Wrong Answer - 926 / 1422 testcases passed
def hasIncreasingSubarrays2(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    ll=len(nums)
    if ll==2: return True
    elif ll==3:
        if nums[0]<nums[1] or nums[1]<nums[2]: return True
    n1=[]; n2 = []; br=False
    for i in range(ll):
        if i==0:
            n1+=[nums[i]]
        else:
            if nums[i] > nums[i-1]:
                n1 += [nums[i]]
                n2 = []
                for j in range(k,ll):
                    if j==k:
                        n2 += [nums[j]]
                    else:
                        if nums[j]>nums[j-1]:
                            n2 += [nums[j]]
                        else:
                            br=True
                            break
        if br:
            print(i, n1,n2)
            if len(n1)>1 and len(n2)>1: return True
            br=False
            n1=[]
    if len(n1) >1 and len(n2) > 1: return True
    else: return False

def hasIncreasingSubarrays3(nums, k):
    ll=len(nums)
    if ll==2 or ll==3: return True
    n1=[]; n2 = []; br=False
    for i in range(ll):
        if i==0:
            n1+=[nums[i]]
            n2+=[nums[i+k]]
        else:
            if nums[i]<=nums[i-1]:
                br=True
                break
            else:
                n1 += [nums[i]]
                if nums[i + k]<= nums[i + k - 1]:
                    br = True
                    break
                else: n2 += [nums[i + k]]
                if nums[i+k]>nums[i+k-1]: n2 += [nums[i+k]]
        if br:
            n1=[nums[i]]
            n2=[nums[i]]
            if (len(n1)>1 and len(n2)>=1) or (len(n1)>=1 and len(n2)>1):
                return True
    if (len(n1)>1 and len(n2)>=1) or (len(n1)>=1 and len(n2)>1):
        return True
    else: return False

# https://leetcode.com/problems/adjacent-increasing-subarrays-detection-i/submissions/1448750230/
# Runtime 108 ms Beats 5.02% Analyze Complexity
# Memory 16.64 MB Beats 54.71%
def hasIncreasingSubarrays4(nums, k):
    def increase(sub):
        return sub == sorted(list(set(sub)))

    ll=len(nums)
    if ll==2 or ll==3: return True

    for i in range(ll-2*k+1):
        if increase(nums[i:i+k]) and increase(nums[i+k:i+2*k]):
            return True
    return False

# Runtime 92 ms Beats 12.55%
# Memory 16.58 MB Beats 96.01%
def hasIncreasingSubarrays5(nums, k):
    def increase(sub):
        return sub == sorted(list(set(sub)))
    for i in range(len(nums)-2*k+1):
        ik=i+k
        if increase(nums[i:ik]) and increase(nums[ik:ik+k]):
            return True
    return False

# Runtime 77 ms Beats 76.19%
# Memory 16.85 MB Beats 19.82%
def hasIncreasingSubarrays(nums, k):
    n = len(nums)
    def is_strictly_increasing(start):
        for i in range(start, start + k - 1):
            if nums[i] >= nums[i + 1]:
                return False
        return True
    for i in range(n - 2 * k + 1):
        if is_strictly_increasing(i) and is_strictly_increasing(i + k):
            return True
    return False




# print(hasIncreasingSubarrays(nums = [2,5,7,8,9,2,3,4,3,1], k = 3))
# print(hasIncreasingSubarrays(nums = [1,2,3,4,4,4,4,5,6,7], k = 5))
# print(hasIncreasingSubarrays(nums = [-5,19,-2], k = 1))
# print(hasIncreasingSubarrays(nums = [-15,19], k = 1))
# print(hasIncreasingSubarrays(nums = [-5,16,14,-19], k = 1))
print(hasIncreasingSubarrays(nums = [1,2,3,4,4,4,4,5,6,7], k = 5))


