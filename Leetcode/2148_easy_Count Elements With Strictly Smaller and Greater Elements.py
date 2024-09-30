"""
Done 01.10.2024. Topics: Array, Sorting, Counting
2148. Count Elements With Strictly Smaller and Greater Elements
https://leetcode.com/problems/count-elements-with-strictly-smaller-and-greater-elements/description/

Given an integer array nums, return the number of elements that have both a strictly smaller
and a strictly greater element appear in nums.

Example 1:
Input: nums = [11,7,2,15]
Output: 2
Explanation: The element 7 has the element 2 strictly smaller than it and the element 11 strictly greater than it.
Element 11 has element 7 strictly smaller than it and element 15 strictly greater than it.
In total there are 2 elements having both a strictly smaller and a strictly greater element appear in nums.

Example 2:
Input: nums = [-3,3,3,90]
Output: 2
Explanation: The element 3 has the element -3 strictly smaller than it and the element 90 strictly greater than it.
Since there are two elements with the value 3, in total there are 2 elements having both a strictly smaller and
a strictly greater element appear in nums.

Constraints:
1 <= nums.length <= 100
-10**5 <= nums[i] <= 10**5

Hint 1
All the elements in the array should be counted except for the minimum and maximum elements.
Hint 2
If the array has n elements, the answer will be n - count(min(nums)) - count(max(nums))
Hint 3
This formula will not work in case the array has all the elements equal, why?

My Solution
✏️ Easy Python solution base on hints and knowledge of the language
https://leetcode.com/problems/count-elements-with-strictly-smaller-and-greater-elements/solutions/5853671/easy-python-solution-base-on-hints-and-knowledge-of-the-language/
Intuition
Main - hint 2
Adding - hint 3 - a test of knowledge of language structures

# Approach
<!-- Describe your approach to solving the problem. -->
Use a set to count the unique elements of an array
"""

# Runtime 16 ms Beats 93.98%
# Memory 11.44 MB Beats 95.18%
def countElements(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ll=len(nums)
    if ll<=2: return 0
    lls=len(set(nums))
    if lls<=2: return 0
    mmax=max(nums)
    mmin=min(nums)
    return ll-nums.count(mmax)-nums.count(mmin)

print(countElements([11,7,2,15]))
print(countElements([-3,3,3,90]))


