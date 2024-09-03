"""
Done 03.09.2024. Topics: Array, Hash Table
2748. Number of Beautiful Pairs
https://leetcode.com/problems/number-of-beautiful-pairs/description/

You are given a 0-indexed integer array nums.
A pair of indices i, j where 0 <= i < j < nums.length is called beautiful if the first
digit of nums[i] and the last digit of nums[j] are coprime.

Return the total number of beautiful pairs in nums.
Two integers x and y are coprime if there is no integer greater than 1 that divides both of them.
In other words, x and y are coprime if gcd(x, y) == 1, where gcd(x, y) is the greatest common divisor of x and y.

Example 1:
Input: nums = [2,5,1,4]
Output: 5
Explanation: There are 5 beautiful pairs in nums:
When i = 0 and j = 1: the first digit of nums[0] is 2, and the last digit of nums[1] is 5. We can confirm that 2 and 5 are coprime, since gcd(2,5) == 1.
When i = 0 and j = 2: the first digit of nums[0] is 2, and the last digit of nums[2] is 1. Indeed, gcd(2,1) == 1.
When i = 1 and j = 2: the first digit of nums[1] is 5, and the last digit of nums[2] is 1. Indeed, gcd(5,1) == 1.
When i = 1 and j = 3: the first digit of nums[1] is 5, and the last digit of nums[3] is 4. Indeed, gcd(5,4) == 1.
When i = 2 and j = 3: the first digit of nums[2] is 1, and the last digit of nums[3] is 4. Indeed, gcd(1,4) == 1.
Thus, we return 5.

Example 2:
Input: nums = [11,21,12]
Output: 2
Explanation: There are 2 beautiful pairs:
When i = 0 and j = 1: the first digit of nums[0] is 1, and the last digit of nums[1] is 1. Indeed, gcd(1,1) == 1.
When i = 0 and j = 2: the first digit of nums[0] is 1, and the last digit of nums[2] is 2. Indeed, gcd(1,2) == 1.
Thus, we return 2.

Constraints:
2 <= nums.length <= 100
1 <= nums[i] <= 9999
nums[i] % 10 != 0

Solution
✏️ Not a completely simple Python solution with some tricks

# Intuition
Use the built-in gcd function of the math module.
Use preparing data & memoization

# Approach
The pairs of initial and final digits are only 100.
Let's save the gcd(nums[i], nums[j]) == 1 values in a two-dimensional array.
To speed up calculations, prepare arrays of the first and last digits.
To speed up calculations, use list comprehension.
"""
from math import gcd
data=[]

# Runtime 143 ms Beats 97.37%
# Memory 16.74 MB Beats 10.75%
def countBeautifulPairs2(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    global data
    if data==[]:
        data = [[0] * 10 for i in range(10)]
        for i in range(10):
            for j in range(10):
                data[i][j]=gcd(i,j)==1
    ll=len(nums)
    fd=[int(str(i)[0]) for i in nums]
    ld=[int(str(i)[-1]) for i in nums]
    n=[data[fd[i]][ld[j]]
        for i in range(ll)
            for j in range(i+1,ll)]
    return sum(n)


# Runtime 140 ms Beats 97.59%
# Memory 16.54 MB Beats 70.61%
def countBeautifulPairs(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    global data
    if data==[]:
        data = [[0] * 10 for i in range(10)]
        for i in range(10):
            for j in range(10):
                data[i][j]=gcd(i,j)==1
    ll=len(nums)
    fd=[int(str(i)[0]) for i in nums]
    ld=[int(str(i)[-1]) for i in nums]
    n=0
    for i in range(ll):
        for j in range(i+1,ll):
            n+=data[fd[i]][ld[j]]
    return n


print(countBeautifulPairs([2,5,1,4]))
print(countBeautifulPairs([11,21,12]))