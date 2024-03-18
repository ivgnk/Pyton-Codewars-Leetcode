'''
Count characters in your string
'''

# Best of Codewars
# from collections import Counter
#
# def count(string):
#     return Counter(string)

def count(s):
    if s=='': return {}
    ddict=dict.fromkeys(set(s),0)
    for s1 in s:
        ddict[s1]=ddict[s1]+1
    return ddict