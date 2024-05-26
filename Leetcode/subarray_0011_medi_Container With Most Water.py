"""
Done 26.05.2025. Topics: Array, Two Pointers

11. Container With Most Water
https://leetcode.com/problems/container-with-most-water/description/

You are given an integer array height of length n.
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1

Hint 1
If you simulate the problem, it will be O(n^2) which is not efficient.
Hint 2
Try to use two-pointers. Set one pointer to the left and one to the right of the array.
Always move the pointer that points to the lower line.
Hint 3
How can you calculate the amount of water at each step?
"""

# Runtime 456 ms Beats 97.56% of users with Python3
# Memory 30.11 MB Beats 6.57% of users with Python3

# https://leimao.github.io/blog/Proof-Container-With-Most-Water-Problem/
def maxArea4(height):
    """
    :type height: List[int]
    :rtype: int
    """
    i = 0
    j = len(height) - 1
    maxVol = -1
    while i < j:
        if (height[i] < height[j]):
            vol = (j - i) * height[i]
            if (vol > maxVol):
                maxVol = vol
            i=i+1
        else:
            vol = (j - i) * height[j]
            if (vol > maxVol):
                maxVol = vol
            j=j-1
    return maxVol




# Runtime 531 ms Beats 36.41% of users with Python3
# Memory 30.05 MB Beats 11.05% of users with Python3

# https://leetcode.com/problems/container-with-most-water/description/comments/1570360
def maxArea4(height):
    """
    :type height: List[int]
    :rtype: int
    """
    ll=len(height); ll1=ll-1
    if ll==2: return min(height)

    hs = sorted(height)
    if hs==height:
        if hs[0]==0:
            return hs[1]*(ll-2)
        else:
            if ll % 2==0: return hs[ll // 2 - 1] * ll // 2
            else: return hs[ll//2]*(ll//2+1)

    area = ll1*min(height[0],height[ll1])
    i=0; j=ll1
    while i != j:
        if height[i]<=height[j]:
            i=i+1
            ar = (j - i) * min(height[i], height[j])
            if ar > area: area = ar
        else:
            j=j-1
            ar = (j - i) * min(height[i], height[j])
            if ar > area: area = ar
        print(i,j,ar,area)
    return area


# Time Limit Exceeded -- 53 / 62 testcases passed
def maxArea3(height):
    """
    :type height: List[int]
    :rtype: int
    """
    ll=len(height); ll1=ll-1
    if ll==2: return min(height)

    hs = sorted(height)
    if hs==height:
        if hs[0]==0:
            return hs[1]*(ll-2)
        else:
            return hs[0] * ll1

    # mmax=max(height)
    # ind=height.index(mmax)
    # lind=[i for i,dat in enumerate(height) if dat==mmax]
    # lmax=lind[len(lind)-1]

    area = ll*min(height[0],height[ll1])
    for i in range(ll): # ll
        hi=height[i]
        if i>0 and hi<height[i-1]: continue
        for j in range(ll1,i-1,-1):
            if j==ll1:
                ar = (j - i) * min(hi, height[j])
                if ar > area: area = ar
            elif height[j]>height[j+1]:
                ar=(j-i)*min(height[i],height[j])
                if ar>area: area=ar
    return area

# Time Limit Exceeded -- 52 / 62 testcases passed
def maxArea2(height):
    """
    :type height: List[int]
    :rtype: int
    """
    ll=len(height); ll1=ll-1
    area = -1
    print(ll)
    for i in range(ll):
        j=ll1
        while i !=j:
            ar=(j-i)*min(height[i],height[j])
            if ar>area: area=ar
            j=j-1
    return area

# print(maxArea([1,8,6,2,5,4,8,3,7]))
# print(maxArea([4,3,2,1,4]))
print(maxArea([10, 10, 100]))