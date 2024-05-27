"""
Done 27.05.2024. Array, Two Pointers, String, Greedy
942. DI String Match
https://leetcode.com/problems/di-string-match/description/

A permutation perm of n + 1 integers of all the integers in the range [0, n] can be represented as a string s of length n where:
s[i] == 'I' if perm[i] < perm[i + 1], and
s[i] == 'D' if perm[i] > perm[i + 1].
Given a string s, reconstruct the permutation perm and return it.
If there are multiple valid permutations perm, return any of them.

Example 1:
Input: s = "IDID"
Output: [0,4,1,3,2]

Example 2:
Input: s = "III"
Output: [0,1,2,3]

Example 3:
Input: s = "DDI"
Output: [3,2,0,1]

as hint
по сути, вам просто нужно просто запустить D в сторону уменьшения длины (n) s и I в сторону увеличения (n).
То есть, если s="DDD", то вывод будет равен [3,2,1,0], где первые 3 массива обозначают длину s и
уменьшаются на 1 каждый раз, когда "D" появляется снова. если бы еще был I, предположим, что «DIIIDI»,
тогда D будет уменьшаться, а я буду увеличиваться на 1. вывод => [6,0,1,2,5,3,4].
Примечание: - D будет начинаться с длины s и будет уменьшаться на 1 всякий раз,
когда «D» появляется снова, и я начинаю с 0 и будет увеличиваться на 1 всякий раз,
когда «I» повторяется. в конце I и D будут в одной и той же позиции,
поэтому просто вставьте любой из них в массив в конце, и вы получите результат.
"""

# Runtime 39 ms Beats 51.97% of users with Python
# Memory 13.14 MB Beats 17.76% of users with Python
# Runtime 34 ms Beats 83.55% of users with Python
# Memory 13.22 MB Beats 9.87% of users with Python

def diStringMatch(s):
    """
    :type s: str
    :rtype: List[int]
    """
    ll=len(s)
    if 'I' not in s: # 'DD..'
        return [i for i in range(ll,-1,-1)]
    elif 'D' not in s: # 'II..'
        return [i for i in range(ll+1)]
    else:
        r = [-1] * (ll + 1)
        mmin=0; mmax=ll
        for i in range(ll):
            if s[i]=='I': r[i]=mmin; mmin=mmin+1
            else: r[i]=mmax; mmax=mmax-1
        r[ll]=min(mmin, mmax)
        return r

# print(diStringMatch("IDID"))
print(diStringMatch("III"))
print(diStringMatch("DDD"))