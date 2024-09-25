"""
Done 25.09.2024. Topics: Array, Greedy
605. Can Place Flowers
https://leetcode.com/problems/can-place-flowers/description/

You have a long flowerbed in which some of the plots are planted, and some are not.
However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's,
where 0 means empty and 1 means not empty, and an integer n,
return true if n new flowers can be planted in the flowerbed
[without violating the no-adjacent-flowers rule]
(не нарушая правила несмежности цветов)
and false otherwise.

Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: true

Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: false

Constraints:
1 <= flowerbed.length <= 2*10**4
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length

Solution
✏️ Easy Python solution based on tips in discussion
# Intuition
Based on tips in discussion
1 tip - https://leetcode.com/problems/can-place-flowers/description/comments/1838260
Short statement: find 0,0,0 and add flower
2 tip - to make it easier to work with tip №1, add additional zeros to the beginning and end

# Approach
Additionally consider the case of flowerbed length == 1
"""

# Main Approach (page 3 sorted by Old to New
#
# Start a for loop to iterate through each spot in the flower bed array.
# Check if the current spot is empty and the spots before and after it are also empty (or do not exist).
# If a new flower can be planted in the current spot, decrement n (the number of flowers left to plant)
# and skip the next spot in the iteration (since it cannot have a flower planted in it).
#
# https://leetcode.com/problems/can-place-flowers/description/comments/1838260
#
# nnew=[0]+flowerbed+[0] 0 another hont in diccussion

# Runtime 132 ms Beats 57.96%
# Memory 16.94 MB Beats 21.73%
# Runtime 130 ms Beats 68.83%
# Memory 17.02 MB Beats 5.18%
# Runtime 129 ms Beats 73.37%
# Memory 16.86 MB Beats 72.08%
# Runtime 128 ms Beats 77.66%
# Memory 16.97 MB Beats 21.73%
# Time Complexity O(N)
# Space Complexity O(N)

def canPlaceFlowers(flowerbed, n):
    ll=len(flowerbed)
    if ll==1:
        if n == 0: return True
        if n == 1 and flowerbed[0]==0: return True
        else: return False
    nn=[0]+flowerbed+[0]
    cnt=0
    i=1
    while i<ll+1:
        if nn[i-1]==0 and nn[i]==0 and nn[i+1]==0:
            cnt +=1
            i+=2
        else: i=i+1
    return cnt>=n

print(canPlaceFlowers(flowerbed = [1,0,0,0,1], n = 1))
print(canPlaceFlowers(flowerbed = [1,0,0,0,1], n = 2))

        # Wrong Answer - 124 / 130 testcases passed
def canPlaceFlowers22(flowerbed, n):
    """
    :type flowerbed: List[int]
    :type n: int
    :rtype: bool
    """
    ll=len(flowerbed)
    if ll==1 and flowerbed[0]==0: return True
    s0=[0,0]
    # res = [flowerbed[i:i + 2] == s0 for i in range(0, ll, 2)]
    res = [(flowerbed[i:i + 2] == s0) and (flowerbed[i-1] !='1' and flowerbed[i+1] !=1) for i in range(0, ll, 2)]
    if ll%2 !=0:
        if flowerbed[-2:]==s0:
            res.append(True)
    nn = sum(res)
    print(nn)

    return nn>=n
