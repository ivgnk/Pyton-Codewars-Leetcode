"""
Done 15.06.2025. Topics: Array, Greedy, Sorting, Counting
945. Minimum Increment to Make Array Unique
https://leetcode.com/problems/minimum-increment-to-make-array-unique/description

You are given an integer array nums. In one move, you can pick an
index i where 0 <= i < nums.length and increment nums[i] by 1.
Return the minimum number of moves to make every value in nums unique.
The test cases are generated so that the answer fits in a 32-bit integer.

Example 1:
Input: nums = [1,2,2]
Output: 1
Explanation: After 1 move, the array could be [1, 2, 3].

Example 2:
Input: nums = [3,2,1,2,1,7]
Output: 6
Explanation: After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
It can be shown with 5 or less moves that it is impossible for the array to have all unique values.
"""

# Runtime 1045 ms Beats 6.90%
# Memory 35.93 MB Beats 6.90%
def minIncrementForUnique2(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # https://www.geeksforgeeks.org/python-returning-index-of-a-sorted-list/

    ll=len(nums)
    n1=sorted([[nums[i],i] for i in range(ll)])
    # print(n1)
    n=0
    for i in range(1,ll):
        if n1[i][0]==n1[i-1][0]:
            n=n+1
            n1[i][0]=n1[i][0]+1
        elif n1[i][0]<n1[i-1][0]:
                add=n1[i-1][0]-n1[i][0]+1
                n=n+add
                n1[i][0]=n1[i][0]+add
    # print(n)
    # nums = sorted(n1, key=lambda x: x[1])
    # print(nums)
    return n

# Runtime 664 ms Beats 68.97%
# Memory 23.38 MB Beats 20.69%
# Runtime 653 ms Beats 86.21%
# Memory 23.58 MB Beats 20.69%

def minIncrementForUnique(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # https://www.geeksforgeeks.org/python-returning-index-of-a-sorted-list/

    ll=len(nums)
    n1=sorted(nums)
    n=0
    for i in range(1,ll):
        if n1[i]==n1[i-1]:
            n=n+1
            n1[i]=n1[i]+1
        elif n1[i]<n1[i-1]:
                add=n1[i-1]-n1[i]+1
                n=n+add
                n1[i]=n1[i]+add
    return n


# print(minIncrementForUnique([1,2,2]))
print(minIncrementForUnique([3,2,1,2,1,7]))



