"""
Done 05.06.2024. Topics: Array, Binary Search, Greedy, Sortingm, Prefix Sum
2389. Longest Subsequence With Limited Sum
https://leetcode.com/problems/longest-subsequence-with-limited-sum/description/

You are given an integer array nums of length n, and an integer array queries of length m.
Return an array answer of length m where answer[i] is the maximum size of a subsequence
that you can take from nums such that the sum of its elements is less than or equal to queries[i].

A subsequence is an array that can be derived from another array by deleting some or no elements
without changing the order of the remaining elements.


Example 1:
Input: nums = [4,5,2,1], queries = [3,10,21]
Output: [2,3,4]
Explanation: We answer the queries as follows:
- The subsequence [2,1] has a sum less than or equal to 3. It can be proven that 2 is the maximum size of such a subsequence, so answer[0] = 2.
- The subsequence [4,5,1] has a sum less than or equal to 10. It can be proven that 3 is the maximum size of such a subsequence, so answer[1] = 3.
- The subsequence [4,5,2,1] has a sum less than or equal to 21. It can be proven that 4 is the maximum size of such a subsequence, so answer[2] = 4.

Example 2:
Input: nums = [2,3,4,5], queries = [1]
Output: [0]
Explanation: The empty subsequence is the only subsequence that has a sum less than or equal to 1, so answer[0] = 0.

Hint 1
Solve each query independently.
Hint 2
When solving a query, which elements of nums should you choose to make the subsequence as long as possible?
Hint 3
Choose the smallest elements in nums that add up to a sum less than the query.
"""

# Runtime 86 ms Beats 82.81% of users with Python3
# Memory 16.98 MB Beats 40.94% of users with Python3
import itertools
def answerQueries(nums, queries):
    n1=sorted(nums); ll=len(n1); rll = range(ll)
    ns=list(itertools.accumulate(n1))
    res = []
    for i in range(len(queries)):
        if ns[-1]<=queries[i]:
            res.append(ll)
            continue
        else:
            for j in rll:
                if ns[j]>queries[i]:
                    res.append(j)
                    break
    return res

print(answerQueries(nums = [4,5,2,1], queries = [3,10,21]))
print(answerQueries(nums = [2,3,4,5], queries = [1]))

# Runtime 156 ms Beats 51.89% of users with Python
# Memory 11.81 MB Beats 82.08% of users with Python
# Runtime 152 ms Beats 52.83% of users with Python
# Memory 11.85 MB Beats 82.08% of users with Python
def answerQueries2(nums, queries):
    """
    :type nums: List[int]
    :type queries: List[int]
    :rtype: List[int]
    """
    n1=sorted(nums); ll=len(n1)
    ns=[]; ssum=0
    for n in n1:
        ssum = ssum+n
        ns.append(ssum)
    res = []
    for i in range(len(queries)):
        if ns[-1]<=queries[i]:
            res.append(ll)
            continue
        else:
            for j in range(ll):
                if ns[j]>queries[i]:
                    res.append(j)
                    break
    return res

# Runtime 98 ms Beats 62.26% of users with Python
# Memory 11.98 MB Beats 54.72% of users with Python
def answerQueries3(nums, queries):
    """
    :type nums: List[int]
    :type queries: List[int]
    :rtype: List[int]
    """
    n1=sorted(nums); res=[]; ll=len(n1)
    alls=sum(n1)
    # print(n1)   print(queries)
    for i in range(len(queries)):
        if alls<=queries[i]:
            res.append(ll)
            continue
        ssum=n1[0]; j=0
        while ssum<=queries[i] and j<ll-1:
            j=j+1
            ssum=ssum+n1[j]
        # print(i,queries[i],n1[:j],j)
        res.append(len(n1[:j]))
    return res

