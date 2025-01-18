'''
18.01.2025. Topics: Greedy, Counting
1221. Split a String in Balanced Strings
https://leetcode.com/problems/split-a-string-in-balanced-strings/description/

Balanced strings are those that have an equal quantity of 'L' and 'R' characters.
Given a balanced string s, split it into some number of substrings such that:
Each substring is balanced.
Return the maximum number of balanced strings you can obtain.

Example 1:
Input: s = "RLRRLLRLRL"
Output: 4
Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.

Example 2:
Input: s = "RLRRRLLRLL"
Output: 2
Explanation: s can be split into "RL", "RRRLLRLL", each substring contains same number of 'L' and 'R'.
Note that s cannot be split into "RL", "RR", "RL", "LR", "LL", because the 2nd and 5th substrings are not balanced.

Example 3:
Input: s = "LLLLRRRR"
Output: 1
Explanation: s can be split into "LLLLRRRR".


Hint 1
Loop from left to right maintaining a balance variable
when it gets an L increase it by one otherwise decrease it by one.
Hint 2
Whenever the balance variable reaches zero then we increase the answer by one.
'''

from itertools import permutations

# Runtime 0 ms Beats 100.00%
# Memory 12.52 MB Beats 5.43%
# Time Complexity O(N)
# Space Complexity O(1)

# https://leetcode.com/problems/split-a-string-in-balanced-strings/solutions/6297766/simple-solution/
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        l = 0
        r = 0
        for i in s:
            if i == 'L':
                l += 1
            if i == 'R':
                l -= 1
            if l == 0:
                r += 1
        return r


def balancedStringSplit_main(s):
    """
    :type s: str
    :rtype: int
    """
    n = len(s); print('n=',n)
    ii=0
    for i in range(2,n-1):
        perm=list(set(list(permutations(s,i))))
        res=[]
        for j in perm:
            res.append(''.join(j))
        # print(i,res)
        delta=0; res2=[]
        for llst in res:
            if llst.count('L')==llst.count('R') and llst.count('R')>0 and llst in s:
                res2.append(llst)
                delta=delta+1
        ii=ii+delta
        print(ii,delta,res2)
    return ii

def balancedStringSplit(s):
    """
    :type s: str
    :rtype: int
    """

    """
    :type s: str
    :rtype: int
    """
    n = len(s);  # print('n=',n)
    ii = 0
    for i in range(2, n - 1):
        perm = list(set(list(permutations(s, i))))
        res = []
        for j in perm:
            res.append(''.join(j))
        # print(i,res)
        delta = 0;
        res2 = []
        for llst in res:
            if llst.count('L') == llst.count('R') and llst.count('R') > 0 and llst in s:
                res2.append(llst)
                delta = delta + 1
        ii = ii + delta
        # print(ii,delta,res2)
    return ii


print(balancedStringSplit("RLRRLLRLRL"))
