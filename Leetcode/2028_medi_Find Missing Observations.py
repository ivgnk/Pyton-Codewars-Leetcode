"""
Done 05.09.2024. Topics: Array, Math
2028. Find Missing Observations
https://leetcode.com/problems/find-missing-observations/description/

You have observations of n + m 6-sided dice rolls with each face numbered from 1 to 6.
n of the observations went missing, and you only have the observations of m rolls.
Fortunately, you have also calculated the average value of the n + m rolls.

You are given an integer array rolls of length m where rolls[i] is the value of the ith observation.
You are also given the two integers mean and n.

Return an array of length n containing the missing observations
such that the average value of the n + m rolls is exactly mean.
If there are multiple valid answers, return any of them.
If no such array exists, return an empty array.

The average value of a set of k numbers is the sum of the numbers divided by k.

Note that mean is an integer, so the sum of the n + m rolls should be divisible by n + m.

Example 1:
Input: rolls = [3,2,4,3], mean = 4, n = 2
Output: [6,6]
Explanation: The mean of all n + m rolls is (3 + 2 + 4 + 3 + 6 + 6) / 6 = 4.

Example 2:
Input: rolls = [1,5,6], mean = 3, n = 4
Output: [2,3,2,2]
Explanation: The mean of all n + m rolls is (1 + 5 + 6 + 2 + 3 + 2 + 2) / 7 = 3.

Example 3:
Input: rolls = [1,2,3,4], mean = 6, n = 4
Output: []
Explanation: It is impossible for the mean to be 6 no matter what the 4 missing rolls are.

Constraints:
m == rolls.length
1 <= n, m <= 10**5
1 <= rolls[i], mean <= 6

Hint 1
What should the sum of the n rolls be?
Hint 2
Could you generate an array of size n such that each element is between 1 and 6?
"""

# Runtime 1007 ms Beats 39.57%
# Memory 27.27 MB Beats 42.78%
# Runtime 981 ms Beats 65.24%
# Memory 27.18 MB Beats 45.99%
from icecream import ic
from statistics import mean
def missingRolls(rolls, mean_all, n):
    """
    :type rolls: List[int]
    :type mean: int
    :type n: int
    :rtype: List[int]
    """
    # https://leetcode.com/problems/find-missing-observations/description/comments/2608714
    # Start by calculating the total sum needed for all n + m rolls to achieve the desired mean.
    # Then, subtract the sum of the observed m rolls to figure out the required sum for the missing n rolls.
    # What constraints must this required sum satisfy to ensure each missing roll is between 1 and 6?
    m=len(rolls)
    sum_all=(n+m)*mean_all
    sum_m=sum(rolls)
    sum_n=sum_all-sum_m
    mean_n=sum_n/n
    if mean_n>6: return []
    if mean_n<1: return []
    mean_n=int(mean_n)
    res=[mean_n for i in range(n)] # blank for the answer
    rem_all=sum_n-mean_n*n  #  Remainder for distribution
    i=0
    while rem_all>0:
        add=6-res[i]
        if add<=rem_all:
            res[i]+=add
        else:
            res[i] +=rem_all
        rem_all-=add
        i+=1
    return res




# ic(missingRolls(rolls = [3,2,4,3], mean_all = 4, n = 2))
ic(missingRolls( [1,5,6],  mean_all = 3, n = 4))
ic(missingRolls([1,2,3,4], 6, n = 4))
ic(missingRolls([4,2,2,5,4,5,4,5,3,3,6,1,2,4,2,1,6,5,4,2,3,4,2,3,3,5,4,1,4,4,5,3,6,1,5,2,3,3,6,1,6,4,1,3], mean_all = 2, n = 53))
