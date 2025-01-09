"""
09.01.2025. Topics: Sliding Window, Number Theory
3411. Maximum Subarray With Equal Products
https://leetcode.com/problems/maximum-subarray-with-equal-products/description/

You are given an array of positive integers nums.

An array arr is called product equivalent if prod(arr) == lcm(arr) * gcd(arr), where:

prod(arr) is the product of all elements of arr.
gcd(arr) is the GCD of all elements of arr.
lcm(arr) is the LCM of all elements of arr.
Return the length of the longest product equivalent subarray of nums.

Example 1:
Input: nums = [1,2,1,2,1,1,1]
Output: 5
Explanation:
The longest product equivalent subarray is [1, 2, 1, 1, 1], where prod([1, 2, 1, 1, 1]) = 2, gcd([1, 2, 1, 1, 1]) = 1, and lcm([1, 2, 1, 1, 1]) = 2.

Example 2:
Input: nums = [2,3,4,5,6]
Output: 3
Explanation:
The longest product equivalent subarray is [3, 4, 5].

Example 3:
Input: nums = [1,2,3,1,4,5,1]
Output: 5

Constraints:
2 <= nums.length <= 100
1 <= nums[i] <= 10

Hint 1
What is the maximum possible lcm?

a small trick. If the prod is already >= 2520 * gcd *lcm, then you could skip the further.
Because gcd would be always become smaller and smaller, and lcm between all numbers <=10
would be never bigger than 2520.
https://leetcode.com/problems/maximum-subarray-with-equal-products/description/comments/2790054

if product is greater then 10! then it can't be the longest subarray just break the loop.
If i was able to catch this observation during the contest then i was able to solve it without any errors!
https://leetcode.com/problems/maximum-subarray-with-equal-products/description/comments/2790399

Use two pointers to explore all subarrays.
For each subarray, compute the product, GCD, and LCM dynamically.
Check if product == gcd * lcm for each subarray.
Track and update the length of the longest valid subarray.
Use helper functions to calculate GCD and LCM efficiently.
https://leetcode.com/problems/maximum-subarray-with-equal-products/description/comments/2790643

Re-writeup of question :
Find the Maximum possible length of a subarray for which
product of subarray's elements == lcm of that subarray * gcd of that subarray
https://leetcode.com/problems/maximum-subarray-with-equal-products/description/comments/2791276

"""

from typing import List
import math

# https://leetcode.com/problems/maximum-subarray-with-equal-products/solutions/6255825/
# Runtime 39 ms Beats 71.04%
# Memory 17.73 MB Beats 81.14%
class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        max_len = 0

        # Iterate through all possible subarrays
        for start in range(n):
            prod = 1
            gcd_val = nums[start]
            lcm_val = nums[start]

            for end in range(start, n):
                prod *= nums[end]
                gcd_val = math.gcd(gcd_val, nums[end])
                lcm_val = (lcm_val * nums[end]) // math.gcd(lcm_val, nums[end])

                # Check the product equivalent condition
                if prod == lcm_val * gcd_val:
                    max_len = max(max_len, end - start + 1)

        return max_len

# https://leetcode.com/problems/maximum-subarray-with-equal-products/solutions/6243801/
class Solution2:
    def maxLength(self, nums: List[int]) -> int:
        maxi = float('-inf')
        for i in range(len(nums)):
            for j in range(i+1 , len(nums)+1):
                win = nums[i:j]
                if math.prod(win) == math.gcd(*win) * math.lcm(*win):
                    if len(win) > maxi:
                        maxi = len(win)
        return maxi

