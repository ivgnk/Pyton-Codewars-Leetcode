"""
2164. Sort Even and Odd Indices Independently
https://leetcode.com/problems/sort-even-and-odd-indices-independently/description/

You are given a 0-indexed integer array nums. Rearrange the values of nums according to the following rules:
Sort the values at odd indices of nums in non-increasing order.
For example, if nums = [4,1,2,3] before this step, it becomes [4,3,2,1] after.
The values at odd indices 1 and 3 are sorted in non-increasing order.
Sort the values at even indices of nums in non-decreasing order.
For example, if nums = [4,1,2,3] before this step, it becomes [2,1,4,3] after.
The values at even indices 0 and 2 are sorted in non-decreasing order.
Return the array formed after rearranging the values of nums.

Example 1:
Input: nums = [4,1,2,3]
Output: [2,3,4,1]
Explanation:
First, we sort the values present at odd indices (1 and 3) in non-increasing order.
So, nums changes from [4,1,2,3] to [4,3,2,1].
Next, we sort the values present at even indices (0 and 2) in non-decreasing order.
So, nums changes from [4,1,2,3] to [2,3,4,1].
Thus, the array formed after rearranging the values is [2,3,4,1].

Example 2:
Input: nums = [2,1]
Output: [2,1]
Explanation:
Since there is exactly one odd index and one even index, no rearrangement of values takes place.
The resultant array formed is [2,1], which is the same as the initial array.
"""

# Runtime 36 ms Beats 35.44% of users with Python
# Memory 11.76 MB Beats 16.46% of users with Python

def sortEvenOdd2(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    ll=len(nums)
    odd_=[nums[i] for i in range(ll) if i%2 != 0]
    eve_=[nums[i] for i in range(ll) if i%2 == 0]
    odd_=sorted(odd_,reverse=True)
    eve_=sorted(eve_)
    ne=0; no=0
    for i in range(ll):
        if i % 2 == 0:
            nums[i]=eve_[ne]
            ne+=1
        else:
            nums[i]=odd_[no]
            no+=1
    return nums

# Runtime 27 ms Beats 88.61% of users with Python
# Memory 11.81 MB Beats 16.46% of users with Python

def sortEvenOdd(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    ll=len(nums)
    odd_=[nums[i] for i in range(ll) if i%2 != 0]
    eve_=[nums[i] for i in range(ll) if i%2 == 0]
    odd_=sorted(odd_,reverse=True)
    eve_=sorted(eve_)
    return[eve_[i//2] if i % 2 == 0 else odd_[i//2] for i in range(ll)]

print(sortEvenOdd([4,1,2,3]))
# print(sortEvenOdd([2,1]))