'''
Done 02.10.2024. Topics: Array, Hash Table
1128. Number of Equivalent Domino Pairs
https://leetcode.com/problems/number-of-equivalent-domino-pairs/description/
Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d]
if and only if either (a == c and b == d), or (a == d and b == c) - that is, one domino can be rotated to be equal to another domino.
Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length,
and dominoes[i] is equivalent to dominoes[j].

Example 1:
Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
Output: 1

Example 2:
Input: dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]
Output: 3

Hint 1
For each domino j, find the number of dominoes you've already seen
(dominoes i with i < j) that are equivalent.
Hint 2
You can keep track of what you've seen using a hashmap.
'''

# Runtime 171 ms Beats 75.31%
# Memory 23.29 MB Beats 93.83%
# Runtime 170 ms Beats 80.25%
# Memory 23.39 MB Beats 91.36%
# Time Complexity O(N)
# Space Complexity O(N)
def numEquivDominoPairs(d):
    d = [tuple(sorted(d1)) for d1 in d]
    dd=dict()
    for d1 in d:
        if d1 in dd:
            dd[d1]+=1
        else:
            dd[d1] = 1
    return sum([v*(v-1)//2 for v in dd.values()])

print(numEquivDominoPairs([[1,2],[2,1],[3,4],[5,6]]))
# print(numEquivDominoPairs([[1, 2], [1, 2], [1, 1], [1, 2], [2, 2]]))

# Time Limit Exceeded -- 18 / 19 testcases passed
def numEquivDominoPairs2(d):
    """
    :type dominoes: List[List[int]]
    :rtype: int
    """
    nums = 0
    llen = len(d)
    for i in range(llen):
        for j in range(i+1,llen):
            if (d[i][0]==d[j][0] and d[i][1]==d[j][1]) or (d[i][1]==d[j][0] and d[i][0]==d[j][1]):
                nums=nums+1
    return nums
