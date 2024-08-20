'''
20.08.2024. Topics: Hash Table, String
1160. Find Words That Can Be Formed by Characters
https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/

You are given an array of strings words and a string chars.
A string is good if it can be formed by characters from chars (each character can only be used once).
Return the sum of lengths of all good strings in words.


Example 1:
Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.

Example 2:
Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation: The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.
'''

# Wrong Answer 10 / 36 testcases passed
# Super long words and a list

def countCharacters2(words, chars):
    """
    :type words: List[str]
    :type chars: str
    :rtype: int
    """
    ssum=0
    for s in words:
        Tr=True
        for s1 in s:
            if not s1 in chars:
                Tr = False
                break
        if Tr:
            ssum=ssum+len(s)
            print(s,len(s))
    return ssum

# print(countCharacters(words = ["cat","bt","hat","tree"], chars = "atach"))
# print(countCharacters( words = ["hello","world","leetcode"], chars = "welldonehoneyr"))

# Runtime 67 ms Beats 88.99%
# Memory 12.29 MB Beats 97.10%
# https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/solutions/5635479/python-easy/
def countCharacters(words, chars):
    res = 0
    for i in range(len(words)):
        count = 0
        for j in words[i]:
            if chars.count(j) >= words[i].count(j):
                count+=1
            else:
                break
        if count == len(words[i]):
            res+=len(words[i])
    return res

words2= ["dyiclysmffuhibgfvapygkorkqllqlvokosagyelotobicwcmebnpznjbirzrzsrtzjxhsfpiwyfhzyonmuabtlwin","ndqeyhhcquplmznwslewjzuyfgklssvkqxmqjpwhrshycmvrb","ulrrbpspyudncdlbkxkrqpivfftrggemkpyjl","boygirdlggnh","xmqohbyqwagkjzpyawsydmdaattthmuvjbzwpyopyafphx","nulvimegcsiwvhwuiyednoxpugfeimnnyeoczuzxgxbqjvegcxeqnjbwnbvowastqhojepisusvsidhqmszbrnynkyop","hiefuovybkpgzygprmndrkyspoiyapdwkxebgsmodhzpx","juldqdzeskpffaoqcyyxiqqowsalqumddcufhouhrskozhlmobiwzxnhdkidr","lnnvsdcrvzfmrvurucrzlfyigcycffpiuoo","oxgaskztzroxuntiwlfyufddl","tfspedteabxatkaypitjfkhkkigdwdkctqbczcugripkgcyfezpuklfqfcsccboarbfbjfrkxp","qnagrpfzlyrouolqquytwnwnsqnmuzphne","eeilfdaookieawrrbvtnqfzcricvhpiv","sisvsjzyrbdsjcwwygdnxcjhzhsxhpceqz","yhouqhjevqxtecomahbwoptzlkyvjexhzcbccusbjjdgcfzlkoqwiwue","hwxxighzvceaplsycajkhynkhzkwkouszwaiuzqcleyflqrxgjsvlegvupzqijbornbfwpefhxekgpuvgiyeudhncv","cpwcjwgbcquirnsazumgjjcltitmeyfaudbnbqhflvecjsupjmgwfbjo","teyygdmmyadppuopvqdodaczob","qaeowuwqsqffvibrtxnjnzvzuuonrkwpysyxvkijemmpdmtnqxwekbpfzs","qqxpxpmemkldghbmbyxpkwgkaykaerhmwwjonrhcsubchs"]
words = ['boygirdlggnh']
chars = "usdruypficfbpfbivlrhutcgvyjenlxzeovdyjtgvvfdjzcmikjraspdfp"

print(''.join(sorted(chars)))

# print(len(words)) # boygirl
print(countCharacters(words, chars))