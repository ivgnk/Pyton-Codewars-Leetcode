"""
Done 05.06.2024. Topics: Array, Sorting
786. K-th Smallest Prime Fraction
https://leetcode.com/problems/k-th-smallest-prime-fraction/description/

You are given a sorted integer array arr containing 1 and prime numbers,
where all the integers of arr are unique. You are also given an integer k.
For every i and j where 0 <= i < j < arr.length, we consider the fraction arr[i] / arr[j].
Return the kth smallest fraction considered. Return your answer as an array of integers of size 2,
where answer[0] == arr[i] and answer[1] == arr[j].

Example 1:
Input: arr = [1,2,3,5], k = 3
Output: [2,5]
Explanation: The fractions to be considered in sorted order are:
1/5, 1/3, 2/5, 1/2, 3/5, and 2/3.
The third fraction is 2/5.

Example 2:
Input: arr = [1,7], k = 1
Output: [1,7]
"""
from itertools import combinations
from heapq import nsmallest, heappush, heappop

# Runtime 2197 ms Beats 15.12% of users with Python3
# Memory 99.75 MB Beats 27.21% of users with Python3
# Runtime 2057 ms Beats 18.29% of users with Python3
# Memory 100.22 MB Beats 24.08% of users with Python3
def kthSmallestPrimeFraction20(arr, k):
    heap = []; ll=len(arr)
    for i in range(ll) :
        for j in range(i+1, ll):
            heappush(heap, (arr[i]/arr[j], (arr[i], arr[j])))

    for i in range(k) :
        val, result = heappop(heap)

    return list(result)

# Runtime 1659 ms Beats 25.99% of users with Python3
# Memory 120.54 MB Beats 9.49% of users with Python3
# https://leetcode.com/problems/k-th-smallest-prime-fraction/solutions/5139295/one-line-solution/
def kthSmallestPrimeFraction(arr, k):
    return nsmallest(k, combinations(arr, 2), lambda q: q[0] / q[1])[-1]


# Runtime 981 ms Beats 45.13% of users with Python3
# Memory 72.64 MB Beats 45.48% of users with Python3
# Runtime 892 ms Beats 47.89% of users with Python3
# Memory 72.82 MB Beats 45.28% of users with Python3

def kthSmallestPrimeFraction3(arr, k: int):
    ll=len(arr)
    return sorted([(arr[i] / arr[j], arr[i], arr[j])
                   for i in range(ll)
                       for j in range(i + 1, ll)])[k - 1][1:]

# Runtime 1022 ms Beats 43.41% of users with Python3
# Memory 72.30 MB Beats 45.51% of users with Python3
# https://leetcode.com/problems/k-th-smallest-prime-fraction/description/comments/2391829
# https://leetcode.com/u/21f1002538/
def kthSmallestPrimeFraction0(arr, k: int):
    return sorted([(arr[i] / arr[j], arr[i], arr[j])
                   for i in range(len(arr))
                   for j in range(i + 1, len(arr))])[k - 1][1:]

# Runtime 2641 ms Beats 7.85% of users with Python3
# Memory 160.67 MB Beats 5.04% of users with Python3
def kthSmallestPrimeFraction1(arr, k):
    """
    :type arr: List[int]
    :type k: int
    :rtype: List[int]
    """
    ll = len(arr)
    mm = ll if k > ll else k
    nn = ll - (k + 1) if ll - (k + 1) >= 0 else 0
    res = [[arr[i] / arr[j], arr[i], arr[j]] for i in range(mm)
           for j in range(ll - 1, nn, -1)]
    res = sorted(res)
    print(len(res))
    return [res[k - 1][1], res[k - 1][2]]


print(kthSmallestPrimeFraction( [1,3,5,29,53,79,83,97], 24))

# Runtime 4564 ms Beats 5.01% of users with Python3
# Memory 160.72 MB Beats 5.04% of users with Python3
def kthSmallestPrimeFraction2(arr, k):
    """
    :type arr: List[int]
    :type k: int
    :rtype: List[int]
    """
    ll=len(arr); rl=range(ll)
    res=[[arr[i]/arr[j], arr[i], arr[j]] for i in rl
                                            for j in rl]
    res=sorted(res)
    print(res)
    return [res[k-1][1], res[k-1][2]]

