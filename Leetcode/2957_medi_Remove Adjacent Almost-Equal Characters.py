"""
Done 07.10.2024. Topics: String
2957. Remove Adjacent Almost-Equal Characters
https://leetcode.com/problems/remove-adjacent-almost-equal-characters/

You are given a 0-indexed string word.
In one operation, you can pick any index i of word and change word[i] to any lowercase English letter.
Return the minimum number of operations needed to remove all adjacent almost-equal characters from word.
Two characters a and b are almost-equal if a == b or a and b are adjacent in the alphabet.

Example 1:
Input: word = "aaaaa"
Output: 2
Explanation: We can change word into "acaca" which does not have any adjacent almost-equal characters.
It can be shown that the minimum number of operations needed to remove all adjacent almost-equal characters from word is 2.

Example 2:
Input: word = "abddez"
Output: 2
Explanation: We can change word into "ybdoez" which does not have any adjacent almost-equal characters.
It can be shown that the minimum number of operations needed to remove all adjacent almost-equal characters
from word is 2.

Example 3:
Input: word = "zyxyxyz"
Output: 3
Explanation: We can change word into "zaxaxaz" which does not have any adjacent almost-equal characters.
It can be shown that the minimum number of operations needed to remove all adjacent almost-equal characters from word is 3.

Constraints:
1 <= word.length <= 100
word consists only of lowercase English letters.

For i > 0, if word[i] and word[i - 1] are adjacent, we will change word[i] to another character.
Which character should we change it to?
Hint 2
We will change word[i] to some character that is not adjacent to word[i - 1] nor word[i + 1] (if it exists).
Such a character always exists. However, since the problem does not ask for the final state of the string,
It is enough to prove that the character exists and we do not need to find it.

My solution
Python solution with functions map(), ord(), abs() and Arbitrary replacement of letters
https://leetcode.com/problems/remove-adjacent-almost-equal-characters/solutions/5883114/python-solution-with-functions-map-ord-abs-and-arbitrary-replacement-of-letters/

Intuition
To speed up, we will immediately replace the letter with its code.

Approach
We compare the letter codes and, if necessary, change the letter to one that is guaranteed to go beyond (taking into account the cyclicity)
"""

# Runtime 8 ms Beats 96.97%
# Memory 11.51 MB Beats 84.85%
def removeAlmostEqualCharacters(word):
    """
    :type word: str
    :rtype: int
    """
    w=list(map(ord,word))
    n=0
    for i in range(1,len(w)):
        if abs(w[i]-w[i-1])<=1:
            n+=1
            w[i]=w[i]+28
    return n
print(removeAlmostEqualCharacters("aaaaa"))
print(removeAlmostEqualCharacters("abddez"))