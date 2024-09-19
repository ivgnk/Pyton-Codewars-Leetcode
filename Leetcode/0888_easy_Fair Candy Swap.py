"""
Done 19.09.2024. Topics: Hash Table, Binary Search
888. Fair Candy Swap
https://leetcode.com/problems/fair-candy-swap/description/

Alice and Bob have a different total number of candies. You are given two integer arrays aliceSizes and bobSizes
where aliceSizes[i] is the number of candies of the ith box of candy that Alice has and
bobSizes[j] is the number of candies of the jth box of candy that Bob has.

Since they are friends, they would like to exchange one candy box each so that after the exchange,
they both have the same total amount of candy.
The total amount of candy a person has is the sum of the number of candies in each box they have.

Return an integer array answer where answer[0] is the number of candies in the box that Alice must exchange, and answer[1]
is the number of candies in the box that Bob must exchange. If there are multiple answers, you may return any one of them.
It is guaranteed that at least one answer exists.

Example 1:
Input: aliceSizes = [1,1], bobSizes = [2,2]
Output: [1,2]

Example 2:
Input: aliceSizes = [1,2], bobSizes = [2,3]
Output: [1,2]

Example 3:
Input: aliceSizes = [2], bobSizes = [1,3]
Output: [2,3]

Constraints:
1 <= aliceSizes.length, bobSizes.length <= 10**4
1 <= aliceSizes[i], bobSizes[j] <= 10**5
Alice and Bob have a different total number of candies.
There will be at least one valid answer for the given input.
"""

# Runtime 1864 ms Beats 7.45%
# Memory 14.09 MB Beats 24.22%
def fairCandySwap(aliceSizes, bobSizes):
    diff = (sum(aliceSizes) - sum(bobSizes)) // 2
    a2 = sorted(aliceSizes)
    b2 = sorted(set(bobSizes))
    for aliceSize in a2:
        target = aliceSize - diff
        if target in b2:
            return [aliceSize, target]


# https://leetcode.com/problems/fair-candy-swap/solutions/5800490/solution-of-problem-no-888-fair-candy-swap/
# Runtime 574 ms Beats 33.54%
# Memory 13.61 MB Beats 52.17%
def fairCandySwap5(aliceSizes, bobSizes):
    diff = (sum(aliceSizes) - sum(bobSizes)) // 2
    bobSizesSet = set(bobSizes)
    for aliceSize in aliceSizes:
        target = aliceSize - diff
        if target in bobSizesSet:
            return [aliceSize, target]

# Runtime 6058 ms Beats 5.59%
# Memory 13.18 MB Beats 93.79%
def fairCandySwap4(aliceSizes, bobSizes):
    """
    :type aliceSizes: List[int]
    :type bobSizes: List[int]
    :rtype: List[int]
    """
    sa=sum(aliceSizes)
    sb=sum(bobSizes)
    d1 = sa - sb
    a2 = [-2*a for a in aliceSizes]
    b2 = [-2*b for b in bobSizes]

    for a in a2:
        d2=d1+a
        for b in b2:
            if d2==b:
                return [-a//2,-b//2]


# Time Limit Exceeded - 71 / 76 testcases passed
# len=len=5001
def fairCandySwap3(aliceSizes, bobSizes):
    """
    :type aliceSizes: List[int]
    :type bobSizes: List[int]
    :rtype: List[int]
    """
    sa=sum(aliceSizes)
    sb=sum(bobSizes)
    res=[]
    for a in aliceSizes:
        for b in bobSizes:
            d=a-b
            if sa-d==sb+d:
                return [a,b]
    return res


# Time Limit Exceeded - 70 / 76 testcases passed
def fairCandySwap2(aliceSizes, bobSizes):
    """
    :type aliceSizes: List[int]
    :type bobSizes: List[int]
    :rtype: List[int]
    """
    sa=sum(aliceSizes)
    sb=sum(bobSizes)
    res=[]
    for a in aliceSizes:
        for b in bobSizes:
            if sa-a+b==sb-b+a:
                return [a,b]
    return res
    sa-sb - 2*a + b == -b