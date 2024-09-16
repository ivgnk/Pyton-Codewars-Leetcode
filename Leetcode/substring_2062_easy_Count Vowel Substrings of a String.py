"""
Done 16.09.2024. Topics: Hash Table, String
2062. Count Vowel Substrings of a String
https://leetcode.com/problems/count-vowel-substrings-of-a-string/description/
A substring is a contiguous (non-empty) sequence of characters within a string.

A vowel substring is a substring that only consists of vowels ('a', 'e', 'i', 'o', and 'u') and has all five vowels present in it.

Given a string word, return the number of vowel substrings in word.



Example 1:

Input: word = "aeiouu"
Output: 2
Explanation: The vowel substrings of word are as follows (underlined):
- "aeiouu"
- "aeiouu"
Example 2:

Input: word = "unicornarihan"
Output: 0
Explanation: Not all 5 vowels are present, so there are no vowel substrings.
Example 3:

Input: word = "cuaieuouac"
Output: 7
Explanation: The vowel substrings of word are as follows (underlined):
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"

Constraints:
1 <= word.length <= 100
word consists of lowercase English letters only.

Hint 1
While generating substrings starting at any index, do you need to continue generating larger substrings if you encounter a consonant?
Hint 2
Can you store the count of characters to avoid generating substrings altogether?

Solution
✏️ Easy Pyhon solution based on dictionary
Intuition
Use dictionary

Approach
Do not use strings or other ways of accumulating characters
Even with nested arrays, the execution speed is good
"""
vow=['a', 'e', 'i', 'o', 'u']

from collections import Counter
def cntr(ww):
    dd=dict(Counter(ww))
    return len(dd)==5

# Runtime 1404 ms Beats 6.17%
# Memory 11.73 MB Beats 25.93%
def countVowelSubstrings2(word):
    """
    :type word: str
    :rtype: int
    """
    ll=len(word)
    w=list(word); n=0
    for i in range(ll):
        s1=w[i]
        if s1 in vow:
            for j in range(i+1,ll):
                if w[j] in vow:
                    s1+=w[j]
                    n += cntr(s1)
                else:
                    break
    return n

# Runtime 46 ms Beats 67.90%
# Memory 11.61 MB Beats 54.32%

def countVowelSubstrings(word):
    ll=len(word)
    w=list(word); n=0
    for i in range(ll):
        dd=dict()
        if w[i] in vow:
            dd[w[i]] = 1
            for j in range(i+1,ll):
                if w[j] in vow:
                    if w[j] in dd:
                        dd[w[j]] +=1
                    else:
                        dd[w[j]] = 1
                    n+=len(dd)>=5
                else:
                    break
    return n



print(countVowelSubstrings("aeiouu"))  # 2
print(countVowelSubstrings("unicornarihan")) # 0
print(countVowelSubstrings("cuaieuouac"))
# print(cntr(list("aeiouu")))