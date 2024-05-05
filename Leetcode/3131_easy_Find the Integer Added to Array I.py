"""
Done 05.05.2024
3131. Find the Integer Added to Array I

You are given two arrays of equal length, nums1 and nums2.
Each element in nums1 has been increased (or decreased in the case of negative) by an integer,
represented by the variable x.
As a result, nums1 becomes equal to nums2.
Two arrays are considered equal when they contain the same integers with the same frequencies.
Return the integer x.


Example 1:
Input: nums1 = [2,6,4], nums2 = [9,7,5]
Output: 3
Explanation:
The integer added to each element of nums1 is 3.

Example 2:
Input: nums1 = [10], nums2 = [5]
Output: -5
Explanation:
The integer added to each element of nums1 is -5.

Example 3:
Input: nums1 = [1,1,1,1], nums2 = [1,1,1,1]
Output: 0
Explanation:
The integer added to each element of nums1 is 0
"""

# Runtime 32 ms Beats 35.85% of users with Python
# Memory 11.56 MB Beats 77.80% of users with Python
# Runtime 25 ms Beats 83.06% of users with Python
# Memory 11.62 MB Beats 45.72% of users with Python

def addedInteger(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: int
    """
    return sorted(nums2)[0]-sorted(nums1)[0]