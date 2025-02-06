"""
06.02.2025. Topics: Hash Table, Counting
1726. Tuple with Same Product

Given an array nums of distinct positive integers,
return the number of tuples (a, b, c, d)
such that a * b = c * d where a, b, c,
and d are elements of nums, and a != b != c != d.

Example 1:
Input: nums = [2,3,4,6]
Output: 8
Explanation: There are 8 valid tuples:
(2,6,3,4) , (2,6,4,3) , (6,2,3,4) , (6,2,4,3)
(3,4,2,6) , (4,3,2,6) , (3,4,6,2) , (4,3,6,2)

Example 2:
Input: nums = [1,2,4,5,10]
Output: 16
Explanation: There are 16 valid tuples:
(1,10,2,5) , (1,10,5,2) , (10,1,2,5) , (10,1,5,2)
(2,5,1,10) , (2,5,10,1) , (5,2,1,10) , (5,2,10,1)
(2,10,4,5) , (2,10,5,4) , (10,2,4,5) , (10,2,5,4)
(4,5,2,10) , (4,5,10,2) , (5,4,2,10) , (5,4,10,2)

Constraints:
1 <= nums.length <= 1000
1 <= nums[i] <= 104
All elements in nums are distinct.

Hint 1
Note that all of the integers are distinct. This means that each time a product is formed it must be formed by two unique integers.
Hint 2
Count the frequency of each product of 2 distinct numbers. Then calculate the permutations formed.
"""
from collections import defaultdict

# as https://leetcode.com/problems/tuple-with-same-product/solutions/6382378/how-to-count-building-the-formula-explai-ftps/
# Runtime 683 ms Beats 22.22%
# Memory 63.42 MB Beats 22.22%

def tupleSameProduct(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ll=len(nums)
    dd=defaultdict(int)
    for i in range(ll):
        for j in range(i+1,ll):
            dd[nums[i]*nums[j]]+=1
    n = sum(4*v*(v-1) for k,v in dd.items())
    return n

print(tupleSameProduct([2,3,4,6]))
print(tupleSameProduct([1,2,4,5,10]))

