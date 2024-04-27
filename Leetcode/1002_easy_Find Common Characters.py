"""
Done 28.04.2024
1002. Find Common Characters

Given a string array words, return an array of all characters that show up in all strings within the words
(including duplicates). You may return the answer in any order.

Example 1:
Input: words = ["bella","label","roller"]
Output: ["e","l","l"]

Example 2:
Input: words = ["cool","lock","cook"]
Output: ["c","o"]
"""

from collections import Counter
def commonChars(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    tdict=[]
    for w in words:
        dd=dict(Counter(w))
        tdict.append(dd)
    # print(tdict)
    ltdict=len(tdict)
    res = []
    for k, v in tdict[0].items():
        lk=[k in tdict[i].keys() for i in range(1,ltdict)]
        # print(k,lk)
        if all(lk):
            # print('  ',k,lk,'all')
            lk2 = [tdict[i][k] for i in range(ltdict)]
            # print('--',k,lk2)
            for j in range(min(lk2)):
                 res.append(k)
    return res

print(commonChars(words = ["bella","label","roller"]))
# print('5' in ['25','23','105'])