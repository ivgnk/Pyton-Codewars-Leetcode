"""
15.11.2024. Topics: Two Pointers, Binary Search, Stack
1574. Shortest Subarray to be Removed to Make Array Sorted
https://leetcode.com/problems/shortest-subarray-to-be-removed-to-make-array-sorted

Given an integer array arr, remove a subarray (can be empty) from arr such that
the remaining elements in arr are non-decreasing.
Return the length of the shortest subarray to remove.
A subarray is a contiguous subsequence of the array.

Example 1:
Input: arr = [1,2,3,10,4,2,3,5]
Output: 3
Explanation: The shortest subarray we can remove is [10,4,2] of length 3.
The remaining elements after that will be [1,2,3,3,5] which are sorted.
Another correct solution is to remove the subarray [3,10,4].

Example 2:
Input: arr = [5,4,3,2,1]
Output: 4
Explanation: Since the array is strictly decreasing, we can only keep a single element. Therefore we need to remove a subarray of length 4, either [5,4,3,2] or [4,3,2,1].

Example 3:
Input: arr = [1,2,3]
Output: 0
Explanation: The array is already non-decreasing. We do not need to remove any elements.

Constraints:
1 <= arr.length <= 105
0 <= arr[i] <= 109

Hint 1
The key is to find the longest non-decreasing subarray starting with the first element or
ending with the last element, respectively.
Hint 2
After removing some subarray, the result is the concatenation of a sorted prefix and a sorted suffix,
where the last element of the prefix is smaller than the first element of the suffix.
"""

from typing import List

class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        r = len(arr) - 1
        while r > 0 and arr[r] >= arr[r - 1]: r -= 1
        res, l = r, 0
        while l < r and (l == 0 or arr[l - 1] <= arr[l]):
            while r < len(arr) and arr[l] > arr[r]: r += 1
            res = min(res, r - l - 1)
            l += 1
        return res

# https://leetcode.com/problems/shortest-subarray-to-be-removed-to-make-array-sorted/solutions/6046568/beats-100-users-in-time-complexity-constant-space-complexity-easy-to-understand/
class Solution3:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        right=len(arr)-1
        while right>0 and arr[right]>=arr[right-1]:
            right-=1
        left=0
        ans=right
        while left<right and (left==0 or arr[left-1]<=arr[left]):
            while right<len(arr) and arr[left]>arr[right]:
                right+=1
            ans=min(ans,right-left-1)
            left+=1
        return ans

# https://leetcode.com/problems/shortest-subarray-to-be-removed-to-make-array-sorted/solutions/6046585/easy-simple-approach-shortest-subarray-to-be-removed-to-make-array-sorted-beats-100/
class Solution2:
    def findLengthOfShortestSubarray(self, arr):
        n = len(arr)
        left, right = 0, n - 1

        # Find longest non-decreasing suffix
        while right > 0 and arr[right - 1] <= arr[right]:
            right -= 1

        # If the entire array is already sorted
        if right == 0:
            return 0

        ans = right

        # Find the minimum length of subarray to remove
        while left < right and (left == 0 or arr[left - 1] <= arr[left]):
            while right < n and arr[left] > arr[right]:
                right += 1
            ans = min(ans, right - left - 1)
            left += 1

        return ans