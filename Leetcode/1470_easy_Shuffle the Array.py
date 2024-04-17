"""
1470. Shuffle the Array
https://leetcode.com/problems/shuffle-the-array/description/

Given the array nums consisting of 2n elements in the form
[x1,x2,...,xn,y1,y2,...,yn].
Return the array in the form [x1,y1,x2,y2,...,xn,yn].
"""

# Runtime 38 ms Beats 47.41% of users with Python
# Memory 11.96 MB Beats 15.97% of users with Python

def shuffle(nums, n):
    """
    :type nums: List[int]
    :type n: int
    :rtype: List[int]
    """
    x=nums[:n]; y=nums[n:]
    res=[]
    for i in range(n):
        res.append(x[i])
        res.append(y[i])
    return res

print(shuffle(nums = [2,5,1,3,4,7], n = 3))