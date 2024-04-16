"""
2001. Number of Pairs of Interchangeable Rectangles
https://leetcode.com/problems/number-of-pairs-of-interchangeable-rectangles/description/

You are given n rectangles represented by a 0-indexed 2D integer array rectangles,
where rectangles[i] = [widthi, heighti] denotes the width and height of the ith rectangle.
Two rectangles i and j (i < j) are considered interchangeable if they have the same width-to-height ratio.
More formally, two rectangles are interchangeable if widthi/heighti == widthj/heightj
(using decimal division, not integer division).
Return the number of pairs of interchangeable rectangles in rectangles.

Example 1:
Input: rectangles = [[4,8],[3,6],[10,20],[15,30]]
Output: 6
Explanation: The following are the interchangeable pairs of rectangles by index (0-indexed):
- Rectangle 0 with rectangle 1: 4/8 == 3/6.
- Rectangle 0 with rectangle 2: 4/8 == 10/20.
- Rectangle 0 with rectangle 3: 4/8 == 15/30.
- Rectangle 1 with rectangle 2: 3/6 == 10/20.
- Rectangle 1 with rectangle 3: 3/6 == 15/30.
- Rectangle 2 with rectangle 3: 10/20 == 15/30.
Example 2:

Input: rectangles = [[4,5],[7,8]]
Output: 0
Explanation: There are no interchangeable pairs of rectangles.
"""

# Time Limit Exceeded -- 41 / 46 testcases passed

def interchangeableRectangles2(rectangles) -> int:
    n = 0; ll = len(rectangles)
    lst = [rectangles[i][0] / rectangles[i][1] for i in range(ll)]
    for i in range(ll):
        for j in range(i + 1, ll):
            n = n + 1 if lst[i] == lst[j] else n
    return n


def interchangeableRectangles(rectangles):
    """
    :type rectangles: List[List[int]]
    :rtype: int
    """
    ll=len(rectangles)
    lst=[rectangles[i][0]/rectangles[i][1] for i in range(ll)]
    # for i in range(ll):
    #     for j in range(i + 1, ll):
    #         if lst[i]==lst[j]: lst2.append(1)
    lst2=[1
          for i in range(ll)
            for j in range(i + 1, ll)
                if lst[i]==lst[j]]
    if lst2==[]: return 0
    else: return sum(lst2)

print(interchangeableRectangles([[4,5],[7,8]]))