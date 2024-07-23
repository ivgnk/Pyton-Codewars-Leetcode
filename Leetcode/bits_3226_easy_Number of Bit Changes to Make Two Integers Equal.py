"""
23.07.2024. Topics: Bit Manipulation
3226. Number of Bit Changes to Make Two Integers Equal
https://leetcode.com/problems/number-of-bit-changes-to-make-two-integers-equal/description/

You are given two positive integers n and k.
You can choose any bit in the binary representation of n that is equal to 1 and change it to 0.
Return the number of changes needed to make n equal to k.
If it is impossible, return -1.

Example 1:
Input: n = 13, k = 4

Output: 2
Explanation:
Initially, the binary representations of n and k are n = (1101)2 and k = (0100)2.
We can change the first and fourth bits of n. The resulting integer is n = (0100)2 = k.

Example 2:
Input: n = 21, k = 21
Output: 0
Explanation:
n and k are already equal, so no changes are needed.

Example 3:
Input: n = 14, k = 13
Output: -1
Explanation:
It is not possible to make n equal to k.

Constraints:
1 <= n, k <= 10**6

Hint 1
Find the binary representations of n and k.
Hint 2
Any bit that is equal to 1 in n and equal to 0 in k needs to be changed.
"""

# Runtime 8 ms Beats 93.29%
# Time Complexity O(N)
# Memory 11.68 MB Beats 41.69%
# Space Complexity O(1)

def minChanges(n, k):
    """
    :type n: int
    :type k: int
    :rtype: int
    """
    if n==k: return 0
    bn=list(bin(n)[2:])
    bk=list(bin(k)[2:])
    lk = len(bk)
    lb = len(bn)
    r=abs(lk-lb)
    if lk>lb:
        for i in range(r): bn.insert(0,'0')
    elif lk<lb:
        for i in range(r): bk.insert(0, '0')
    n=0
    for i in range(max(lk,lb)):
        if bn[i]=='1' and bk[i]=='0':
            bn[i] = '0'
            n=n+1
    if bn != bk: return -1
    return n

print(minChanges(13,4))
print(minChanges(13,14))