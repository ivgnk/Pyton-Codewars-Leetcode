"""
Done 05.09.2024. Topics: Array, Hash Table
128. Longest Consecutive Sequence
https://leetcode.com/problems/longest-consecutive-sequence/description/

Given an unsorted array of integers nums,
return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Constraints:
0 <= nums.length <= 10**5
-10**9 <= nums[i] <= 10**9

Solution
✏️ Not the most obvious Python solution

Intuition
You can use tricky tricks like in
stackoverflow.com/questions/49787852/group-consecutive-integers-together
But the simplest thing is.
To get a convenient desired sequence:
1) remove duplicates
2) sort

# Approach
For the increasing sequence to be searched for, the next element must be one more than the previous one (saved with in the list)

"""

# stackoverflow.com/questions/49787852/group-consecutive-integers-together
# Runtime 346 ms Beats 70.43%
# Memory 28.89 MB Beats 45.47%

def longestConsecutive(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if nums == []: return 0
    nums=sorted(set(nums))
    res= [nums[0]]
    i = 1; mmax=0
    while i < len(nums):
        if res[-1] + 1 != nums[i]:
            mmax=max(mmax,len(res))
            res=[nums[i]]
        else: res.append(nums[i])
        i += 1
        # print(i,res)
    mmax = max(mmax, len(res))
    return mmax

print(longestConsecutive([100,4,200,1,3,2]))
print(longestConsecutive([0,3,7,2,5,8,4,6,0,1]))