"""
Done 07.05.2024. Topics: String, Sorting
2785. Sort Vowels in a String
https://leetcode.com/problems/sort-vowels-in-a-string/description/

Given a 0-indexed string s, permute s to get a new string t such that:
All consonants remain in their original places. More formally,
if there is an index i with 0 <= i < s.length such that s[i] is a consonant, then t[i] = s[i].
The vowels must be sorted in the nondecreasing order of their ASCII values.
More formally, for pairs of indices i, j with 0 <= i < j < s.length such that s[i] and s[j] are vowels,
then t[i] must not have a higher ASCII value than t[j].
Return the resulting string.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in lowercase or uppercase.
Consonants comprise all letters that are not vowels.

Example 1:
Input: s = "lEetcOde"
Output: "lEOtcede"
Explanation: 'E', 'O', and 'e' are the vowels in s; 'l', 't', 'c', and 'd' are all consonants. The vowels are sorted according to their ASCII values, and the consonants remain in the same places.
Example 2:

Input: s = "lYmpH"
Output: "lYmpH"
Explanation: There are no vowels in s (all characters in s are consonants), so we return "lYmpH".
"""


vowels= ['A','E','I','O','U', 'a', 'e', 'i', 'o', 'u']

# Runtime 488 ms Beats 39.63% of users with Python
# Memory 14.75 MB Beats 90.00% of users with Python
def sortVowels2(s):
    """
    :type s: str
    :rtype: str
    """
    if len(s) > 1000:
        if all(s1 in vowels for s1 in s): return ''.join(sorted(s))

    vow = sorted([s1 for s1 in s if s1 in vowels])
    n=0; res=[]
    for s1 in s:
        if s1 in vow:
            res.append(vow[n])
            n = n + 1
        else:res.append(s1)
    return ''.join(res)

# Runtime 527 ms Beats 39.63% of users with Python
# Memory 15.11 MB Beats 79.63% of users with Python
# https://ru.stackoverflow.com/questions/1418582/Как-заменить-символ-в-строке-по-индексу
def sortVowel3(s):
    """
    :type s: str
    :rtype: str
    """
    ll=len(s)
    if ll > 1000:
        if all(s1 in vowels for s1 in s): return ''.join(sorted(s))

    vow = sorted([s1 for s1 in s if s1 in vowels])
    n=0
    for i in range(ll):
        if s[i] in vow:
            s=s[:i] + vow[n] + s[i+1:]
            n = n + 1
    return s

# Runtime 171 ms Beats 82.22% of users with Python
# Memory 15.75 MB Beats 70.00% of users with Python
# Runtime 163 ms Beats 84.81% of users with Python
# Memory 15.96 MB Beats 68.52% of users with Python
def sortVowel(s):
        ss = list(s)
        ll = len(s)
        if ll > 1000:
            if all(s1 in vowels for s1 in ss): return ''.join(sorted(s))
        ind = [i for i in range(ll) if ss[i] in vowels]
        vow = sorted([s1 for s1 in ss if s1 in vowels])
        n=0
        for i in ind:
            ss[i]=vow[n]
            n=n+1
        return ''.join(ss)

# print(sortVowels("lEetcOde"))
print(''.join(sorted("lEetcOde")))