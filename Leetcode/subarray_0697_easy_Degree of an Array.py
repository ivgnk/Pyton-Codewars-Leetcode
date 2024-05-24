"""
Done 25.05.2024. Topics: Array, Hash Table
697. Degree of an Array
https://leetcode.com/problems/degree-of-an-array/description/

Given a non-empty array of non-negative integers nums, the degree of this array
is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums,
that has the same degree as nums.

Example 1:
Input: nums = [1,2,2,3,1]
Output: 2
Explanation:
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.

Example 2:
Input: nums = [1,2,2,3,1,4,2]
Output: 6
Explanation:
The degree is 3 because the element 2 is repeated 3 times.
So [2,2,3,1,4,2] is the shortest subarray, therefore returning 6.

Hint 1
Say 5 is the only element that occurs the most number of times - for example,
nums = [1, 5, 2, 3, 5, 4, 5, 6]. What is the answer?
"""

# Runtime 156 ms Beats 93.30% of users with Python
# Memory 14.49 MB Beats 5.74% of users with Python

# https://leetcode.com/problems/degree-of-an-array/solutions/349801/solution-in-python-3-beats-98/
# by https://leetcode.com/u/junaidmansuri/
def findShortestSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    di = dict()
    for i,d in enumerate(nums):
        if d in di:
            di[d].append(i)
        else:
            di[d] = [i]

    mmax=max([len(v) for k,v in di.items()])
    return min(len(nums[v[0]:v[-1]+1]) for k,v in di.items() if len(v)==mmax)


# Runtime 1868 ms Beats 7.18% of users with Python
# Memory 13.35 MB Beats 52.15% of users with Python
def findShortestSubArray2(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    dd = dict()
    for i in nums:
        if i in dd:
            dd[i] += 1
        else:
            dd[i] = 1
    lst = sorted([[v, k] for k, v in dd.items()], reverse=True)
    lst2 = [v for v in lst if v[0] == lst[0][0]]

    mmin = 100000
    for dat in lst2:
        l = [i for i, d in enumerate(nums) if d == dat[1]]
        mmin = min(mmin, len(nums[l[0]:l[-1] + 1]))
    return mmin


# Runtime 1879 ms Beats 7.18% of users with Python
# Memory 13.76 MB Beats 44.02% of users with Python

from collections import Counter
def findShortestSubArray3(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    dd=dict(Counter(nums))
    lst=sorted([[v,k] for k,v in dd.items()],reverse=True)
    lst2=sorted([v for v in lst if v[0]==lst[0][0]])

    mmin = 100000
    for dat in lst2:
        l=[i for i,d in enumerate(nums) if d==dat[1]]
        mmin=min(mmin,len(nums[l[0]:l[-1]+1]))
    return mmin


print(findShortestSubArray([1,2,2,3,1]))