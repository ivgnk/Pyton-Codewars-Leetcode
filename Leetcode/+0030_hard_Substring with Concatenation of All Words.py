"""
29.10.2024. Topics: Hash Table, String, Sliding Window

30. Substring with Concatenation of All Words
You are given a string s and an array of strings words.
All the strings of words are of the same length.

A concatenated string is a string that exactly contains all the strings
of any permutation of words concatenated.

For example, if words = ["ab","cd","ef"],
then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are
all concatenated strings. "acdbef"
is not a concatenated string because it is not the concatenation of any permutation of words.
Return an array of the starting indices of all the concatenated substrings in s.
You can return the answer in any order.

Example 1:
Input: s = "barfoothefoobarman", words = ["foo","bar"]
Output: [0,9]
Explanation:
The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a permutation of words.
The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a permutation of words.

Example 2:
Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
Output: []
Explanation:
There is no concatenated substring.

Example 3:
Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
Output: [6,9,12]
Explanation:
The substring starting at 6 is "foobarthe". It is the concatenation of ["foo","bar","the"].
The substring starting at 9 is "barthefoo". It is the concatenation of ["bar","the","foo"].
The substring starting at 12 is "thefoobar". It is the concatenation of ["the","foo","bar"].

Constraints:
1 <= s.length <= 104
1 <= words.length <= 5000
1 <= words[i].length <= 30
s and words[i] consist of lowercase English letters.


"""
import time

from icecream import ic
from itertools import permutations

# Memory Limit Exceeded - 151 / 181 testcases passed
def findSubstring2(s, words):
    """
    :type s: str
    :type words: List[str]
    :rtype: List[int]
    """
    #------------- Letters control
    sa=set(s)
    sw={let for w in words for let in w}
    if not sw.issubset(sa): return []
    # ------------- Perm
    ll=len(s); rll=range(ll)

    lst=list(permutations(words))
    ic(lst)
    lst=list({''.join(prm) for prm in lst})
    ic(lst)
    res=[]

    sset = set()
    for ss in lst:
        if s.count(ss)>0:
            n=0
            while True:
                n=s.find(ss, n)
                if n > -1:
                    sset.add(n)
                    n=n+1
                else:
                    break
    res = res + list(sset)


    return list(set(res))

# Time Limit Exceeded - 152 / 182 testcases passed
import itertools
import sys
def findSubstring3(s, words):
    """
    :type s: str
    :type words: List[str]
    :rtype: List[int]
    """
    #------------- Letters control
    sa=set(s)
    sw={let for w in words for let in w}
    if not sw.issubset(sa): return []
    # ------------- Perm
    # ll=len(s); rll=range(ll)

    res=[]
    sset = set()
    for prm in permutations(words):
        ss=''.join(prm)
        if s.count(ss)>0:
            n=0
            while True:
                n=s.find(ss, n)
                if n > -1:
                    sset.add(n)
                    n=n+1
                else:
                    break
    res = res + list(sset)

    return list(set(res))

# Time Limit Exceeded - 152 / 182 testcases passed
def findSubstring4(s, words):
    """
    :type s: str
    :type words: List[str]
    :rtype: List[int]
    """
    #------------- Letters control
    sa=set(s)
    sw={let for w in words for let in w}
    if not sw.issubset(sa): return []
    # ------------- Perm
    sset = set()
    for prm in permutations(words):
        ss=''.join(prm)
        n = 0
        while True:
            n = s.find(ss, n)
            if n > -1:
                sset.add(n)
                n = n + 1
            else: break
    return list(sset)

take = lambda x, n: list(itertools.permutations(x, n))
def findSubstring5(s, words):
    """
    :type s: str
    :type words: List[str]
    :rtype: List[int]
    """
    #------------- Letters control
    sa=set(s)
    sw={let for w in words for let in w}
    if not sw.issubset(sa): return []
    # ------------- Perm
    sset = set()
    # Memory Limit Exceeded -  152 / 182 testcases passed
    for prm in take(words,len(words)):
        print(prm)
        ss=''.join(prm)
        n = 0
        while True:
            n = s.find(ss, n)
            if n > -1:
                sset.add(n)
                n = n + 1
            else: break
    return list(sset)

