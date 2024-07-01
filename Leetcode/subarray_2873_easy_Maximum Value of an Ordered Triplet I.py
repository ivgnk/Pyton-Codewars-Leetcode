"""
Done 01.07.2024. Topics: Array
2873. Maximum Value of an Ordered Triplet I
https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-i/description/

You are given a 0-indexed integer array nums.
Return the maximum value over all triplets of indices (i, j, k) such that i < j < k.
If all such triplets have a negative value, return 0.
The value of a triplet of indices (i, j, k) is equal to (nums[i] - nums[j]) * nums[k].

Example 1:
Input: nums = [12,6,1,2,7]
Output: 77
Explanation: The value of the triplet (0, 2, 4) is (nums[0] - nums[2]) * nums[4] = 77.
It can be shown that there are no ordered triplets of indices with a value greater than 77.

Example 2:
Input: nums = [1,10,3,4,19]
Output: 133
Explanation: The value of the triplet (1, 2, 4) is (nums[1] - nums[2]) * nums[4] = 133.
It can be shown that there are no ordered triplets of indices with a value greater than 133.

Example 3:
Input: nums = [1,2,3]
Output: 0
Explanation: The only ordered triplet of indices (0, 1, 2) has a negative value of (nums[0] - nums[1]) * nums[2] = -3. Hence, the answer would be 0.

Constraints:
3 <= nums.length <= 100
1 <= nums[i] <= 106

Hint 1
Use three nested loops to find all the triplets.
"""

# Runtime 91 ms Beats 76.00%
# Memory 11.63 MB Beats 41.33%

def maximumTripletValue(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ll = len(nums);  ll1 = ll - 1
    res1 = 0
    for i in range(ll - 2):
        for j in range(i + 1, ll1):
            nn = nums[i] - nums[j]
            for k in range(j + 1, ll):
                rr = nn * nums[k]
                if rr > res1:
                    res1 = rr
    return res1


# Runtime 115 ms Beats 62.67%
# Memory 11.50 MB Beats 96.00%
# Runtime 102 ms Beats 68.00%
# Memory 11.40 MB Beats 96.00%
def maximumTripletValue3(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ll = len(nums);    ll1 = ll - 1
    res1 = 0
    for i in range(ll - 2):
        for j in range(i + 1, ll1):
            nn = nums[i] - nums[j]
            for k in range(j + 1, ll):
                rr = nn * nums[k]
                if rr > 0:
                    res1 = max(rr, res1)
    return res1


# Runtime 144 ms Beats 45.33%
# Memory 11.62 MB Beats 41.33%
# Runtime 138 ms Beats 49.33%
# Memory 11.68 MB Beats 41.33%
# Runtime 133 ms Beats 49.33%
# Memory 11.52 MB Beats 73.33%
def maximumTripletValue2(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ll = len(nums); ll1=ll - 1
    res1 = 0
    for i in range(ll - 2):
        for j in range(i + 1, ll1):
            nn=nums[i] - nums[j]
            for k in range(j + 1, ll):
                res1 = max(nn*nums[k], res1)
    return res1

print(maximumTripletValue([12,6,1,2,7]))
print(maximumTripletValue([1,10,3,4,19]))
print(maximumTripletValue([1,2,3]))

