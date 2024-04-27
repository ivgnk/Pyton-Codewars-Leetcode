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
    tdict = [dict(Counter(w)) for w in words]
    ltdict = len(tdict)
    res = []
    for k, v in tdict[0].items():
        # lk=[k in tdict[i].keys() for i in range(1,ltdict)]
        lk = [k in t.keys() for t in tdict]
        if all(lk):
            lk2 = [t[k] for t in tdict]
            for j in range(min(lk2)):
                res.append(k)
    return res


print(commonChars(words = ["bella","label","roller"]))
# print('5' in ['25','23','105'])