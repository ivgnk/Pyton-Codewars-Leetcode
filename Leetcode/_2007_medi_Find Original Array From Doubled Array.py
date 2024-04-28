"""
28.04.2024 -- Time Limit Exceeded -- 175 / 179 testcases passed
2007. Find Original Array From Doubled Array
An integer array original is transformed into a doubled array changed
by appending twice the value of every element in original,
and then randomly shuffling the resulting array.
Given an array changed, return original if changed is a doubled array.
If changed is not a doubled array, return an empty array.
The elements in original may be returned in any order.

Example 1:
Input: changed = [1,3,4,2,6,8]
Output: [1,3,4]
Explanation: One possible original array could be [1,3,4]:
- Twice the value of 1 is 1 * 2 = 2.
- Twice the value of 3 is 3 * 2 = 6.
- Twice the value of 4 is 4 * 2 = 8.
Other original arrays could be [4,3,1] or [3,1,4].

Example 2:
Input: changed = [6,3,0,1]
Output: []
Explanation: changed is not a doubled array.

Example 3:
Input: changed = [1]
Output: []
Explanation: changed is not a doubled array.
"""

# I did it according to Hint1-3 and bypassing pathological cases,
# I got "Time Limit Exceeded 175 / 179 test cases passed".
# Apparently, you do not need to believe Hint1-3 and delete elements,
# this increases the work time

from icecream import ic
def findOriginalArray(changed):
    """
    :type changed: List[int]
    :rtype: List[int]
    """
    lc_=len(changed)
    if changed==[] or lc_==1: return []
    sc=sorted(changed)
    if sc.count(0) == lc_: return sc[:lc_ // 2]
    res=[]
    while sc !=[]:
        d=sc[0]*2
        if sc[0]==0 and sc.count(0)>1:
            res.append(0)
            del sc[0]
            del sc[0]
        elif sc[0]==0:return []
        elif sc.count(d)>0:
            res.append(sc[0])
            sc.remove(d)
            sc.remove(sc[0])
        else: return []
    return res

# print(findOriginalArray([1,3,4,2,6,8]))
print(findOriginalArray([6,3,0,1]))
# print(findOriginalArray([0,3,2,4,6,0]))
# print([1,3,4,2,6,8].index(2))