"""
Done 16.07.2024. Topics: String, Greedy
3216. Lexicographically Smallest String After a Swap
https://leetcode.com/problems/lexicographically-smallest-string-after-a-swap/description/

Given a string s containing only digits, return the lexicographically smallest string
that can be obtained after swapping adjacent digits in s with the same parity at most once.

Digits have the same parity if both are odd or both are even.
For example, 5 and 9, as well as 2 and 4, have the same parity, while 6 and 9 do not.

Example 1:
Input: s = "45320"
Output: "43520"
Explanation:
s[1] == '5' and s[2] == '3' both have the same parity, and swapping them results in the lexicographically smallest string.

Example 2:
Input: s = "001"
Output: "001"
Explanation:
There is no need to perform a swap because s is already the lexicographically smallest.

Constraints:
2 <= s.length <= 100
s consists only of digits.

Hint 1
Try all possible swaps satisfying the constraints and find the one that results in the lexicographically smallest string.

TIP:
Remember we can only make ONE swap.
It is important to also notice, the first swap is all you need.
You do not need to collect all swaps and do a sort(my original naive solution).
This is due to the earlier index having a large impact than the later indexes.
For example: "531", our two swaps are "513", "351" where "351 "
is obviously lexicographically smaller.
Traverse s keeping track of the prev element, check parity,
and if possible swap and return the s after making the swap. O(n)
https://leetcode.com/problems/lexicographically-smallest-string-after-a-swap/description/comments/2515877
"""

# Runtime 13 ms Beats 85.79%
# Time Complexity O(N)
# Memory 11.74 MB Beats 24.66%
# Space Complexity O(N)

def getSmallestString(self, s):
    """
    :type s: str
    :rtype: str
    """
    ss = [s1 for s1 in s]
    for i in range(1, len(s)):
        if (int(ss[i - 1]) % 2 == 0) == (int(ss[i]) % 2 == 0):
            if ss[i - 1] > ss[i]:
                ss[i - 1], ss[i] = ss[i], ss[i - 1]
                break
    return ''.join(ss)


# Runtime 15 ms Beats 79.62%
# Memory 11.68 MB Beats 61.66%
def getSmallestString2(self, s):
    """
    :type s: str
    :rtype: str
    """
    ii = [int(s1) for s1 in s]
    # bb=[i1%2==0 for i1 in ii]
    for i in range(1, len(s)):
        if (ii[i - 1] % 2 == 0) == (ii[i] % 2 == 0):
            if ii[i - 1] > ii[i]:
                ii[i - 1], ii[i] = ii[i], ii[i - 1]
                break
    return ''.join([str(i1) for i1 in ii])

# Runtime 20 ms Beats 48.26%
# Memory 11.77 MB Beats 24.66%
def getSmallestString3(s):
    """
    :type s: str
    :rtype: str
    """
    ii=[int(s1) for s1 in s]
    bb=[i1%2==0 for i1 in ii]
    for i in range(1,len(s)):
        if bb[i-1]==bb[i]:
            if ii[i-1]>ii[i]:
                ii[i - 1], ii[i] = ii[i], ii[i-1]
                break
    return ''.join([str(i1) for i1 in ii])

print(getSmallestString("45320"))
print(getSmallestString("001"))


