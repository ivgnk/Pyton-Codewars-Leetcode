"""
Done 05.06.2024. Topics: Binary Search

1237. Find Positive Integer Solution for a Given Equation
https://leetcode.com/problems/find-positive-integer-solution-for-a-given-equation/description/

Given a callable function f(x, y) with a hidden formula and a value z, reverse engineer the formula and
return all positive integer pairs x and y where f(x,y) == z. You may return the pairs in any order.
While the exact formula is hidden, the function is monotonically increasing, i.e.:

f(x, y) < f(x + 1, y)
f(x, y) < f(x, y + 1)
The function interface is defined like this:

interface CustomFunction {
public:
  // Returns some positive integer f(x, y) for two positive integers x and y based on a formula.
  int f(int x, int y);
};
We will judge your solution as follows:

The judge has a list of 9 hidden implementations of CustomFunction,
along with a way to generate an answer key of all valid pairs for a specific z.
The judge will receive two inputs: a function_id (to determine which implementation to test your code with), and the target z.
The judge will call your findSolution and compare your results with the answer key.
If your results match the answer key, your solution will be Accepted.

Example 1:
Input: function_id = 1, z = 5
Output: [[1,4],[2,3],[3,2],[4,1]]
Explanation: The hidden formula for function_id = 1 is f(x, y) = x + y.
The following positive integer values of x and y make f(x, y) equal to 5:
x=1, y=4 -> f(1, 4) = 1 + 4 = 5.
x=2, y=3 -> f(2, 3) = 2 + 3 = 5.
x=3, y=2 -> f(3, 2) = 3 + 2 = 5.
x=4, y=1 -> f(4, 1) = 4 + 1 = 5.

Example 2:
Input: function_id = 2, z = 5
Output: [[1,5],[5,1]]
Explanation: The hidden formula for function_id = 2 is f(x, y) = x * y.
The following positive integer values of x and y make f(x, y) equal to 5:
x=1, y=5 -> f(1, 5) = 1 * 5 = 5.
x=5, y=1 -> f(5, 1) = 5 * 1 = 5.

Constraints:
1 <= function_id <= 9
1 <= z <= 100
It is guaranteed that the solutions of f(x, y) == z will be in the range 1 <= x, y <= 1000.
It is also guaranteed that f(x, y) will fit in 32 bit signed integer if 1 <= x, y <= 1000.

Hint 1
Loop over 1 ≤ x,y ≤ 1000 and check if f(x,y) == z.
"""

# https://leetcode.com/problems/find-positive-integer-solution-for-a-given-equation/solutions/2956705/python-efficient-solution-beats-92-easy-to-understand/
# https://leetcode.com/problems/find-positive-integer-solution-for-a-given-equation/solutions/2763738/python3-easy-solution/



# Runtime 8147 ms Beats 17.50% of users with Python
# Memory 11.52 MB Beats 70.00% of users with Python
def findSolution0(customfunction, z):
    """
    :type num: int
    :type z: int
    :rtype: List[List[int]]
    """
    rr = range(1, 1001)
    return [[i, j] for i in rr
            for j in rr
            if customfunction.f(i, j) == z]

# Runtime 653 ms Beats 24.27% of users with Python3
# Memory 16.43 MB Beats 80.21% of users with Python3

def findSolution2(customfunction, z):
    """
    :type num: int
    :type z: int
    :rtype: List[List[int]]
    """
    rr = range(1, 1001)
    m = 99
    res=[]; isav=0; jsav=0; isbreak=False
    for i in rr:
        for j in rr:
            dat=customfunction.f(i, j)
            if dat == z: res.append([i,j])
            elif dat>z:
                if isav==0 and jsav==0:
                    isav=i; jsav=j
                elif i>isav+m and j>jsav+m:
                    isbreak = True
                    break
        if isbreak: return res
    return res

def f1(x,y):
    return x+y

# TLE
def findSolution(customfunction, z):
    im,jm=0,0
    i,j=1000,1000
    while customfunction(i, j) > z*3:
        medi = im + (i - im)//2
        medj = jm + (j - jm) // 2
        if customfunction(medi, medj)>j:
            im = medi
            jm = medj
        else:
            i = medi
            j = medj
    # print(im,i)
    # print(jm,j)
    if im-3<1: im=1
    if jm-3<1: jm=1
    rri=range(im,i+3)
    rrj=range(jm,j+3)
    return [[i, j] for i in rri
                for j in rrj
                if customfunction(i, j) == z]

print(findSolution(f1,5))