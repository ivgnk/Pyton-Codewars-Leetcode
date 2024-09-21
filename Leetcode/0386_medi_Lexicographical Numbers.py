"""
Done 21.09.2024. Topics: Depth-First Search, Trie
386. Lexicographical Numbers

Given an integer n, return all the numbers in the range [1, n] sorted in lexicographical order.
You must write an algorithm that runs in O(n) time and uses O(1) extra space.

Example 1:
Input: n = 13
Output: [1,10,11,12,13,2,3,4,5,6,7,8,9]

Example 2:
Input: n = 2
Output: [1,2]

Constraints:
1 <= n <= 5 * 10**4
"""

# Runtime 69 ms Beats 71.31%
# Memory 18.13 MB Beats 19.67%
# Time Complexity O(NLogN)
# Space Complexity O(N)
def lexicalOrder(n):
    """
    :type n: int
    :rtype: List[int]
    """
    lst=[i+1 for i in range(n)]
    return list(map(int,sorted(map(str,lst))))

# Runtime 71 ms Beats 70.49%
# Memory 18.01 MB Beats 36.89%
def lexicalOrder2(n):
    """
    :type n: int
    :rtype: List[int]
    """
    return list(map(int,sorted(map(str,[i+1 for i in range(n)]))))

print(lexicalOrder(13))

# Code DFS
class Solution:
    def lexicalOrder(self, n):
        res = []

        def fn(curr):
            if curr > n:
                return

            res.append(curr)

            for j in range(0, 10):
                if curr * 10 + j > n:
                    return
                else:
                    fn(curr * 10 + j)

        for i in range(1, 10):
            fn(i)

        return res

# https://leetcode.com/problems/lexicographical-numbers/solutions/5814261/python-trie-solution-sorting-solution-dfs/