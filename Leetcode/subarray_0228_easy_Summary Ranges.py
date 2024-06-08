"""
Done 08.06.2024. Topics: Array
228. Summary Ranges
https://leetcode.com/problems/summary-ranges/description/

You are given a sorted unique integer array nums.
A range [a,b] is the set of all integers from a to b (inclusive).
Return the smallest sorted list of ranges that cover all the numbers in the array exactly.
That is, each element of nums is covered by exactly one of the ranges, and there is no
integer x such that x is in one of the ranges but not in nums.
Each range [a,b] in the list should be output as:
"a->b" if a != b
"a" if a == b

Example 1:
Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"

Example 2:
Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"
"""

# Runtime 38 ms Beats 30.43% of users with Python3
# Memory 16.48 MB Beats 81.88% of users with Python3
# Runtime 35 ms Beats 51.37% of users with Python3
# Memory 16.48 MB Beats 81.88% of users with Python3
def summaryRanges2(nums):
    """
    :type nums: List[int]
    :rtype: List[str]
    """
    ll=len(nums)
    if ll==0: return ''
    res=[]; prev=nums[0]
    for i in range(1,ll):
        if nums[i]!=nums[i-1]+1:
            if nums[i-1]==prev:
                res.append(str(nums[i-1]))
            else:
                res.append(f'{prev}->{nums[i-1]}')
                # if i==ll-1:
                #     res.append(str(nums[i]))
            prev=nums[i]
    else:
        if prev==nums[ll - 1]:
            res.append(str(nums[ll-1]))
        else: res.append(f'{prev}->{nums[ll - 1]}')
    return res

print(summaryRanges2([0,1,2,4,5,7]))
print(summaryRanges2([0,2,3,4,6,8,9]))