# Time Limit Exceeded - 152 / 182 testcases passed
def findSubstring6(s, words):
    """
    :type s: str
    :type words: List[str]
    :rtype: List[int]
    """
    #------------- Letters control
    sa=set(s)
    sw={let for w in words for let in w}
    if not sw.issubset(sa): return []
    # ------------- Perm
    ll=len(words)
    lstn=list(range(ll))
    sset = set()
    for prm in permutations(lstn):
        ss=''.join(words[i] for i in prm)
        n = 0
        while True:
            n = s.find(ss, n)
            if n > -1:
                sset.add(n)
                n = n + 1
            else: break
    return list(sset)

take = lambda x, n: list(itertools.permutations(x, n))
def findSubstring7(s, words):
    """
    :type s: str
    :type words: List[str]
    :rtype: List[int]
    """
    #------------- Letters control
    sa=set(s)
    sw={let for w in words for let in w}
    if not sw.issubset(sa): return []
    # ------------- Perm
    ll=len(words)
    lstn=list(range(ll))
    sset = set()
    for prm in take(lstn,ll):
        ss=''.join(words[i] for i in prm)
        n = 0
        while True:
            n = s.find(ss, n)
            if n > -1:
                sset.add(n)
                n = n + 1
            else: break
    return list(sset)

# Time Limit Exceeded - 152 / 182 testcases passed
from math import factorial
import random
def findSubstring8(s, words):
    """
    :type s: str
    :type words: List[str]
    :rtype: List[int]
    """
    #------------- Letters control
    sa=set(s)
    sw={let for w in words for let in w}
    if not sw.issubset(sa): return []
    # ------------- Perm
    ll=len(words)
    nn=factorial(ll)
    sset = set()
    set_res=set()
    lr=list(range(ll))
    while len(sset) < nn:
        temp = lr.copy()
        random.shuffle(temp)
        t = tuple(temp)
        if t not in sset:
            sset.add(t)  # `tuple` because `list`s are not hashable
            ss=''.join(words[i] for i in t)
            n = 0
            while True:
                n = s.find(ss, n)
                if n > -1:
                    set_res.add(n)
                    n = n + 1
                else: break
    return list(set_res)

# Runtime 5773 ms Beats 43.37%
# Memory 17.52 MB Beats 13.21%
# based on
# https://leetcode.com/problems/substring-with-concatenation-of-all-words/solutions/5954135/slicing-of-string-and-using-a-hashmap-to-get-the-word-0-length-check-in-the-sliced-string/
from collections import Counter
def findSubstring(s, words):
    #------------- Letters control
    # ------------- because words can be repeated
    sa=set(s)
    sw={let for w in words for let in w}
    if not sw.issubset(sa): return []
    # ------------- preparing
    res=[]
    ls=len(s)
    lw=len(words)
    lw0=len(words[0])
    newl=lw*lw0
    # ic(ls,newl)
    dd=dict()
    # словарь слов
    for w in words:
        if w in dd: dd[w]+=1
        else: dd[w]=1
    # ic(dd)
    for i in range(ls-newl+1):
        ss=s[i:i+newl]
        currd=dict()
        for j in range(0,newl,lw0):
            s1=ss[j:j+lw0]
            if s1 in currd: currd[s1]+=1
            else: currd[s1] = 1

        # ic(i,currd)
        if currd==dd: res.append(i)
    return res

