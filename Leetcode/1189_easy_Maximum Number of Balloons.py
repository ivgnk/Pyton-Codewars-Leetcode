'''
1189. Maximum Number of Balloons
https://leetcode.com/problems/maximum-number-of-balloons/description/

Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.
You can use each character in text at most once. Return the maximum number of instances that can be formed.

Example 1:
Input: text = "nlaebolko"
Output: 1

Example 2:
Input: text = "loonbalxballpoon"
Output: 2

Example 3:
Input: text = "leetcode"
Output: 0
'''

# Runtime 18 ms Beats 64.33% of users with Python
# Memory 11.69 MB Beats 96.99% of users with Python

from collections import Counter
def maxNumberOfBalloons(text):
    """
    :type text: str
    :rtype: int
    """
    tb="balloon"
    db=dict(Counter(tb))

    ddict=dict(Counter(text))

    res=[]
    for k in db.keys():
        if k in ddict:
            i = ddict[k]
            j = db[k]
            kk = i // j
            res.append(kk)
        else:
            return 0
    return min(res)

print(maxNumberOfBalloons("nlaebolko"))
# print(maxNumberOfBalloons("loonbalxballpoon"))
# print(maxNumberOfBalloons("leetcode"))