"""
Done 19.02.2025. Topics: Array
3452. Sum of Good Numbers
https://leetcode.com/problems/sum-of-good-numbers

Given an array of integers nums and an integer k, an element nums[i]
is considered good if it is strictly greater than the elements at indices i - k and i + k (if those indices exist).
If neither of these indices exists, nums[i] is still considered good.
Return the sum of all the good elements in the array.

Example 1:
Input: nums = [1,3,2,1,5,4], k = 2
Output: 12
Explanation:
The good numbers are nums[1] = 3, nums[4] = 5, and nums[5] = 4
because they are strictly greater than the numbers at indices i - k and i + k.

Example 2:
Input: nums = [2,1], k = 1
Output: 2
Explanation:
The only good number is nums[0] = 2 because it is strictly greater than nums[1].

Constraints:
2 <= nums.length <= 100
1 <= nums[i] <= 1000
1 <= k <= floor(nums.length / 2)

Topics: Array
Hint 1
For each index, check if nums[i] is strictly greater than nums[i - k] and nums[i + k].

My solution
Fast (2 ms) and easy Python solution for Problem 3452
https://leetcode.com/problems/sum-of-good-numbers/solutions/6439294/fast-2-ms-and-easy-python-solution-for-p-snbc/
Intuition
Use Hint 1:
For each index, check if nums[i] is strictly greater than nums[i - k] and nums[i + k].
"""

# Runtime 15 ms Beats 5.32%
# Memory 12.34 MB Beats 89.73%
def sumOfGoodNumbers2(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    ll=len(nums); ssum=0
    rr=range(ll)
    for i in rr:
        n1=i-k
        n2=i+k
        tr=True
        if n1 in rr: tr = tr and (nums[i] > nums[n1])
        if n2 in rr: tr = tr and (nums[i] > nums[n2])
        if tr: ssum+=nums[i]
    return ssum

# Runtime 2 ms Beats 68.78%
# Memory 12.22 MB Beats 99.88%
# Time Complexity O(N)
# Space Complexity O(1)
def sumOfGoodNumbers(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    ll=len(nums); ssum=0
    for i in range(ll):
        lft=i-k
        rgt=i+k
        tr=True
        if lft>-1: tr = tr and (nums[i] > nums[lft])
        if rgt<ll: tr = tr and (nums[i] > nums[rgt])
        if tr: ssum+=nums[i]
    return ssum


print(sumOfGoodNumbers(nums = [1,3,2,1,5,4], k = 2))
print(sumOfGoodNumbers(nums = [2,1], k = 1))
