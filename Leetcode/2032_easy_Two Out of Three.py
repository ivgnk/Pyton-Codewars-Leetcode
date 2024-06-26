"""
Done 27.06.2024. Topics: Array
2032. Two Out of Three
https://leetcode.com/problems/two-out-of-three/description/

Given three integer arrays nums1, nums2, and nums3, return a distinct array containing all the values that
are present in at least two out of the three arrays. You may return the values in any order.

Example 1:
Input: nums1 = [1,1,3,2], nums2 = [2,3], nums3 = [3]
Output: [3,2]
Explanation: The values that are present in at least two arrays are:
- 3, in all three arrays.
- 2, in nums1 and nums2.

Example 2:
Input: nums1 = [3,1], nums2 = [2,3], nums3 = [1,2]
Output: [2,3,1]
Explanation: The values that are present in at least two arrays are:
- 2, in nums2 and nums3.
- 3, in nums1 and nums2.
- 1, in nums1 and nums3.

Example 3:
Input: nums1 = [1,2,2], nums2 = [4,3,3], nums3 = [5]
Output: []
Explanation: No value is present in at least two arrays.

Hint 1
What data structure can we use to help us quickly find whether an element belongs in an array?
Hint 2
Can we count the frequencies of the elements in each array?
"""


# Runtime 41 ms Beats 88.36%
# Memory 11.50 MB Beats 68.78%
def twoOutOfThree(nums1, nums2, nums3):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :type nums3: List[int]
    :rtype: List[int]
    """
    s1=set(nums1)
    s2=set(nums2)
    s3=set(nums3)
    r1=[se for se in s1 if se in s2 or se in s3]
    r2=[se for se in s2 if se in s1 or se in s3]
    r3=[se for se in s3 if se in s1 or se in s2]
    return list(set(r1+r2+r3))

print(twoOutOfThree(nums1 = [1,1,3,2], nums2 = [2,3], nums3 = [3]))
print(twoOutOfThree(nums1 = [3,1], nums2 = [2,3], nums3 = [1,2]))
print(twoOutOfThree(nums1 = [1,2,2], nums2 = [4,3,3], nums3 = [5]))

