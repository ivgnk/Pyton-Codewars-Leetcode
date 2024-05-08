"""
Done 08.05.2024. Topics: Array, Hash Table, Counting

2404. Most Frequent Even Element
https://leetcode.com/problems/most-frequent-even-element/

Given an integer array nums, return the most frequent even element.
If there is a tie, return the smallest one. If there is no such element, return -1.

Example 1:
Input: nums = [0,1,2,2,4,4,1]
Output: 2
Explanation:
The even elements are 0, 2, and 4. Of these, 2 and 4 appear the most.
We return the smallest one, which is 2.

Example 2:
Input: nums = [4,4,4,9,2,4]
Output: 4
Explanation: 4 is the even element appears the most.

Example 3:
Input: nums = [29,47,21,41,13,37,25,7]
Output: -1
Explanation: There is no even element.

Hint 1
Could you count the frequency of each even element in the array?
Hint 2
Would a hashmap help?
"""

from collections import Counter
from icecream import ic

# Runtime 238 ms Beats 28.53% of users with Python3
# Memory 17.21 MB Beats 14.22% of users with Python3
# Runtime 236 ms Beats 30.84% of users with Python3
# Memory 17.21 MB Beats 14.22% of users with Python3
# Runtime 225 ms Beats 48.44% of users with Python3
# Memory 17.15 MB Beats 32.27% of users with Python3

def mostFrequentEven(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    lst=[s for i,s in enumerate(nums) if s%2==0]
    if lst == []: return -1

    dd=dict(Counter(lst))
    if len(dd)==1: return lst[0]

    lst2=sorted([[v,k] for k,v in dd.items()],reverse=True)
    ll2=len(lst2)
    if all (lst2[i][0]==lst2[i-1][0] for i in range(1,ll2)):
        return min(lst2[i][1] for i in range(ll2))

    nn = lst2[0][0]
    res=[];i=0
    while nn == lst2[i][0] and i<ll2-1:
        res.append(lst2[i][1])
        i = i + 1
    print(res,i,ll2)
    return min(res)

ic(mostFrequentEven([0,1,2,2,4,4,1]))
ic(mostFrequentEven([8154,9139,8194,3346,5450,9190,133,8239,4606,8671,8412,6290]))
