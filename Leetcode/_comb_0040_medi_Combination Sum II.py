"""

Topics: Array, Backtracking
40. Combination Sum II
https://leetcode.com/problems/combination-sum-ii/description/

Given a collection of candidate numbers (candidates) and a target number (target),
find all unique combinations in candidates where the candidate numbers sum to target.
Each number in candidates may only be used once in the combination.
Note: The solution set must not contain duplicate combinations.

Example 1:
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

Example 2:
Input: candidates = [2,5,2,1,2], target = 5
Output:
[
[1,2,2],
[5]
]


Constraints:
1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30
"""

# https://leetcode.com/problems/combination-sum-ii/description/comments/1997800
# Memory Limit Exceeded - 23 / 176 testcases passed
# candidates = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], target = 27

from itertools import permutations, combinations
def combinationSum2_(candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    lc=len(candidates)
    if len(candidates) == 1:
        if candidates[0] == target: return [candidates]
    elif lc==2:
        if candidates[0]+candidates[1] == target: return [candidates]
    combs = []
    for i in range(1, lc):
        for c in combinations(candidates, i):
            combs.append(tuple(sorted(c)))
    ans = set()
    for c in combs:
        if sum(c) == target: ans.add(c)
    return sorted(ans)

# Time Limit Exceeded - 124 / 176 testcases passed
# candidates = [14,6,25,9,30,20,33,34,28,30,16,12,31,9,9,12,34,16,25,32,8,7,30,12,33,20,21,29,24,17,27,34,11,17,30,6,32,21,27,17,16,8,24,12,12,28,11,33,10,32,22,13,34,18,12]
# target = 27
def combinationSum2__(candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    lc=len(candidates)
    if len(candidates) == 1:
        if candidates[0] == target: return [candidates]
    elif lc==2:
        if candidates[0]+candidates[1] == target: return [candidates]
    combs = []
    for i in range(1, lc):
        for c in combinations(candidates, i):
            if sum(c) == target:
                combs.append(tuple(sorted(c)))
    ans = {c for c in combs}
    return sorted(ans)

# Time Limit Exceeded - 124 / 176 testcases passed
# candidates = [14,6,25,9,30,20,33,34,28,30,16,12,31,9,9,12,34,16,25,32,8,7,30,12,33,20,21,29,24,17,27,34,11,17,30,6,32,21,27,17,16,8,24,12,12,28,11,33,10,32,22,13,34,18,12]
# target = 27
from icecream import ic
def combinationSum2___(candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    candidates = sorted([i for i in candidates if i<=target])

    if sum(candidates) < target:  return []
    elif sum(candidates) == target: return [candidates]

    lc=len(candidates)
    # ic(lc)
    # ic(candidates)

    combs = set()
    for i in range(1, lc):
        ic(i, ' from ',lc )
        for c in combinations(candidates, i):
            if sum(c) == target:
                combs.add(tuple(sorted(c)))
    return sorted(combs)

# https://leetcode.com/problems/combination-sum-ii/solutions/5629473/x/
def combinationSum2(candidates,target):
    candidates.sort(reverse=True)
    candidates = [candidate for candidate in candidates if candidate <= target]

    partial_sums = set()

    for candidate in candidates:
        new_partial_sums = set()
        ic('1',candidate,new_partial_sums)
        for partial_sum, partial_tuple in partial_sums:
            ic(candidate, partial_sum, partial_tuple)
            if partial_sum + candidate <= target:
                new_partial_sums.add((
                    (partial_sum + candidate),
                    partial_tuple + (candidate,)
                ))
        ic('2',candidate,partial_sums)
        ic('    ')
        partial_sums.add((candidate, (candidate,)))
        partial_sums = partial_sums.union(new_partial_sums)

    result = set()

    for partial_sum, partial_tuple in partial_sums:
        if partial_sum == target:
            result.add(partial_tuple)

    return [list(x) for x in result]

# ic(combinationSum2(candidates = [1,2], target = 1))
ic(combinationSum2(candidates = [14,6,25,9,30,20,33,34,28,30,16,12,31,9,9,12,34,16,25,32,8,7,30,12,33,20,21,29,24,17,27,34,11,17,30,6,32,21,27,17,16,8,24,12,12,28,11,33,10,32,22,13,34,18,12],
                      target = 27))
# print(combinationSum2(candidates = [1,4,1,5,4,1], target = 3))
# print(combinationSum2(candidates = [10,1,2,7,6,1,5], target = 8)) # [(1, 1, 6), (1, 2, 5), (1, 7), (2, 6)]
# print(combinationSum2(candidates = [1], target = 1))
# print(combinationSum2(candidates = [1,1], target = 2))