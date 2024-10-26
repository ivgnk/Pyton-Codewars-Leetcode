"""
26.10.2024. Topics: Array, Backtracking
39. Combination Sum
https://leetcode.com/problems/combination-sum/description/
Given an array of distinct integers candidates and a target integer target,
return a list of all unique combinations of candidates where the chosen numbers sum to target.
You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times.
Two combinations are unique if the frequency of at least one of the chosen numbers is different.
The test cases are generated such that the number of unique combinations that sum up to target is
less than 150 combinations for the given input.

Example 1:
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

Example 2:
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

Example 3:
Input: candidates = [2], target = 1
Output: []

Constraints:
1 <= candidates.length <= 30
2 <= candidates[i] <= 40
All elements of candidates are distinct.
1 <= target <= 40


"""


# Wrong Answer - 117 / 160 testcases passed
# Output
# [[34,6],[18,16,6],[18,18,2,2],[34,2,2,2],[2,16,16,6],[18,2,2,2,16],[16,6,6,6,6],[18,2,2,6,6,6],
# [2,2,2,2,16,16],[2,2,2,16,6,6,6],[18,2,2,2,2,2,6,6],[2,2,6,6,6,6,6,6],[2,2,2,2,2,2,16,6,6],
# [18,2,2,2,2,2,2,2,2,6],[2,2,2,2,2,6,6,6,6,6],[2,2,2,2,2,2,2,2,2,16,6],[18,2,2,2,2,2,2,2,2,2,2,2],
# [2,2,2,2,2,2,2,2,6,6,6,6],[2,2,2,2,2,2,2,2,2,2,2,2,16],[2,2,2,2,2,2,2,2,2,2,2,6,6,6]]
# Expected
# [[18,18,2,2],[18,2,2,2,2,2,2,2,2,2,2,2],[18,2,2,2,2,2,2,2,2,6],[18,2,2,2,2,2,6,6],[18,2,2,2,16],
# [18,2,2,6,6,6],[18,16,6],[34,2,2,2],[34,6],[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
# [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,6],[2,2,2,2,2,2,2,2,2,2,2,2,2,2,6,6],
# [2,2,2,2,2,2,2,2,2,2,2,2,16],[2,2,2,2,2,2,2,2,2,2,2,6,6,6],[2,2,2,2,2,2,2,2,2,16,6],
# [2,2,2,2,2,2,2,2,6,6,6,6],[2,2,2,2,2,2,16,6,6],[2,2,2,2,2,6,6,6,6,6],[2,2,2,2,16,16],
# [2,2,2,16,6,6,6],[2,2,6,6,6,6,6,6],[2,16,16,6],[16,6,6,6,6]]

# or i in range(1, len(candidates) + 9): = Memory Limit Exceeded

# Runtime # 15
# ms
# Beats
# 92.31%
# Analyze Complexity
# Memory
# 16.79
# MB
# Beats
# 23.50%
from itertools import combinations_with_replacement
class Solution2(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        for i in range(1, len(candidates) + 9):
            t = list(combinations_with_replacement(candidates, i))
            for s in t:
                if sum(s) == target:
                    res.append(list(s))
        return res


class Solution:
    def combinationSum(self, candidates, target):
        def check(candidates,result,stack,target,sum_val,i):
            if i==len(candidates):
                return
            if sum_val==target:
                result.append(stack)
                return
            elif sum_val>target:
                return
            else:
                check(candidates,result,stack+[candidates[i]],target,sum_val+candidates[i],i)
                check(candidates,result,stack,target,sum_val,i+1)
            return result


        result=[]
        stack=[]
        sum_val=0
        i=0
        return check(candidates,result,stack,target,sum_val,i)

# Accepted
# Runtime: 45ms
class Solution4:
    def combinationSum(self, candidates, target):
        results = [[] for _ in range(target + 1)]
        results[0] = [[]]

        for candidate in candidates:
            for num in range(candidate, target+1):
                for seq in results[num - candidate]:
                    # print(type(seq))
                    results[num].append(seq+[candidate])

        return results[target]

S=Solution4()
print(S.combinationSum(candidates = [2,3,6,7], target = 7))

# https://leetcode.com/problems/combination-sum/solutions/5536804/simple-dp-backtracking-memoization/
class Solution5:
    def combinationSum(self, candidates, target):
        dp = [[] for i in range(target+1)]
        dp[0].append(())
        for x in candidates:
            for i in range(x, target+1):
                dp[i].extend(_+(x,) for _ in dp[i-x])
        return dp[target]

# https://leetcode.com/problems/combination-sum/solutions/5891115/iterative-solution-with-diagrams-in-video-c-java-python-js/
class Solution6(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        dp = [[] for _ in range(target + 1)]
        dp[0].append([])

        for i in range(1, target + 1):
            for candidate in candidates:
                if candidate <= i:
                    for prev in dp[i - candidate]:
                        temp = prev + [candidate]
                        temp.sort()
                        if temp not in dp[i]:
                            dp[i].append(temp)
        return dp[target]

# https://leetcode.com/problems/combination-sum/solutions/5528686/dfs-solution-python-simple-34ms/
class Solution7(object):
    def combinationSum(self, candidates, target):
        res = []
        temp = []

        def dfs(i, sm):
            if sm > target:
                return
            elif sm == target:
                res.append(temp[:])
                return

            if i < len(candidates):
                temp.append(candidates[i])
                dfs(i, sm + candidates[i])
                temp.pop()
                dfs(i+1, sm)

        dfs(0, 0)
        return res

# https://leetcode.com/problems/combination-sum/solutions/4709609/beats-98-no-recursion-backtracking-only-iteration-easiest-beginner-solution/
class Solution7:
    def combinationSum(self, candidates, target):
        result = []
        stack = [(0, target, [])]

        while stack:
            current_index, current_target, current_combination = stack.pop()

            while current_index < len(candidates):
                current_candidate = candidates[current_index]

                if current_candidate == current_target:
                    result.append(current_combination + [current_candidate])
                elif current_candidate < current_target:
                    stack.append((current_index, current_target - current_candidate, current_combination + [current_candidate]))

                current_index += 1

        return result