"""
Done 20.20.2024. Topics: Hash Table, String, Sliding Window
3305. Count of Substrings Containing Every Vowel and K Consonants I
https://leetcode.com/problems/count-of-substrings-containing-every-vowel-and-k-consonants-i

You are given a string word and a non-negative integer k.
Return the total number of substrings of word that contain every vowel
('a', 'e', 'i', 'o', and 'u') at least once and exactly k consonants.

Example 1:
Input: word = "aeioqq", k = 1
Output: 0
Explanation:
There is no substring with every vowel.

Example 2:
Input: word = "aeiou", k = 0
Output: 1
Explanation:
The only substring with every vowel and zero consonants is word[0..4], which is "aeiou".

Example 3:
Input: word = "ieaouqqieaouqq", k = 1
Output: 3
Explanation:
The substrings with every vowel and one consonant are:
word[0..5], which is "ieaouq".
word[6..11], which is "qieaou".
word[7..12], which is "ieaouq".

Constraints:
5 <= word.length <= 250
word consists only of lowercase English letters.
0 <= k <= word.length - 5

Hint 1
Use a HashMap and check all the substrings.
"""

from icecream import ic
vow=('a', 'e', 'i', 'o', 'u')
dd={s:0 for s in vow}

# Runtime 194 ms Beats 59.55% Analyze Complexity
# Memory 16.73 MB Beats 7.47%
def countOfSubstrings(word: str, k: int) -> int:
    # vowels = set("aeiou")
    count = 0
    for i in range(len(word)):
        vowel_set = set()
        consonants = 0
        for j in range(i, len(word)):
            if word[j] in vow:
                vowel_set.add(word[j])
            else:
                consonants += 1
            if len(vowel_set) == 5 and consonants == k:
                count += 1
            if consonants > k:
                break
    return count

ic(countOfSubstrings(word = "aeioqq", k = 1)) # 1
ic(countOfSubstrings(word = "aeiou", k = 0))
ic(countOfSubstrings(word = "ieaouqqieaouqq", k = 1))


# Runtime 3728 ms Beats 12.45%
# Memory 16.45 MB Beats 94.92%
def countOfSubstrings3(word, k):
    """
    :type word: str
    :type k: int
    :rtype: int
    """
    ll=len(word)
    lw=5+k; totn=0
    # ic(lw); ic(ll-lw)
    for i in range(ll-lw+1):
        # ic(i, i+lw+1)
        for j in range(i+lw,ll+1):
            wrk=True
            dd1 = dd.copy()
            cons = 0
            subs=word[i:j]
            # ic(i,j,subs)
            for d in subs:
                if d in vow: dd1[d]+=1
                else:
                    cons+=1
                    if cons>k:
                        wrk=False
                        break
            if wrk:
                if cons==k:
                    totn+=all([v>=1 for k,v in dd1.items()])
    return totn

# Runtime 4914 ms Beats 9.67%
# Memory 16.57 MB Beats 72.66%
def countOfSubstrings4(word, k):
    """
    :type word: str
    :type k: int
    :rtype: int
    """
    ll=len(word)
    lw=5+k; totn=0
    # ic(lw); ic(ll-lw)
    for i in range(ll-lw+1):
        # ic(i, i+lw+1)
        for j in range(i+lw,ll+1):
            dd1 = dd.copy()
            cons = 0
            subs=word[i:j]
            # ic(i,j,subs)
            for d in subs:
                if d in vow: dd1[d]+=1
                else: cons+=1
            totn+=cons==k and all([v>=1 for k,v in dd1.items()])
    return totn


def countOfSubstrings_(word, k):
    """
    :type word: str
    :type k: int
    :rtype: int
    """

    ll=len(word)
    lw=5+k; totn=0
    for i in range(ll-lw+1):
        dd1 = dd.copy()
        cons = 0
        subs=word[i:i+lw]
        for d in subs:
            if d in vow: dd1[d]+=1
            else: cons+=1
        totn+=cons==k and all([v>=1 for k,v in dd1.items()])
    return totn

