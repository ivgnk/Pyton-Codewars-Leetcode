"""
03.05.2024
477. Total Hamming Distance
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
Given an integer array nums, return the sum of Hamming distances between all the pairs of the integers in nums.

Example 1:
Input: nums = [4,14,2]
Output: 6
Explanation: In binary representation, the 4 is 0100, 14 is 1110, and 2 is 0010 (just
showing the four bits relevant in this case).
The answer will be:
HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 + 2 + 2 = 6.

Example 2:
Input: nums = [4,14,4]
Output: 4
"""

# Time Limit Exceeded -- 35 / 46 testcases passed

def totalHammingDistance(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ll = len(nums)
    nb=[bin(i)[2:] for i in nums]
    nbl=[len(nbi) for nbi in nb]
    mm=max(nbl)
    nbm=['0'*(mm-nbl[i])+nb[i] if nbl[i]<mm else nb[i] for i in range(ll)]
    n = 0
    for i in range(ll):
        for j in range(i+1,ll):
            n += sum([1 for k in range(mm) if nbm[i][k] != nbm[j][k]])
    return n

print(totalHammingDistance([4,14,2]))