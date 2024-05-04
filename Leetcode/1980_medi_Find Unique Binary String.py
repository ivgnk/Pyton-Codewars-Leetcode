"""
work 04.05.2024
1980. Find Unique Binary String
https://leetcode.com/problems/find-unique-binary-string/description/

Given an array of strings nums containing n unique binary strings each of length n,
return a binary string of length n that does not appear in nums.
If there are multiple answers, you may return any of them.

Example 1:
Input: nums = ["01","10"]
Output: "11"
Explanation: "11" does not appear in nums. "00" would also be correct.

Example 2:
Input: nums = ["00","01"]
Output: "11"
Explanation: "11" does not appear in nums. "10" would also be correct.

Example 3:
Input: nums = ["111","011","001"]
Output: "101"
Explanation: "101" does not appear in nums. "000", "010", "100", and "110" would also be correct.
"""

from icecream import ic
from itertools import product

def findDifferentBinaryString2(nums):
    """
    :type nums: List[str]
    :rtype: str
    """
    # https://stackoverflow.com/questions/25991292/python-all-possible-combinations-of-0-1-of-length-k
    k = len(nums[0])
    lst = list(product(range(2), repeat=k))
    # for lsst in lst:
    #     # s=''
    #     # for i in range(k):
    #     #     s = s+ str(lsst[i])
    #     # ss.append(s)
    #     s=''.join(str(lsst[i]) for i in range(k))
    #     ss.append(s)
    ss = [''.join(str(lsst[i]) for i in range(k)) for lsst in lst]
    sset=set(ss)
    snum=set(ss)
    s2=sset-snum
    print(lst)
    print(ss)
    return list(s2)[0]

# Runtime 6450 ms Beats 5.33% of users with Python
# Memory 35.20 MB Beats 5.33% of users with Python
def findDifferentBinaryString3(nums):
    k = len(nums[0])
    lst = list(product(range(2), repeat=k))
    ss = [''.join(str(lsst[i]) for i in range(k)) for lsst in lst]
    sset=set(ss)
    snum=set(nums)
    s2=sset-snum
    # print(sset,snum,s2)
    return list(s2)[0]

# nums = ["01","10"]
# nums = ["00","01"]
# nums = ["111","011","001"]
def findDifferentBinaryString(nums):
    # https://leetcode.com/problems/find-unique-binary-string/solutions/2823559/python-solution-o-n/
    ans = []
    for i in range(len(nums)):
        digit = nums[i][i]
        if digit == '1':
            ans.append('0')
        else:
            ans.append('1')
        print(i,ans,digit)
    return "".join(ans)



print(findDifferentBinaryString( ["011","001","111"]))
