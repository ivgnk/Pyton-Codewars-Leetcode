"""
Done 04.11.2024. Topics: Array, Hash Table, Sliding Window
3318. Find X-Sum of All K-Long Subarrays I
https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-i/description/

You are given an array nums of n integers and two integers k and x.
The x-sum of an array is calculated by the following procedure:

Count the occurrences of all elements in the array.
Keep only the occurrences of the top x most frequent elements.
If two elements have the same number of occurrences, the element with the bigger value is considered more frequent.
Calculate the sum of the resulting array.
Note that if an array has less than x distinct elements, its x-sum is the sum of the array.
Return an integer array answer of length n - k + 1 where answer[i] is the x-sum of the
subarray nums[i..i + k - 1].

Example 1:
Input: nums = [1,1,2,2,3,4,2,3], k = 6, x = 2
Output: [6,10,12]
Explanation:
For subarray [1, 1, 2, 2, 3, 4], only elements 1 and 2 will be kept in the resulting array. Hence, answer[0] = 1 + 1 + 2 + 2.
For subarray [1, 2, 2, 3, 4, 2], only elements 2 and 4 will be kept in the resulting array. Hence, answer[1] = 2 + 2 + 2 + 4. Note that 4 is kept in the array since it is bigger than 3 and 1 which occur the same number of times.
For subarray [2, 2, 3, 4, 2, 3], only elements 2 and 3 are kept in the resulting array. Hence, answer[2] = 2 + 2 + 2 + 3 + 3.

Example 2:
Input: nums = [3,8,7,8,7,5], k = 2, x = 2
Output: [11,15,15,15,12]
Explanation:
Since k == x, answer[i] is equal to the sum of the subarray nums[i..i + k - 1].

Constraints:
1 <= n == nums.length <= 50
1 <= nums[i] <= 50
1 <= x <= k <= nums.length

Hint 1
Implement the x-sum function. Then, run x-sum on every subarray of nums of size k.
"""

# Runtime 16 ms Beats 92.64%
# Memory 16.67 MB Beats 60.52%
# Time Complexity O((N−K)Klog(K)
# Space Complexity O(N)
from collections import Counter
def findXSum(nums, k, x):
    """
    :type nums: List[int]
    :type k: int
    :type x: int
    :rtype: List[int]
    """
    ll=len(nums); res=[]
    for i in range(ll-k+1):
        s1=nums[i:i+k]
        lst=sorted([(v,k) for k,v in Counter(s1).items()],reverse=True)
        if len(lst)<x: res.append(sum(s1))
        else: res.append(sum([lst[j][0]*lst[j][1] for j in range(x)]))
    return res

# print(findXSum(nums = [1,1,2,2,3,4,2,3], k = 6, x = 2))
# print(findXSum(nums = [3,8,7,8,7,5], k = 2, x = 2))
print(findXSum(nums = [9,2,2], k = 3, x = 3))

