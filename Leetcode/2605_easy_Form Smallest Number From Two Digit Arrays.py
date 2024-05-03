"""
Done 03.05.2024
2605. Form Smallest Number From Two Digit Arrays
Given two arrays of unique digits nums1 and nums2,
return the smallest number that contains at least one digit from each array.

Example 1:
Input: nums1 = [4,1,3], nums2 = [5,7]
Output: 15
Explanation: The number 15 contains the digit 1 from nums1 and the digit 5 from nums2.
It can be proven that 15 is the smallest number we can have.

Example 2:
Input: nums1 = [3,5,2,6], nums2 = [3,1,7]
Output: 3
Explanation: The number 3 contains the digit 3 which exists in both arrays.
"""

# Runtime 11 ms Beats 91.18% of users with Python
# Memory 11.78 MB Beats 10.29% of users with Python

def minNumber(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: int
    """
    s1=set(nums1); s2=set(nums2)
    ss=sorted(s1.intersection(s2))

    m1 = min(nums1)
    m2 = min(nums2)
    print(m1,m2)
    if m1==m2:return m1
    elif ss !=[]:
        return ss[0]

    if m1<m2 and m2 in nums1: return m2
    if m2<m1 and m1 in nums2: return m1

    if m1<m2: return int(str(m1)+str(m2))
    else: return int(str(m2)+str(m1))

# print(minNumber(nums1 = [4,1,3], nums2 = [5,7]))
print(minNumber(nums1 = [3,5,2,6], nums2 = [3,1,7]))

