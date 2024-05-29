"""
Done 29.05.2024. Topics: Math, Greedy
2139. Minimum Moves to Reach Target Score
https://leetcode.com/problems/minimum-moves-to-reach-target-score/description/

You are playing a game with integers. You start with the integer 1
and you want to reach the integer target.

In one move, you can either:
Increment the current integer by one (i.e., x = x + 1).
Double the current integer (i.e., x = 2 * x).
You can use the increment operation any number of times,
however, you can only use the double operation at most maxDoubles times.
Given the two integers target and maxDoubles, return the minimum number of moves needed to reach target starting with 1.

Example 1:
Input: target = 5, maxDoubles = 0
Output: 4
Explanation: Keep incrementing by 1 until you reach target.

Example 2:
Input: target = 19, maxDoubles = 2
Output: 7
Explanation: Initially, x = 1
Increment 3 times so x = 4
Double once so x = 8
Increment once so x = 9
Double again so x = 18
Increment once so x = 19

Example 3:
Input: target = 10, maxDoubles = 4
Output: 4
Explanation: Initially, x = 1
Increment once so x = 2
Double once so x = 4
Increment once so x = 5
Double again so x = 10

Hint 1
Solve the opposite problem: start at the given score and move to 1.
Hint 2
It is better to use the move of the second type once we can to lose more scores fast.
"""

# Runtime 8 ms Beats 89.36% of users with Python
# Memory 11.56 MB Beats 91.49% of users with Python

def minMoves(target, maxDoubles):
    """
    :type target: int
    :type maxDoubles: int
    :rtype: int
    """

    if maxDoubles==0: return target-1
    n=0
    while target !=1:
        if maxDoubles==0: return n+(target-1)
        if target%2 !=0:
            target=target-1; n=n+1
        elif maxDoubles !=0:
            maxDoubles=maxDoubles-1
            n = n + 1
            target = target//2
        else:
            target=target-1; n=n+1
    return n

print(minMoves(target = 5, maxDoubles = 0))
print(minMoves(target = 19, maxDoubles = 2))
print(minMoves(target = 10, maxDoubles = 4))

