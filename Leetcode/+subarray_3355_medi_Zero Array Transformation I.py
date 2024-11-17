"""
17.11.2024
3355. Zero Array Transformation I
https://leetcode.com/problems/zero-array-transformation-i

You are given an integer array nums of length n and a 2D array queries,
where queries[i] = [li, ri].

For each queries[i]:
Select a subset of indices within the range [li, ri] in nums.
Decrement the values at the selected indices by 1.
A Zero Array is an array where all elements are equal to 0.
Return true if it is possible to transform nums into a Zero Array
after processing all the queries sequentially, otherwise return false.
A subset of an array is a selection of elements (possibly none) of the array.

Example 1:
Input: nums = [1,0,1], queries = [[0,2]]
Output: true
Explanation:
For i = 0:
Select the subset of indices as [0, 2] and decrement the values at these indices by 1.
The array will become [0, 0, 0], which is a Zero Array.

Example 2:
Input: nums = [4,3,2,1], queries = [[1,3],[0,2]]
Output: false
Explanation:
For i = 0:
Select the subset of indices as [1, 2, 3] and decrement the values at these indices by 1.
The array will become [4, 2, 1, 0].
For i = 1:
Select the subset of indices as [0, 1, 2] and decrement the values at these indices by 1.
The array will become [3, 1, 0, 0], which is not a Zero Array.

Constraints:
1 <= nums.length <= 105
0 <= nums[i] <= 105
1 <= queries.length <= 105
queries[i].length == 2
0 <= li <= ri < nums.length

Hint 1
Can we use difference array and prefix sum to check if an index can be made zero?
"""
# Time Limit Exceeded- 661 / 667 testcases passed
def isZeroArray2(nums, queries):
    """
    :type nums: List[int]
    :type queries: List[List[int]]
    :rtype: bool
    """
    for q in queries:
        for i in range(q[0],q[1]+1):
            if nums[i]!=0:
                nums[i]=nums[i]-1
    return all(i==0 for i in nums)

# Time Limit Exceeded- 661 / 667 testcases passed
def isZeroArray3(nums, queries):
    """
    :type nums: List[int]
    :type queries: List[List[int]]
    :rtype: bool
    """
    for q in queries:
        for i in range(q[0],q[1]+1):
            nums[i]=nums[i]-1
    # print(nums)
    return all(i<=0 for i in nums)

# Runtime 105 ms Beats 100.00%
# Memory 47.48 MB Beats 100.00%
# https://leetcode.com/problems/zero-array-transformation-i/solutions/6053353/rust-python-mark-start-and-end-of-the-query/
def isZeroArray(nums, queries):
    ll=len(nums)
    ind=[0]*(ll+1)
    for lft,rgt in queries:
        ind[lft]+=1
        ind[rgt+1]-=1
    summ=[0] * ll
    summc=0
    for i in range(ll):
        summc += ind[i]
        summ[i] = summc

    for i in range(ll):
        if nums[i] > summ[i]:
              return False
    return True



print(isZeroArray(nums = [1,0,1], queries = [[0,2]]))
# print(isZeroArray(nums = [4,3,2,1], queries = [[1,3],[0,2]]))


