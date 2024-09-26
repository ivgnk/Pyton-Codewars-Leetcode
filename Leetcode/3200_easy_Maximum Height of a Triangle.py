"""
Done 26.09.2024. Topics: Array
3200. Maximum Height of a Triangle
https://leetcode.com/problems/maximum-height-of-a-triangle/description/

You are given two integers red and blue representing the count of red and blue colored balls.
You have to arrange these balls to form a triangle such that the 1st row will have 1 ball, the 2nd row will have 2 balls,
the 3rd row will have 3 balls, and so on.
All the balls in a particular row should be the same color, and adjacent rows should have different colors.
Return the maximum height of the triangle that can be achieved.

Example 1:
Input: red = 2, blue = 4
Output: 3
Explanation:
The only possible arrangement is shown above.

Example 2:
Input: red = 2, blue = 1
Output: 2
Explanation:
The only possible arrangement is shown above.

Example 3:
Input: red = 1, blue = 1
Output: 1

Example 4:
Input: red = 10, blue = 1
Output: 2
Explanation:
The only possible arrangement is shown above.

Constraints:
1 <= red, blue <= 100

Hint 1
Count the max height using both possibilities. That is, red ball as top and blue ball as top.
Hint 2
For counting the max height, use a simple for loop and remove the number of balls required at this level.

as hint for formula -not used
https://leetcode.com/problems/maximum-height-of-a-triangle/solutions/5391512/using-ap-sum-formula-t-c-o-1-intution-code/

Solution
✏️ Easy Python solution with separate calculation for even and odd number of red/blue balls
Intuition
The essence is reflected in the name of the solution

Approach
Do not forget to restore the number of balls on the second pass.
"""

from icecream import ic
import operator
from itertools import accumulate

from numpy.ma.core import append
from sympy.codegen.ast import break_

# Runtime 18 ms Beats 47.25%
# Memory 11.40 MB Beats 98.90%
# Runtime 17 ms Beats 52.75%
# Memory 11.42 MB Beats 93.41%
# Runtime 12 ms Beats 82.42%
# Memory 11.49 MB Beats 93.41%
# Time Complexity O(1)
# Space Complexity O(1)
def maxHeightOfTriangleN(red, blue):
    rb=red+blue
    if rb == 2: return 1
    elif rb == 3: return 2
    elif red == 1 or blue == 1:
        return 2
    rs=red; bs=blue
    nr1=0
    # odd red
    while red>=0 and blue>=0:
        nr1+=1
        if nr1%2==0:
            if nr1<=blue:
                blue-=nr1
            else:
                nr1-=1
                break
        else:
            if nr1 <= red:
                red -= nr1
            else:
                nr1 -= 1
                break
    ic(nr1)
    red=rs; blue=bs
    nr2=0
    while red>=0 and blue>=0:
        nr2+=1
        if nr2%2==0:
            if nr2<=red:
                red-=nr2
            else:
                nr2-=1
                break
        else:
            if nr2 <= blue:
                blue -= nr2
            else:
                nr2 -= 1
                break
    ic(nr2)
    return max(nr1, nr2)

def maxHeightOfTriangle(red, blue):
    if red>blue:
        if red==blue+1: return red
        else: return blue
    else:
        if blue==red+1: return blue
        else: return red



# ic(maxHeightOfTriangle(red = 4, blue = 4))
ic(maxHeightOfTriangle(red = 2, blue = 4))


def maxHeightOfTriangle_2(red, blue):
    rb=red + blue
    n=0
    rb1=rb
    p1=[];    p2=[]
    while rb1>0:
        n=n+1
        if n<=rb1:
            if n % 2 == 0:
                p2.append(n)
            else:
                p1.append(n)
        else: break



def maxHeightOfTriangle_(red, blue):
    """
    :type red: int
    :type blue: int
    :rtype: int
    """
    rb=red + blue
    pyr=[]; n=0
    rb1=rb
    while rb1>0:
        n=n+1
        rb1=rb1-n
        pyr.append(n)
    # seve_ = [i for i in pyr if i % 2 == 0]
    # seve2 = list(accumulate(seve_, operator.add))
    # sseve_=sum(seve_)
    # sodd_ = [i for i in pyr if i % 2 != 0]
    # sodd2 = list(accumulate(sodd_, operator.add))
    lp=len(pyr)
    pyr2=pyr[:]
    for i in range(1, lp):
            pyr2[i] = pyr2[i-1]+ pyr[i]
    # ssodd_=sum(sodd_)
    ic(pyr)
    # ic(seve_,sodd_,sseve_,ssodd_)
    ic(pyr2)
    # ic(seve2,sodd2)
    # if (red==seve_ and blue==sodd_) or (blue==seve_ and red==sodd_):
    #     return len(pyr)
    if rb == 2: return 1
    elif rb == 3: return 2
    elif red==1 or blue==1: return 2
    else:
        nn=-13
        for i in range(1,lp):
            if (red <= pyr[i] and blue >= pyr[i]) or (blue <= pyr[i] and  red >= pyr[i]):
                nn = i
                break
            # else: # i%2!=0
            #     if (red<=sodd_[i-1] and blue>=seve_[i]) or (blue <= sodd_[i-1] and red>=seve_[i]):
            #         nn =i
            #         break
    return nn

    #     if
    # rb1 = rb; n=0
    # while rb1>0:
    #     n = n + 1
    #     if n%2==0:
    #         if red>=n:
    #
    #
    #
    #
    # print(pyr,rb,sum(pyr))
    # for i in rrb:
    #     if i%2==0
    #         rt1.append()=n
    #     pass

