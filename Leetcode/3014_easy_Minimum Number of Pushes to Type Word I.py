"""
Done 13.07.2024. Topics: Math, String, Greedy
3014. Minimum Number of Pushes to Type Word I
https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-i/description/

You are given a string word containing distinct lowercase English letters.

Telephone keypads have keys mapped with distinct collections of lowercase English letters,
which can be used to form words by pushing them. For example, the key 2 is mapped with ["a","b","c"],
we need to push the key one time to type "a", two times to type "b", and three times to type "c" .

It is allowed to remap the keys numbered 2 to 9 to distinct collections of letters.
The keys can be remapped to any amount of letters, but each letter must be mapped to exactly one key.
You need to find the minimum number of times the keys will be pushed to type the string word.

Return the minimum number of pushes needed to type word after remapping the keys.

An example mapping of letters to keys on a telephone keypad is given below. Note that 1, *, #,
and 0 do not map to any letters.

Example 1:
Input: word = "abcde"
Output: 5
Explanation: The remapped keypad given in the image provides the minimum cost.
"a" -> one push on key 2
"b" -> one push on key 3
"c" -> one push on key 4
"d" -> one push on key 5
"e" -> one push on key 6
Total cost is 1 + 1 + 1 + 1 + 1 = 5.
It can be shown that no other mapping can provide a lower cost.

Example 2:
Input: word = "xycdefghij"
Output: 12
Explanation: The remapped keypad given in the image provides the minimum cost.
"x" -> one push on key 2
"y" -> two pushes on key 2
"c" -> one push on key 3
"d" -> two pushes on key 3
"e" -> one push on key 4
"f" -> one push on key 5
"g" -> one push on key 6
"h" -> one push on key 7
"i" -> one push on key 8
"j" -> one push on key 9
Total cost is 1 + 2 + 1 + 2 + 1 + 1 + 1 + 1 + 1 + 1 = 12.
It can be shown that no other mapping can provide a lower cost.

Constraints:
1 <= word.length <= 26
word consists of lowercase English letters.
All letters in word are distinct.

Hint 1
We have 8 keys in total. We can type 8 characters with one push each,
8 different characters with two pushes each, and so on.
Hint 2
The optimal way is to map letters to keys evenly.
"""

# Wrong Answer - 227 / 500 testcases passed
# Output = 36, Expected = 24
from icecream import ic
def minimumPushes2(word):
    """
    :type word: str
    :rtype: int
    """
    ll = len(word)
    if ll <= 8: return ll
    else:
        nn = ll//8
        no = ll%8
        sn = 8*(2+(nn-1))**nn//2
        return sn+no*(nn+1)


# Runtime 14 ms Beats 62.07%
# Memory 11.62 MB Beats 32.18%
# Runtime 10 ms Beats 86.21%
# Time Complexity O(1)
# Memory 11.63 MB Beats 32.18%
# Space Complexity O(1)
# https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-i/submissions/1319047009/

def minimumPushes(word):
    ll = len(word)
    if ll <= 8: return ll
    else:
        ssum=0
        for i in range(ll):
            if i <= 7: ssum=ssum+1
            elif i <= 15: ssum=ssum+2
            elif i <= 23: ssum=ssum+3
            else: ssum=ssum+4
        return ssum

# ic(minimumPushes("abcde"))
ic(minimumPushes("xycdefghij"))
ic(minimumPushes("abhrlngxyjkezwcm"))