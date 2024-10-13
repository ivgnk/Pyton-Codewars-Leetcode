"""
Done 13.10.2024. Topics: Array, Binary Search, Sorting
1608. Special Array With X Elements Greater Than or Equal X
https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x

You are given an array nums of non-negative integers.
nums is considered special if there exists a number x such that there are exactly x
numbers in nums that are greater than or equal to x.

Notice that x does not have to be an element in nums.
Return x if the array is special, otherwise, return -1.
It can be proven that if nums is special, the value for x is unique.

Example 1:
Input: nums = [3,5]
Output: 2
Explanation: There are 2 values (3 and 5) that are greater than or equal to 2.

Example 2:
Input: nums = [0,0]
Output: -1
Explanation: No numbers fit the criteria for x.
If x = 0, there should be 0 numbers >= x, but there are 2.
If x = 1, there should be 1 number >= x, but there are 0.
If x = 2, there should be 2 numbers >= x, but there are 0.
x cannot be greater since there are only 2 numbers in nums.

Example 3:
Input: nums = [0,4,3,0,4]
Output: 3
Explanation: There are 3 values that are greater than or equal to 3.

Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 1000

Hint 1
Count the number of elements greater than or equal to x for each x in the range [0, nums.length].
Hint 2
If for any x, the condition satisfies, return that x. Otherwise, there is no answer.


"""
# Wrong Answer - 7 / 98 testcases passed
# nums = [3,5]
# Output -1
# Expected 2
def specialArray2(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ll = len(nums)
    ns = sorted(nums)
    for i in range(ll+1):
        if i==ll:
            if i >= ns[i-1]: return i
        else:
            if i >= ns[i]: return i
    return -1

# Runtime 37 ms Beats 72.89%
# Memory 16.71 MB Beats 7.83%
# Runtime 33 ms Beats 90.07%
# Memory 16.62 MB Beats 7.83%
def specialArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # 1-case: all equal numbers in list with length==numbers
    ll = len(nums)
    ss=set(nums)
    if len(ss)==1 and ll==nums[0]: return nums[0]

    # 2-case x in range(min(nums),max(nums)+1)
    ns = sorted(nums)
    # print(ns)
    for i in range(1,ll):
        if i <= ns[-i] and i > ns[-i-1]:
            print('first')
            return i

    # 3 case x not in range(min(nums),max(nums)+1)
    sr=set(range(min(nums),max(nums)+1))
    for i in range(1,ll+1):
        if i==ll and not (i in sr) and i<=nums[0]:
            print('ll')
            return i
    print('last')
    return -1

# print(specialArray([0,0]))  #-1
# print(specialArray([0,4,3,0,4])) # 3
# print(specialArray([3,5]))
# print(specialArray([7,0,0,2,0]))
# print(specialArray([20,21,21,8,23,2,3,6,19,22,6,13,2,12,12,25,10])) # -1