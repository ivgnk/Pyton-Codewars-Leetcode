# stackoverflow.com/questions/3852780/python-intersection-of-multiple-lists
d = [[1,2,3,4], [2,3,4], [3,4,5,6,7]]
s = set.intersection(*map(set,d))
print(s,type(s))