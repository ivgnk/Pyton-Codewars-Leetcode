"""
07.12.2024
3375. Minimum Operations to Make Array Values Equal to K
https://leetcode.com/problems/minimum-operations-to-make-array-values-equal-to-k/description/

You are given an integer array nums and an integer k.
An integer h is called valid if all values in the array
that are strictly greater than h are identical.

For example, if nums = [10, 8, 10, 8],
a valid integer is h = 9 because all nums[i] > 9
are equal to 10, but 5 is not a valid integer.

You are allowed to perform the following operation on nums:

Select an integer h that is valid for the current values in nums.
For each index i where nums[i] > h, set nums[i] to h.
Return the minimum number of operations required to make every element in nums equal to k.
If it is impossible to make all elements equal to k, return -1.

Example 1:
Input: nums = [5,2,5,4,5], k = 2
Output: 2
Explanation:
The operations can be performed in order using valid integers 4 and then 2.

Example 2:
Input: nums = [2,1,2], k = 2
Output: -1
Explanation:
It is impossible to make all the values equal to 2.

Example 3:
Input: nums = [9,7,5,3], k = 1
Output: 4
Explanation:
The operations can be performed using valid integers in the order 7, 5, 3, and 1.

Constraints:
1 <= nums.length <= 100
1 <= nums[i] <= 100
1 <= k <= 100

Hint 1
Handle the case when the array contains an integer less than k
Hint 2
Start by performing operations on the highest integer
Hint 3
You can perform an operation on the highest integer using the second-highest, an operation on the second-highest using the third-highest, and so forth.
Hint 4
The answer is the number of distinct integers in the array that are larger than k.


For anyone who is confused with the problem description:
We have an array and a number k, we have to make all elements equal to k ,
in each step we can select a number h such that all the numbers greater than h in array should be same for eg.
in array 5,2,5,4,5 we can select h as 4 because after that all the elements greater than h are 5 and no element is different ,
still confused here: if we select h as 2 or 3 we will get 4,5,5,5 as greater elements where 4 is different so we cant choose that ok now ,
after selecting 4 we convert all 5 to h which is 4 after that we can select 3 or 2 as h in next step
because all elements are 4 now this is how we will convert all the numbers to k and
if a number cant be converted to k so we return -1
else we return how many steps it took us to convert all elements to k ;
a number can only go lower it cant get bigger so only case where we return -1
is when we cant make a number equal to k ; ie it is lower
https://leetcode.com/problems/minimum-operations-to-make-array-values-equal-to-k/description/comments/2752047
"""

# Runtime 40 ms Beats 100.00%
# Memory 12.03 MB Beats 100.00%
# Time Complexity O(N)
# Space Complexity O(N)

def minOperations( nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
