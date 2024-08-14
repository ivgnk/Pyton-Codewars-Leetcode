"""
Done 14.08.2024. Topics: Array
2540. Minimum Common Value
https://leetcode.com/problems/minimum-common-value/description/

Given two integer arrays nums1 and nums2, sorted in non-decreasing order,
return the minimum integer common to both arrays.
If there is no common integer amongst nums1 and nums2, return -1.

Note that an integer is said to be common to nums1 and nums2
if both arrays have at least one occurrence of that integer.

Solution
✏️ Easy Python solution
# Intuition
Use only the built-in language tools

# Approach
Simple steps:
1) Compress the lists by making them sets
2) Find a new set as an intersection of lists
3) Sort the new set
4) Find the first element of the received list.

The methods specified in the tags are confusing in the right way!
Not needed:  Hash Table, Two Pointers, Binary Search
"""




# Runtime 334 ms Beats 96.88%
# Memory 37.42 MB Beats 16.94%

def getCommon(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: int
    """
    s=set(nums1) & set(nums2)
    if len(s) == 0: return -1
    else: return sorted(s)[0]


print(getCommon(nums1 = [2,4], nums2 = [1,2]))