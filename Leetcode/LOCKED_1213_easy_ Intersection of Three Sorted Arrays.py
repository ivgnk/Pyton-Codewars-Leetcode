"""
Done 05.10.2024. Topics: Hash Table, Sorting
1213. Intersection of Three Sorted Arrays
https://leetcode.com/problems/intersection-of-three-sorted-arrays/description/

The goal is to identify common integers that are present in three different sorted arrays
arr1, arr2, and arr3. These arrays are given to be sorted in strictly increasing order,
which means there are no duplicate elements within each array and
each subsequent element is greater than the previous one.
We need to find a list of integers that are present in all three arrays and
return this list in sorted order.
Since the arrays are already sorted,
the resulting list of common elements will also be automatically sorted.
https://algo.monster/liteproblems/1213
"""
def arrays_intersection(arr1, arr2, arr3):
    arr=arr1+arr2+arr3
    dd=dict()
    for a in arr:
        if a in dd:
            dd[a]+=1
        else:
            dd[a]=1
    return [k for k,v in dd.items() if v==3]

print(arrays_intersection(arr1 = [1,2,3], arr2 = [1,3,5], arr3 = [1,3,7]))

