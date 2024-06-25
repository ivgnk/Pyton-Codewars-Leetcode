"""
Done 25.06.2024. Topics: Array, Math

1588. Sum of All Odd Length Subarrays
https://leetcode.com/problems/sum-of-all-odd-length-subarrays/description/

Given an array of positive integers arr, return the sum of all possible odd-length subarrays of arr.
A subarray is a contiguous subsequence of the array.

Example 1:
Input: arr = [1,4,2,5,3]
Output: 58
Explanation: The odd-length subarrays of arr and their sums are:
[1] = 1
[4] = 4
[2] = 2
[5] = 5
[3] = 3
[1,4,2] = 7
[4,2,5] = 11
[2,5,3] = 10
[1,4,2,5,3] = 15
If we add all these together we get 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58

Example 2:
Input: arr = [1,2]
Output: 3
Explanation: There are only 2 subarrays of odd length, [1] and [2]. Their sum is 3.

Example 3:
Input: arr = [10,11,12]
Output: 66

Constraints:
1 <= arr.length <= 100
1 <= arr[i] <= 1000

Hint 1
You can brute force – try every (i,j) pair,
and if the length is odd, go through and add the sum to the answer.
"""

# Runtime 33 ms Beats 65.92%
# Memory 11.58 MB Beats 67.04%
# Runtime 30 ms Beats 71.54%
# Memory 11.78 MB Beats 15.36%
def sumOddLengthSubarrays(arr):
    """
    :type arr: List[int]
    :rtype: int
    """
    ll=len(arr)
    s1=sum(arr)
    if ll<3: return s1
    nn=[i for i in range(3,ll+1) if i%2!=0]
    for i in nn:
        # print(i)
        for j in range(ll):
            jj=i+j
            if jj<=ll:
                # print(j,arr[j:jj])
                s1=s1+sum(arr[j:jj])
    return s1

print(sumOddLengthSubarrays([1,4,2,5,3]))
print(sumOddLengthSubarrays([1,2]))
print(sumOddLengthSubarrays([10,11,12]))

