"""
Done 16.08.2024. Topics: Array, Greedy

624. Maximum Distance in Arrays
https://leetcode.com/problems/maximum-distance-in-arrays/description/

You are given m arrays, where each array is sorted in ascending order.
You can pick up two integers from two different arrays (each array picks one) and calculate the distance.
We define the distance between two integers a and b to be their absolute difference |a - b|.
Return the maximum distance.

Example 1:
Input: arrays = [[1,2,3],[4,5],[1,2,3]]
Output: 4
Explanation: One way to reach the maximum distance 4 is to pick 1 in the first or third array and pick 5 in the second array.

Example 2:
Input: arrays = [[1],[1]]
Output: 0

Constraints:
m == arrays.length
2 <= m <= 105
1 <= arrays[i].length <= 500
-10**4 <= arrays[i][j] <= 10**4
arrays[i] is sorted in ascending order.
There will be at most 105 integers in all the arrays.

Solution
✏️ Easy Python solution

Intuition
Sequential accumulation of distances.
"""

# Runtime 1361 ms Beats 38.46%
# Memory 42.24 MB Beats 69.23%
# Runtime 1353 ms Beats 48.72%
# Memory 42.22 MB Beats 69.23%

# Time Complexity O(N)
# Space Complexity O(1)
def maxDistance(arrays):
    mmi=arrays[0][0]
    mma=arrays[0][-1]
    ll = len(arrays)
    lla=[len(arrays[i])-1 for i in range(ll)]
    dist = -1
    for i in range(1,ll):
        curmax = arrays[i][lla[i]]
        curmin = arrays[i][0]
        dist = max(dist, abs(mma - curmin))
        dist = max(dist, abs(mmi - curmax))

        mma = max(mma, curmax)
        mmi = min(mmi, curmin)
    return dist

print(maxDistance([[1,2,3],[4,5],[1,2,3]]))


# Wrong Answer - 121 / 136 testcases passed
# arrays = [[1,4],[0,5]]
def maxDistance2(arrays):
    """
    :type arrays: List[List[int]]
    :rtype: int
    """
    mmin=min([s[0] for s in arrays])
    mmax=max([s[-1] for s in arrays])
    return abs(mmax-mmin)


# Time Limit Exceeded - 128 / 136 testcases passed
def maxDistance3(arrays):
    """
    :type arrays: List[List[int]]
    :rtype: int
    """
    # https://leetcode.com/problems/maximum-distance-in-arrays/description/comments/2575971
    mi = [s[0] for s in arrays];    lmi = len(mi)
    ma = [s[-1] for s in arrays];   lma = len(ma)
    if ma == mi: return abs(max(ma) - min(mi))
    dist = -1
    for i in range(lma):
        for j in range(lmi):
            if i != j:
                z = abs(ma[i] - mi[j])
                if z > dist: dist = z
    return dist

# Time Limit Exceeded - 124 / 136 testcases passed
def maxDistance4(arrays):
    """
    :type arrays: List[List[int]]
    :rtype: int
    """
    mi = [s[0] for s in arrays]
    ma = [s[-1] for s in arrays]
    if ma == mi: return abs(max(ma) - min(mi))

    ll=len(arrays); rll=range(ll)
    mi=list({(mi[i],i) for i in rll})
    ma=list({(ma[i],i) for i in rll})

    dist=-1
    for a in ma:
        for i in mi:
            if a[1] != i[1]:
                z=abs(a[0]-i[0])
                if z>dist: dist=z
    return dist

