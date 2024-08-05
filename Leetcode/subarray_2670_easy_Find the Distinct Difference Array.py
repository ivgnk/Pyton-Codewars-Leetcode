"""
Done 05.08.2024. Topics: Array, Set
2670. Find the Distinct Difference Array
https://leetcode.com/problems/find-the-distinct-difference-array/description/

You are given a 0-indexed array nums of length n.

The distinct difference array of nums is an array diff of length n such that diff[i]
is equal to the number of distinct elements in the suffix nums[i + 1, ..., n - 1]
subtracted from the number of distinct elements in the prefix nums[0, ..., i].

Return the distinct difference array of nums.
Note that nums[i, ..., j] denotes the subarray of nums starting at index i and ending at index j inclusive.
Particularly, if i > j then nums[i, ..., j] denotes an empty subarray.

Example 1:
Input: nums = [1,2,3,4,5]
Output: [-3,-1,1,3,5]
Explanation: For index i = 0, there is 1 element in the prefix and 4 distinct elements in the suffix.
Thus, diff[0] = 1 - 4 = -3.
For index i = 1, there are 2 distinct elements in the prefix and 3 distinct elements in the suffix.
Thus, diff[1] = 2 - 3 = -1.
For index i = 2, there are 3 distinct elements in the prefix and 2 distinct elements in the suffix.
Thus, diff[2] = 3 - 2 = 1.
For index i = 3, there are 4 distinct elements in the prefix and 1 distinct element in the suffix.
Thus, diff[3] = 4 - 1 = 3.
For index i = 4, there are 5 distinct elements in the prefix and no elements in the suffix.
Thus, diff[4] = 5 - 0 = 5.

Example 2:
Input: nums = [3,2,3,4,2]
Output: [-2,-1,0,2,3]
Explanation: For index i = 0, there is 1 element in the prefix and 3 distinct elements in the suffix.
Thus, diff[0] = 1 - 3 = -2.
For index i = 1, there are 2 distinct elements in the prefix and 3 distinct elements in the suffix.
Thus, diff[1] = 2 - 3 = -1.
For index i = 2, there are 2 distinct elements in the prefix and 2 distinct elements in the suffix.
Thus, diff[2] = 2 - 2 = 0.
For index i = 3, there are 3 distinct elements in the prefix and 1 distinct element in the suffix.
Thus, diff[3] = 3 - 1 = 2.
For index i = 4, there are 3 distinct elements in the prefix and no elements in the suffix.
Thus, diff[4] = 3 - 0 = 3.

Constraints:
1 <= n == nums.length <= 50
1 <= nums[i] <= 50

Hint 1
Which data structure will help you maintain distinct elements?
Hint 2
Iterate over all possible prefix sizes. Then, use a nested loop to add the elements of the prefix to a set,
and another nested loop to add the elements of the suffix to another set.
"""

def distinctDifferenceArray2(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    prf=set([nums[0]])
    pst=set(nums[1:])
    ll=len(nums); diff=[len(prf)-len(pst)]
    for i in range(1,ll):
        prf.add(nums[i])
        if nums[i] in pst:
            pst.remove(nums[i])
        diff.append(len(prf) - len(pst))
    return diff


# Runtime 72 ms Beats 81.55%
# Memory 11.70 MB Beats 31.07%
# Runtime 69 ms Beats 89.32%
# Memory 11.63 MB Beats 31.07%
def distinctDifferenceArray1(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    diff=[]
    for i in range(len(nums)):
        prf=set(nums[:i+1])
        pst=set(nums[i+1:])
        diff.append(len(prf) - len(pst))
    return diff

# Runtime 73 ms Beats 79.61%
# Memory 11.55 MB Beats 69.90%
def distinctDifferenceArray(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    return [len(set(nums[:i+1])) - len(set(nums[i+1:])) for i in range(len(nums)) ]



print(distinctDifferenceArray([1,2,3,4,5]))
print(distinctDifferenceArray([3,2,3,4,2]))
