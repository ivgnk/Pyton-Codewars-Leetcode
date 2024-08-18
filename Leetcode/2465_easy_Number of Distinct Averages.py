"""
Done 18.08.2024. Topics: Array, Sorting
2465. Number of Distinct Averages

You are given a 0-indexed integer array nums of even length.
As long as nums is not empty, you must repetitively:
Find the minimum number in nums and remove it.
Find the maximum number in nums and remove it.
Calculate the average of the two removed numbers.
The average of two numbers a and b is (a + b) / 2.
For example, the average of 2 and 3 is (2 + 3) / 2 = 2.5.
Return the number of distinct averages calculated using the above process.
Note that when there is a tie for a minimum or maximum number, any can be removed.

Example 1:
Input: nums = [4,1,4,0,3,5]
Output: 2
Explanation:
1. Remove 0 and 5, and the average is (0 + 5) / 2 = 2.5. Now, nums = [4,1,4,3].
2. Remove 1 and 4. The average is (1 + 4) / 2 = 2.5, and nums = [4,3].
3. Remove 3 and 4, and the average is (3 + 4) / 2 = 3.5.
Since there are 2 distinct numbers among 2.5, 2.5, and 3.5, we return 2.

Example 2:
Input: nums = [1,100]
Output: 1
Explanation:
There is only one average to be calculated after removing 1 and 100, so we return 1.

Constraints:
2 <= nums.length <= 100
nums.length is even.
0 <= nums[i] <= 100

Hint 1
Try sorting the array.
Hint 2
Store the averages being calculated, and find the distinct ones

Solution
✏️ Easy Python solution with sorting, pop & set comprehension
Intuition
Sorting the array.
Store the averages being calculated in set.

Approach
1) Sort
2) Set comprehension
3) Pop for deleting elements
"""

# Runtime 36 ms Beats 52.23%
# Memory 16.60 MB Beats 13.36%
def distinctAverages2(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums = sorted(nums); res=set()
    for i in range(len(nums) // 2):
        a=nums.pop(0)
        b=nums.pop()
        res.add((a + b)/2)
    return len(res)

# Runtime 34 ms Beats 71.00%
# Memory 16.42 MB Beats 89.05%
def distinctAverages3(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums = sorted(nums); res=set()
    for i in range(len(nums) // 2):
        res.add((nums.pop(0) + nums.pop())/2)
    return len(res)

# Runtime 33 ms Beats 74.37%
# Memory 16.46 MB Beats 89.05%
# Runtime 28 ms Beats 93.26%
# Memory 16.60 MB Beats 57.40%
def distinctAverages(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums = sorted(nums)
    res={(nums.pop(0) + nums.pop())/2 for i in range(len(nums) // 2) }
    return len(res)


# print(distinctAverages([4,1,4,0,3,5]))
print(distinctAverages([9,5,7,8,7,9,8,2,0,7]))



