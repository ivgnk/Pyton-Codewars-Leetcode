"""
18.11.2024. Topics: Hash Table, String, Sliding Window
2516. Take K of Each Character From Left and Right
https://leetcode.com/problems/take-k-of-each-character-from-left-and-right

You are given a string s consisting of the characters 'a', 'b', and 'c' and a non-negative integer k.
Each minute, you may take either the leftmost character of s, or the rightmost character of s.

Return the minimum number of minutes needed for you to take at least k of each character,
or return -1 if it is not possible to take k of each character.

Example 1:
Input: s = "aabaaaacaabc", k = 2
Output: 8
Explanation:
Take three characters from the left of s. You now have two 'a' characters, and one 'b' character.
Take five characters from the right of s. You now have four 'a' characters, two 'b' characters, and two 'c' characters.
A total of 3 + 5 = 8 minutes is needed.
It can be proven that 8 is the minimum number of minutes needed.

Example 2:
Input: s = "a", k = 1
Output: -1
Explanation: It is not possible to take one 'b' or 'c' so return -1.

Constraints:
1 <= s.length <= 105
s consists of only the letters 'a', 'b', and 'c'.
0 <= k <= s.length

Hint 1
Start by counting the frequency of each character and checking if it is possible.
Hint 2
If you take x characters from the left side, what is the minimum number of characters you need to take from the right side? Find this for all values of x in the range 0 ≤ x ≤ s.length.
Hint 3
Use a two-pointers approach to avoid computing the same information multiple times.
"""
from collections import defaultdict


# https://leetcode.com/problems/take-k-of-each-character-from-left-and-right/solutions/2947989/python-3-sliding-window/

class Solution1:
    def takeCharacters(self, s: str, k: int) -> int:
        ra = s.count('a') - k
        rb = s.count('b') - k
        rc = s.count('c') - k

        # if any of them is less than 0, it means there are less than k occurences of a character.
        if any(i < 0 for i in [ra, rb, rc]):   return -1
        hm = defaultdict(int)
        length = left = res = 0

        for right in s:
            hm[right] += 1
            length += 1

            while hm['a'] > ra or hm['b'] > rb or hm['c'] > rc:
                hm[s[left]] -= 1
                length -= 1
                left += 1

            res = max(res, length)

        return len(s) - res

# https://leetcode.com/problems/take-k-of-each-character-from-left-and-right/solutions/2948183/python-clean-12-line-sliding-window-solution-with-explanation/
class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        limits = {c: s.count(c) - k for c in 'abc'}
        if any(x < 0 for x in limits.values()):
            return -1

        cnts = {c: 0 for c in 'abc'}
        ans = l = 0
        for r, c in enumerate(s):
            cnts[c] += 1
            while cnts[c] > limits[c]:
                cnts[s[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)

        return len(s) - ans