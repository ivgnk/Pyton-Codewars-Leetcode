"""
01.01.2025. Topics: Backtracking, Dynamic Programming
22. Generate Parentheses
https://leetcode.com/problems/generate-parentheses/description/

Given n pairs of parentheses,
write a function to generate all combinations of well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]

Constraints:
1 <= n <= 8
"""
from typing import List


# https://leetcode.com/problems/generate-parentheses/solutions/6209783/intuitive-python-solution-by-misbaazeez-mmdv/
class Solution1:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        def backtrack(curr,openn,close):
            if (openn==n and close==n):
                output.append(curr)
                return
            if openn==close:
                curr += '('
                backtrack(curr,openn+1,close)
            elif openn==n:
                curr += ')'
                backtrack(curr,openn,close+1)
            else:
                curr += "("
                backtrack(curr,openn+1,close)
                curr = curr[:-1]
                curr += ')'
                backtrack(curr,openn,close+1)
        backtrack('',0,0)
        return output


# Runtime 0 ms Beats 100.00%
# Memory 12.78 MB Beats 11.28%
# https://leetcode.com/problems/generate-parentheses/solutions/6206529/python3solution-like-a-prodont-miss-this-2xxa/
class Solution2:
    def generateParenthesis(self, n: int) -> List[str]:
        def rec(left, right, s):
            if len(s) == n * 2:
                res.append(s)
                return
            if left < n:
                rec(left + 1, right, s + '(')
            if right < left:
                rec(left, right + 1, s + ')')

        res = []
        rec(0, 0, '')
        return res

