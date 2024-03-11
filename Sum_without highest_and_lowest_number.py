'''
Sum all the numbers of a given array ( cq. list ),
except the highest and the lowest element ( by value, not by index! ).

The highest or lowest element respectively is a single element at each edge,
even if there are more than one with the same value.

Mind the input validation.
'''

def sum_array(arr):
    if arr is None: return 0;
    if arr ==[]: return 0;
    arr.sort(); llen = len(arr)
    ssum = 0
    for i in range(1,llen-1):
        ssum = ssum+arr[i]
    return ssum

# Best Codewars
# def sum_array(arr):
#     if arr == None or len(arr) < 3:
#         return 0
#     return sum(arr) - max(arr) - min(arr)

print(sum_array([6, 2, 1, 8, 10]))