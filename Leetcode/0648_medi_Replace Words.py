"""
Done 07.06.2024. Topics: Array, Hash Table, String, Trie
648. Replace Words
https://leetcode.com/problems/replace-words/description/?envType=daily-question&envId=2024-06-07

In English, we have a concept called root, which can be followed by some other word to form another longer word -
let's call this word derivative. For example, when the root "help" is followed by the word "ful",
we can form a derivative "helpful".

Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces,
replace all the derivatives in the sentence with the root forming it.
If a derivative can be replaced by more than one root,
replace it with the root that has the shortest length.

Return the sentence after the replacement.

Example 1:
Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"

Example 2:
Input: dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
Output: "a a b c"

!!!! Только слова начинающиеся с корня, в примере нет слов с приставками !!!!!!
"""

# https://leetcode.com/problems/replace-words/solutions/5272873/without-trie-python-100-efficient-beginner-s-approach-easy-to-understand/
# Runtime 303 ms Beats 36.80% of users with Python
# Memory 31.45 MB Beats 81.60% of users with Python

def replaceWords(self, dictionary, sentence):
    word_List = sentence.split(" ")  # Split sentence into words
    Sorted_dict = sorted(dictionary, key=len)  # Sort dictionary by string length

    for root in Sorted_dict:
        count = len(root)
        for i, word in enumerate(word_List):
            count1 = len(word)
            if count1 >= count:  # If word length >= root length
                if word[:count] == root:  # If word starts with root
                    word_List[i] = root  # Replace word with root

    return " ".join(word_List)  # Join updated word_List into a string


# https://leetcode.com/problems/replace-words/submissions/1280311279/
# Runtime 174 ms Beats 42.19% of users with Python3
# Memory 24.75 MB Beats 98.64% of users with Python3

def replaceWords(dictionary, sentence: str) -> str:
    break_sentence = sentence.split()

    n = len(break_sentence)

    for i in range(n):
        for j in dictionary:
            if break_sentence[i].startswith(j):
                break_sentence[i] = j
    output = ' '.join(break_sentence)
    return output


# Runtime 3454 ms Beats 5.60% of users with Python
# Memory 31.54 MB Beats 72.80% of users with Python
def replaceWords2(self, dic, sent):
    """
    :type dic: List[str]
    :type sent: str
    :rtype: str
    """
    lst=sent.split()
    for i in range(len(lst)):
        res=[[dic[j],lst[i].find(dic[j]) ] for j in range(len(dic)) if lst[i].find(dic[j]) ==0]
        ll=len(res)
        if ll !=0:
            if ll>1: res=sorted(res,key=lambda x: (x[1],x[0]))
            lst[i]=res[0][0]
    return ' '.join(lst)



# Wrong Answer -- 126 / 127 testcases passed
# dictionary = ["catt","cat","bat","rat"]
# sentence = "the cattle was rattled by the battery"
# Use Testcase
# Output     "the catt was rat by the bat"
# Expected   "the cat was rat by the bat"
def replaceWords2(dic, sent):
    """
    :type dic: List[str]
    :type sent: str
    :rtype: str
    """
    lst=sent.split()
    for i in range(len(lst)):
        res=[dic[j] for j in range(len(dic)) if lst[i].find(dic[j]) == 0]
        ll=len(res)
        if ll !=0:
            lst[i]=res[0]
    return ' '.join(lst)


# print(replaceWords(["cat","bat","rat"], "the cattle was rattled by the battery"))
print(replaceWords(["a", "aa", "aaa", "aaaa"],"a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"))
print(replaceWords2(["a", "aa", "aaa", "aaaa"],"a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"))
