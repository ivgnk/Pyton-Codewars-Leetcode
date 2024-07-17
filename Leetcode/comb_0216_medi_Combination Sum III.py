"""
Done 17.07.2024. Topics: Array, Backtracking
216. Combination Sum III

Find all valid combinations of k numbers that sum up to n such that the following conditions are true:
Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain the same combination twice,
and the combinations may be returned in any order.

Example 1:
Input: k = 3, n = 7
Output: [[1,2,4]]
Explanation:
1 + 2 + 4 = 7
There are no other valid combinations.

Example 2:
Input: k = 3, n = 9
Output: [[1,2,6],[1,3,5],[2,3,4]]
Explanation:
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
There are no other valid combinations.

Example 3:
Input: k = 4, n = 1
Output: []
Explanation: There are no valid combinations.
Using 4 different numbers in the range [1,9], the smallest sum we can get is 1+2+3+4 = 10 and since 10 > 1, there are no valid combination.

Constraints:
2 <= k <= 9
1 <= n <= 60
"""

from itertools import permutations, combinations, combinations_with_replacement

# Runtime 12 ms Beats 82.90%
# Memory 11.66 MB Beats 27.94%
def combinationSum3(k, n):
    """
    :type k: int
    :type n: int
    :rtype: List[List[int]]
    """
    comb = combinations([1, 2, 3, 4, 5, 6, 7, 8, 9], k)
    return [list(c1) for c1 in comb if sum(c1) == n]


print(combinationSum3(k = 3, n = 7))
print(combinationSum3(k = 3, n = 9))
print(combinationSum3(k = 4, n = 1))