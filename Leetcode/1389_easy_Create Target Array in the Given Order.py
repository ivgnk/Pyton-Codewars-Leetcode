"""
 Done 29.09.2024. Topics: Simulation
1389. Create Target Array in the Given Order
https://leetcode.com/problems/create-target-array-in-the-given-order/description/

Given two arrays of integers nums and index. Your task is to create target array under the following rules:
Initially target array is empty.

From left to right read nums[i] and index[i],
insert at index index[i] the value nums[i] in target array.

Repeat the previous step until there are no elements to read in nums and index.

Return the target array.
It is guaranteed that the insertion operations will be valid.

Example 1:
Input: nums = [0,1,2,3,4], index = [0,1,2,2,1]
Output: [0,4,1,3,2]
Explanation:
nums       index     target
0            0        [0]
1            1        [0,1]
2            2        [0,1,2]
3            2        [0,1,3,2]
4            1        [0,4,1,3,2]

Example 2:
Input: nums = [1,2,3,4,0], index = [0,1,2,3,0]
Output: [0,1,2,3,4]
Explanation:
nums       index     target
1            0        [1]
2            1        [1,2]
3            2        [1,2,3]
4            3        [1,2,3,4]
0            0        [0,1,2,3,4]

Example 3:
Input: nums = [1], index = [0]
Output: [1]

Constraints:
1 <= nums.length, index.length <= 100
nums.length == index.length
0 <= nums[i] <= 100
0 <= index[i] <= i

Hint 1
Simulate the process and fill corresponding numbers in the designated spots.
"""

# Runtime 4 ms Beats 99.70%
# Memory 11.81 MB Beats 8.61%
def createTargetArray(nums, index):
    """
    :type nums: List[int]
    :type index: List[int]
    :rtype: List[int]
    """
    # return [nums[i] for i in index]
    res = []
    for i in range(len(index)):
        res.insert(index[i], nums[i])
    return res

print(createTargetArray( nums = [0,1,2,3,4], index = [0,1,2,2,1]))