ic(findSubstring( s = "barfoothefoobarman", words = ["foo","bar"]))
# ic(findSubstring(s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]))
# ic(findSubstring(s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]))
# ic(findSubstring(s = "abababab", words = ["a","b","a"]))
# ic(findSubstring(s = "mississippi", words = ["si","is"]))
# ic(findSubstring(s = "mississippi", words = ["si","is"]))
# s = "pjzkrkevzztxductzzxmxsvwjkxpvukmfjywwetvfnujhweiybwvvsrfequzkhossmootkmyxgjgfordrpapjuunmqnxxdrqrfgkrsjqbszgiqlcfnrpjlcwdrvbumtotzylshdvccdmsqoadfrpsvnwpizlwszrtyclhgilklydbmfhuywotjmktnwrfvizvnmfvvqfiokkdprznnnjycttprkxpuykhmpchiksyucbmtabiqkisgbhxngmhezrrqvayfsxauampdpxtafniiwfvdufhtwajrbkxtjzqjnfocdhekumttuqwovfjrgulhekcpjszyynadxhnttgmnxkduqmmyhzfnjhducesctufqbumxbamalqudeibljgbspeotkgvddcwgxidaiqcvgwykhbysjzlzfbupkqunuqtraxrlptivshhbihtsigtpipguhbhctcvubnhqipncyxfjebdnjyetnlnvmuxhzsdahkrscewabejifmxombiamxvauuitoltyymsarqcuuoezcbqpdaprxmsrickwpgwpsoplhugbikbkotzrtqkscekkgwjycfnvwfgdzogjzjvpcvixnsqsxacfwndzvrwrycwxrcismdhqapoojegggkocyrdtkzmiekhxoppctytvphjynrhtcvxcobxbcjjivtfjiwmduhzjokkbctweqtigwfhzorjlkpuuliaipbtfldinyetoybvugevwvhhhweejogrghllsouipabfafcxnhukcbtmxzshoyyufjhzadhrelweszbfgwpkzlwxkogyogutscvuhcllphshivnoteztpxsaoaacgxyaztuixhunrowzljqfqrahosheukhahhbiaxqzfmmwcjxountkevsvpbzjnilwpoermxrtlfroqoclexxisrdhvfsindffslyekrzwzqkpeocilatftymodgztjgybtyheqgcpwogdcjlnlesefgvimwbxcbzvaibspdjnrpqtyeilkcspknyylbwndvkffmzuriilxagyerjptbgeqgebiaqnvdubrtxibhvakcyotkfonmseszhczapxdlauexehhaireihxsplgdgmxfvaevrbadbwjbdrkfbbjjkgcztkcbwagtcnrtqryuqixtzhaakjlurnumzyovawrcjiwabuwretmdamfkxrgqgcdgbrdbnugzecbgyxxdqmisaqcyjkqrntxqmdrczxbebemcblftxplafnyoxqimkhcykwamvdsxjezkpgdpvopddptdfbprjustquhlazkjfluxrzopqdstulybnqvyknrchbphcarknnhhovweaqawdyxsqsqahkepluypwrzjegqtdoxfgzdkydeoxvrfhxusrujnmjzqrrlxglcmkiykldbiasnhrjbjekystzilrwkzhontwmehrfsrzfaqrbbxncphbzuuxeteshyrveamjsfiaharkcqxefghgceeixkdgkuboupxnwhnfigpkwnqdvzlydpidcljmflbccarbiegsmweklwngvygbqpescpeichmfidgsjmkvkofvkuehsmkkbocgejoiqcnafvuokelwuqsgkyoekaroptuvekfvmtxtqshcwsztkrzwrpabqrrhnlerxjojemcxel"
# words = ["dhvf","sind","ffsl","yekr","zwzq","kpeo","cila","tfty","modg","ztjg","ybty","heqg","cpwo","gdcj","lnle","sefg","vimw","bxcb"]
# ic(findSubstring(s,words))
# # for i in range(len(words)):
# #     print(i,s.count(words[i]))
# print(len(s))
# for i in range(2,len(words)):
#     print(i,s.count(words[i]+words[i-1]+words[i-2]))
#     print(i,s.count(words[i-2]+words[i-1]+words[i]))
# s = "fffffffffffffffffffffffffffffffff"
# words = ["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"]
# ic(findSubstring(s,words))
# ic(findSubstring( s = "barfoothefoobarman", words = ["foo","bar"]))
# ic(findSubstring( s = "foobarfoobar", words = ["foo","bar"]))
# ic(findSubstring(s = "aaa", words = ["a","a"]))

