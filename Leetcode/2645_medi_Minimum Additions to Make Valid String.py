"""
Done 19.07.2024. String
2645. Minimum Additions to Make Valid String
https://leetcode.com/problems/minimum-additions-to-make-valid-string/

Given a string word to which you can insert letters "a", "b" or "c"
anywhere and any number of times, return the minimum number of letters that must be inserted so that word becomes valid.
A string is called valid if it can be formed by concatenating the string "abc" several times.

Example 1:
Input: word = "b"
Output: 2
Explanation: Insert the letter "a" right before "b", and the letter "c" right next to "b" to obtain the valid string "abc".

Example 2:
Input: word = "aaa"
Output: 6
Explanation: Insert letters "b" and "c" next to each "a" to obtain the valid string "abcabcabc".

Example 3:
Input: word = "abc"
Output: 0
Explanation: word is already valid. No modifications are needed.

Constraints:
1 <= word.length <= 50
word consists of letters "a", "b" and "c" only.

Hint 1
Maintain a pointer on word and another pointer on string “abc”.
Hint 2
If the two characters that are being pointed to differ,
Increment the answer and the pointer to the string “abc” by one.
"""

from icecream import ic

# Wrong Answer -- 346 / 1523 testcases passed
from collections import Counter
def addMinimum2(word):
    """
    :type word: str
    :rtype: int
    """
    dd=dict(Counter(word))
    lst = [[v,k] for k,v in dd.items()]
    print(lst)
    if len(lst)==3:
        if lst[0][0]==lst[1][0]==lst[2][0]: return 0
    mmain=[0,0,0]
    if 'a' in dd: mmain[0] = dd['a']
    if 'b' in dd: mmain[1] = dd['b']
    if 'c' in dd: mmain[2] = dd['c']
    m = max(mmain)
    return (m-mmain[0])+(m-mmain[1])+(m-mmain[2])

# Runtime 34 ms Beats 85.91%
# Memory 16.47 MB Beats 76.36%
def addMinimum(word):
    res=0; i=0; sav=''
    while i<len(word):
        if word[i] == 'a':
            if sav=='': sav +=word[i]
            else:
                res += 3-len(sav)
                sav=word[i]
        if word[i] == 'b':
            if sav == '': sav = word[i] # не знаем что дальше
            elif sav == 'a': sav +=word[i] # просто продолжаем
            elif sav == 'b': res += 2      # вычисление
            elif sav == 'ab': res += 1; sav = word[i]      # вычисление
        if word[i] == 'c':
            if sav=='': res += 2
            elif sav=='a': res += 1
            elif sav=='b': res += 1
            sav = ''
        # print(i, word[i], sav, res)
        i += 1
    if sav !='': res += 3 - len(sav)
    return res



# print(addMinimum("b")) # 2
# print(addMinimum("aaa")) # 6
# print(addMinimum("abc")) # 0
# print(addMinimum("aaaaac")) # 9
# print(addMinimum("aaaabb")) # 9
ic(addMinimum("aaaacc")) # 9
