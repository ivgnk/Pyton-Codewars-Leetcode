"""
Done 09.05.2024. Topics: Array, Hash Table, Two Pointers
2570. Merge Two 2D Arrays by Summing Values
https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/description/

You are given two 2D integer arrays nums1 and nums2.
nums1[i] = [idi, vali] indicate that the number with the id idi has a value equal to vali.
nums2[i] = [idi, vali] indicate that the number with the id idi has a value equal to vali.
Each array contains unique ids and is sorted in ascending order by id.
Merge the two arrays into one array that is sorted in ascending order by id, respecting the following conditions:

Only ids that appear in at least one of the two arrays should be included in the resulting array.
Each id should be included only once and its value should be the sum of the values of this id in the two arrays.
If the id does not exist in one of the two arrays then its value in that array is considered to be 0.
Return the resulting array. The returned array must be sorted in ascending order by id.

Example 1:
Input: nums1 = [[1,2],[2,3],[4,5]], nums2 = [[1,4],[3,2],[4,1]]
Output: [[1,6],[2,3],[3,2],[4,6]]
Explanation: The resulting array contains the following:
- id = 1, the value of this id is 2 + 4 = 6.
- id = 2, the value of this id is 3.
- id = 3, the value of this id is 2.
- id = 4, the value of this id is 5 + 1 = 6.

Example 2:
Input: nums1 = [[2,4],[3,6],[5,5]], nums2 = [[1,3],[4,3]]
Output: [[1,3],[2,4],[3,6],[4,3],[5,5]]
Explanation: There are no common ids, so we just include each id with its value in the resulting list.

Hint 1
Use a dictionary/hash map to keep track of the indices and their sum values.
"""

# Runtime 33 ms Beats 87.50% of users with Python
# Memory 11.91 MB Beats 23.61% of users with Python
def mergeArrays(self, nums1, nums2):
    """
    :type nums1: List[List[int]]
    :type nums2: List[List[int]]
    :rtype: List[List[int]]
    """
    d1 = dict(nums1);    d2 = dict(nums2)
    for k, v in d2.items():
        if k in d1:
            d1[k] = d1[k] + v
        else:
            d1[k] = v
    return sorted([[k, v] for k, v in d1.items()])


# Runtime 38 ms Beats 61.11% of users with Python
# Memory 11.79 MB Beats 91.67% of users with Python
def mergeArrays2(nums1, nums2):
    """
    :type nums1: List[List[int]]
    :type nums2: List[List[int]]
    :rtype: List[List[int]]
    """
    d1 = dict(nums1); d2 = dict(nums2)
    rd=dict()
    for k,v in d1.items():
        rd[k]=v
    for k,v in d2.items():
        if k in rd:
            rd[k] = rd[k]+v
        else:
            rd[k] = v
    return sorted([[k,v] for k,v in rd.items()])




print(mergeArrays(nums1 = [[1,2],[2,3],[4,5]], nums2 = [[1,4],[3,2],[4,1]]))