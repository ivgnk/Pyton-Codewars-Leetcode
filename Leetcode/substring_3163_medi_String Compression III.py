"""
05.07.2024. Topics: String
3163. String Compression III
https://leetcode.com/problems/string-compression-iii/description/

Given a string word, compress it using the following algorithm:

Begin with an empty string comp. While word is not empty, use the following operation:
Remove a maximum length prefix of word made of a single character c repeating at most 9 times.
Append the length of the prefix followed by c to comp.
Return the string comp.

Example 1:
Input: word = "abcde"
Output: "1a1b1c1d1e"
Explanation:
Initially, comp = "". Apply the operation 5 times, choosing "a", "b", "c", "d", and "e"
as the prefix in each operation.
For each prefix, append "1" followed by the character to comp.

Example 2:
Input: word = "aaaaaaaaaaaaaabb"
Output: "9a5a2b"
Explanation:
Initially, comp = "". Apply the operation 3 times, choosing "aaaaaaaaa", "aaaaa", and "bb" as the prefix in each operation.
For prefix "aaaaaaaaa", append "9" followed by "a" to comp.
For prefix "aaaaa", append "5" followed by "a" to comp.
For prefix "bb", append "2" followed by "b" to comp.

Constraints:
1 <= word.length <= 2 * 10**5
word consists only of lowercase English letters.

Hint 1
Each time, just cut the same character in prefix up to at max 9 times.
It’s always better to cut a bigger prefix.
"""

# Runtime 201 ms Beats 100.00%
# Memory 17.38 MB Beats 45.44%
def compressedString(word):
    """
    :type word: str
    :rtype: str
    """
    res = []
    # ll=len(word);
    prf = '';   n = 0
    for s in word:
        if prf == s:
            n = n + 1
            if n == 10:
                res.append('9')
                res.append(prf)
                n = 1
        else:
            if n != 0:
                res.append(str(n))
                res.append(prf)
            n = 1
            prf = s
    else:
        res.append(str(n))
        res.append(prf)
    return ''.join(res)

print(compressedString("abcde"))
print(compressedString("aaaaaaaaaaaaaabb"))


# Time Limit Exceeded - 738 / 744 testcases passed
def compressedString2(word):
    """
    :type word: str
    :rtype: str
    """
    res=''; ll=len(word); prf=word[0]; n=1
    for i in range(1,ll):
        if prf==word[i]:
            n=n+1
            if n==10:
                res=res+'9'+prf
                n=1
        else:
            res=res+str(n)+prf
            n=1
            prf=word[i]
    else: res=res+str(n)+prf
    return res

