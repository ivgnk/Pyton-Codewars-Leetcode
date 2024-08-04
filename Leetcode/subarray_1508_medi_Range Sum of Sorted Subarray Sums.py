"""
Done 04.08.2024. Array, Sorting
1508. Range Sum of Sorted Subarray Sums
https://leetcode.com/problems/range-sum-of-sorted-subarray-sums/description

You are given the array nums consisting of n positive integers.
You computed the sum of all non-empty continuous subarrays from the array and
then sorted them in non-decreasing order, creating a new array of n * (n + 1) / 2 numbers.

Return the sum of the numbers from index left to index right (indexed from 1),
inclusive, in the new array. Since the answer can be a huge number return it modulo 109 + 7.

Example 1:
Input: nums = [1,2,3,4], n = 4, left = 1, right = 5
Output: 13
Explanation: All subarray sums are 1, 3, 6, 10, 2, 5, 9, 3, 7, 4. After sorting them in non-decreasing order we have the new array [1, 2, 3, 3, 4, 5, 6, 7, 9, 10]. The sum of the numbers from index le = 1 to ri = 5 is 1 + 2 + 3 + 3 + 4 = 13.

Example 2:
Input: nums = [1,2,3,4], n = 4, left = 3, right = 4
Output: 6
Explanation: The given array is the same as example 1. We have the new array [1, 2, 3, 3, 4, 5, 6, 7, 9, 10]. The sum of the numbers from index le = 3 to ri = 4 is 3 + 3 = 6.

Example 3:
Input: nums = [1,2,3,4], n = 4, left = 1, right = 10
Output: 50

Constraints:
n == nums.length
1 <= nums.length <= 1000
1 <= nums[i] <= 100
1 <= left <= right <= n * (n + 1) / 2

Hint 1
Compute all sums and save it in array.
Hint 2
Then just go from LEFT to RIGHT index and calculate answer modulo 1e9 + 7.
"""

# Runtime 347 ms Beats 35.71%
# Memory 42.79 MB Beats 42.86%

# Runtime 290 ms Beats 75.00%
# Time complexity: O(N**2*LogN+(Right−Left))
# Memory 43.01 MB Beats 28.57%
# Space complexity: O(N**2)

modu = 10 ** 9 + 7
def rangeSum(nums, n, left, right):
    res=[]
    for i in range(n):
        s1=nums[i]
        res.append(s1)
        for j in range(i + 1, n):
            s1=s1+nums[j]
            res.append(s1)
    res.sort()
    # special sum in order to pass last test
    ssum = 0
    for i in range(left - 1, right):
        ssum = (ssum + res[i]) % modu
    return ssum

print(rangeSum(nums = [1,2,3,4], n = 4, left = 1, right = 5))


# Runtime 2476 ms Beats 7.14%
# Memory 48.42 MB Beats 7.14%
def rangeSum3(nums, n, left, right):
    """
    :type nums: List[int]
    :type n: int
    :type left: int
    :type right: int
    :rtype: int
    """
    n1=n+1
    res = sorted([sum(nums[i:j])
                  for i in range(n1)
                      for j in range(i + 1, n1)])
    # special sum in order to pass last test
    ssum = 0
    for i in range(left - 1, right):
        ssum = (ssum + res[i]) % modu
    return ssum

# Wrong Answer - 53 / 54 testcases passed
def rangeSum2(nums, n, left, right):
    """
    :type nums: List[int]
    :type n: int
    :type left: int
    :type right: int
    :rtype: int
    """
    n1=n+1
    res=sorted([sum(nums[i:j])
                for i in range(n1)
                    for j in range(i+1,n1)])
    return sum(res[left-1:right])







