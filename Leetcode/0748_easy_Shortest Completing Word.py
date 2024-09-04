"""
Done 04.09.2024. Topics: Hash Table, String
748. Shortest Completing Word
https://leetcode.com/problems/shortest-completing-word/description/

Given a string licensePlate and an array of strings words,
find the shortest completing word in words.

A completing word is a word that contains all the letters in licensePlate.
Ignore numbers and spaces in licensePlate, and treat letters as case insensitive.
If a letter appears more than once in licensePlate,
then it must appear in the word the same number of times or more.

For example, if licensePlate = "aBc 12c", then it contains letters 'a', 'b' (ignoring case),
and 'c' twice. Possible completing words are "abccdef", "caaacab", and "cbca".

Return the shortest completing word in words. It is guaranteed an answer exists.
If there are multiple shortest completing words, return the first one that occurs in words.

Example 1:
Input: licensePlate = "1s3 PSt", words = ["step","steps","stripe","stepple"]
Output: "steps"
Explanation: licensePlate contains letters 's', 'p', 's' (ignoring case), and 't'.
"step" contains 't' and 'p', but only contains 1 's'.
"steps" contains 't', 'p', and both 's' characters.
"stripe" is missing an 's'.
"stepple" is missing an 's'.
Since "steps" is the only word containing all the letters, that is the answer.

Example 2:
Input: licensePlate = "1s3 456", words = ["looks","pest","stew","show"]
Output: "pest"
Explanation: licensePlate only contains the letter 's'. All the words contain 's', but among these "pest", "stew", and "show" are shortest. The answer is "pest" because it is the word that appears earliest of the 3.

Constraints:
1 <= licensePlate.length <= 7
licensePlate contains digits, letters (uppercase or lowercase), or space ' '.
1 <= words.length <= 1000
1 <= words[i].length <= 15
words[i] consists of lower case English letters.

Hint 1
Count only the letters (possibly converted to lowercase) of each word.
If a word is shorter and the count of each letter is at least
the count of that letter in the licensePlate, it is the best answer we've seen yet.

Считайте только буквы (возможно, переведенные в нижний регистр) каждого слова.
Если слово короче и количество каждой буквы не меньше количества
этой буквы на лицензионной табличке, это лучший ответ, который мы когда-либо видели.
"""

# Runtime 120 ms Beats 12.05%
# Memory 11.90 MB Beats 87.35%
from collections import Counter
def shortestCompletingWord(licensePlate, words):
    """
    :type licensePlate: str
    :type words: List[str]
    :rtype: str
    """
    # Преобразуем licensePlate в словарь
    dpl=dict()
    for s in licensePlate:
        if s.isalpha():
            s=s.lower()
            if s in dpl:
                dpl[s]+=1
            else:
                dpl[s] = 1
    n=1000; res=''; dpls=list(dpl)
    # Цикл по словам
    for w in words:
        dw=Counter(w)
        allsw=dict.fromkeys(dpls, False)  # Для контроля буквы в слове
        alls=True
        for k,v in dw.items():
            if k in allsw: allsw[k]=True
            if k in dpl: # Для контроля числа букв в слове
                 if dpl[k]>v:
                     alls = False
                     break
        alls2 = all([v for k,v in allsw.items()])
        if alls2: # Для контроля буквы в слове
            if alls: # Для контроля числа букв в слове
                lle=len(w)
                if lle<n:
                    n=lle
                    res=w
    return res

# print(shortestCompletingWord(licensePlate = "1s3 PSt", words = ["step","steps","stripe","stepple"]))
# print(shortestCompletingWord(licensePlate = "1s3 456", words = ["looks","pest","stew","show"]))
print(shortestCompletingWord(licensePlate = "Ah71752", words = ["suggest","letter","of","husband","easy","education","drug","prevent","writer","old"]))