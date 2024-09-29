"""
Done 29.09.2024. Topics: String
3304. Find the K-th Character in String Game I
https://leetcode.com/problems/find-the-k-th-character-in-string-game-i/description/

Alice and Bob are playing a game.
Initially, Alice has a string word = "a".

You are given a positive integer k.
Now Bob will ask Alice to perform the following operation forever:

Generate a new string by changing each character in word to its next character in the English alphabet,
and append it to the original word.

For example, performing the operation on "c" generates "cd" and performing the operation on "zb" generates "zbac".

Return the value of the kth character in word, after enough operations have been done for word to have at least k characters.

Note that the character 'z' can be changed to 'a' in the operation.

Example 1:
Input: k = 5
Output: "b"
Explanation:
Initially, word = "a". We need to do the operation three times:
Generated string is "b", word becomes "ab".
Generated string is "bc", word becomes "abbc".
Generated string is "bccd", word becomes "abbcbccd".

Example 2:
Input: k = 10
Output: "c"

Constraints:
1 <= k <= 500

Hint 1
The constraints are small. Construct the string by simulating the operations.

Solution
✏️ Easy Python solution with a pre-prepared dictionary
# Intuition
Not use string, use list of symbols.
Prepare a dictionary for cyclic shift of letters.

# Approach
Use a while loop until the desired list length is reached.
Use the operator := to make the program short.
"""

# Runtime 34 ms Beats 100.00%
# Memory 16.40 MB Beats 100.00%
res=['a']
md={'a': 'b', 'b': 'c', 'c': 'd', 'd': 'e', 'e': 'f', 'f': 'g', 'g': 'h', 'h': 'i','i': 'j',
    'j': 'k', 'k': 'l', 'l': 'm', 'm': 'n', 'n': 'o', 'o': 'p', 'p': 'q', 'q': 'r', 'r': 's',
    's': 't', 't': 'u', 'u': 'v', 'v': 'w', 'w': 'x', 'x': 'y', 'y': 'z', 'z': 'a'}
def kthCharacter(k):
    """
    :type k: int
    :rtype: str
    """
    if k==1: return res[0]
    else:
        while (zz:=len(res))<k:
            for i in range(zz):
                res.append(md[res[i]])
    return res[k-1]

print(kthCharacter(5))