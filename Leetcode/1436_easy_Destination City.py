'''
1436. Destination City
https://leetcode.com/problems/destination-city/description/

You are given the array paths, where paths[i] = [cityAi, cityBi] means
there exists a direct path going from cityAi to cityBi. Return the destination city,
that is, the city without any path outgoing to another city.
It is guaranteed that the graph of paths forms a line without any loop,
therefore, there will be exactly one destination city.


Example 1:
Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
Output: "Sao Paulo"
Explanation: Starting at "London" city you will reach "Sao Paulo" city which is the destination city.
Your trip consist of: "London" -> "New York" -> "Lima" -> "Sao Paulo".

Example 2:
Input: paths = [["B","C"],["D","B"],["C","A"]]
Output: "A"
Explanation: All possible trips are:
"D" -> "B" -> "C" -> "A".
"B" -> "C" -> "A".
"C" -> "A".
"A".
Clearly the destination city is "A".

Example 3:
Input: paths = [["A","Z"]]
Output: "Z"
'''

# Runtime 31 ms Beats 68.17% of users with Python
# Memory 11.68 MB Beats 93.37% of users with Python

from collections import Counter
def destCity(paths):
    """
    :type paths: List[List[str]]
    :rtype: str
    """
    # https://ru.stackoverflow.com/questions/1144555/Преобразовать-список-списков-в-один-список
    if len(paths)==1: return paths[0][1]
    p2=sum(paths, [])
    # print(p2)
    ddict=dict(Counter(p2))
    # print(ddict)
    for s in paths:
        if ddict[s[1]]==1: return s[1]


print(destCity([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]))
print(destCity([["B","C"],["D","B"],["C","A"]]))
# print(destCity([["A","Z"]]))
