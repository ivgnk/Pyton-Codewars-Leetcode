'''
Write a function that takes an array of strings as an argument and returns a sorted array
containing the same strings, ordered from shortest to longest.
'''
from copy import deepcopy

# best of codewars
# def sort_by_length(arr):
#   arr.sort(key = len) # key sorts them by parameter of choosing
#   return arr

def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k
def sort_by_length(arr):
     d_len = {}
     for i,s in enumerate(arr):
        d_len[i] = len(s)
     res = []
     k = list(d_len.values())
     k.sort()
     for i,dat in enumerate(k):
        j = get_key(d_len,dat)
        res.append(arr[j])
     return res

     # for i,s in enumerate(arr):
     #     res
     # print('keys')
     # for key in ddict.keys():
     #    print(key)
     # print('values')
     # for value in ddict.values():
     #    print(value)

print(sort_by_length(["beg", "life", "i", "to"]))