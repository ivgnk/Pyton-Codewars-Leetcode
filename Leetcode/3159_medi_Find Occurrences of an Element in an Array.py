"""
Done 05.08.2024. Topics: Array, Hash Table
3159. Find Occurrences of an Element in an Array
https://leetcode.com/problems/find-occurrences-of-an-element-in-an-array/description/

You are given an integer array nums, an integer array queries, and an integer x.

For each queries[i], you need to find the index of the
queries[i]th occurrence of x in the nums array.
If there are fewer than queries[i] occurrences of x, the answer should be -1 for that query.

Return an integer array answer containing the answers to all queries.

Example 1:
Input: nums = [1,3,1,7], queries = [1,3,2,4], x = 1
Output: [0,-1,2,-1]
Explanation:
For the 1st query, the first occurrence of 1 is at index 0.
For the 2nd query, there are only two occurrences of 1 in nums, so the answer is -1.
For the 3rd query, the second occurrence of 1 is at index 2.
For the 4th query, there are only two occurrences of 1 in nums, so the answer is -1.

Example 2:
Input: nums = [1,2,3], queries = [10], x = 5
Output: [-1]
Explanation:
For the 1st query, 5 doesn't exist in nums, so the answer is -1.

Constraints:
1 <= nums.length, queries.length <= 10**5
1 <= queries[i] <= 10**5
1 <= nums[i], x <= 10**4

Hint 1
Compress the array nums and save all the occurrences of each element in the separate array
"""

# Runtime 1334 ms Beats 75.34%
# Memory 31.71 MBBeats 8.90%
# Runtime 1325 ms Beats 83.56%
# Memory 31.62 MB Beats 21.92%
def occurrencesOfElement(nums, queries, x):
    """
    :type nums: List[int]
    :type queries: List[int]
    :type x: int
    :rtype: List[int]
    """
    prep = [i for i in range(len(nums)) if nums[i] == x]
    ll = len(prep)
    return [-1 if q > ll else prep[q-1] for q in queries ]

print(occurrencesOfElement(nums = [1,3,1,7], queries = [1,3,2,4], x = 1))

# Runtime 1343 ms Beats 63.70%
# Memory 31.52 MB Beats 57.53%
def occurrencesOfElement2(nums, queries, x):
    """
    :type nums: List[int]
    :type queries: List[int]
    :type x: int
    :rtype: List[int]
    """
    prep = [i for i in range(len(nums)) if nums[i] == x]
    res = []
    ll = len(prep)
    for q in queries:
        if q > ll:
            res.append(-1)
        else:
            res.append(prep[q-1])
    return res

