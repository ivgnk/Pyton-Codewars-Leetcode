"""
Done 06.12.2024. Topics: Sorting
274. H-Index
https://leetcode.com/problems/h-index/

Given an array of integers citations where citations[i] is the number of citations
a researcher received for their ith paper, return the researcher's h-index.

According to the definition of h-index on Wikipedia:
The h-index is defined as the maximum value of h such that the given researcher has published at
least h papers that have each been cited at least h times.

Example 1:
Input: citations = [3,0,6,1,5]
Output: 3
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.

Example 2:
Input: citations = [1,3,1]
Output: 1

Constraints:
n == citations.length
1 <= n <= 5000
0 <= citations[i] <= 1000

Hint 1
An easy approach is to sort the array first.
Hint 2
What are the possible values of h-index?
Hint 3
A faster approach is to use extra space.

Tip https://leetcode.com/problems/h-index/description/comments/2282689

sort the list.
reverse it. Initialize "res = 0"
loop over list with following condition
if i+1 <= ans[i]: # reason for i+1 is mentioned below
res = i+1
return res.
Note-> here we are saying i+1 because no. we cannot no. of paper from 1. if we do code will change a bit. you can give it a try.

My solution https://leetcode.com/problems/h-index/solutions/6118880/fast-0-ms-and-easy-python-solution-for-problem-0274-based-on-tip/
Fast (0 ms) and easy Python solution for Problem 0274, based on tip
"""

# Runtime 0 ms Beats 100.00%
# Memory 12.61 MB Beats 6.20%
# Time Complexity O(NLogN)
# Space Complexity O(N)
def hIndex2(citations):
    """
    :type citations: List[int]
    :rtype: int
    """
    c=sorted(citations,reverse=True)
    res=0
    for i in range(len(citations)):
        res+=c[i]>=i+1
    return res

def hIndex(citations):
    c=sorted(citations,reverse=True)
    return sum([c[i]>=i+1 for i in range(len(citations)) ])
print(hIndex([3,0,6,1,5]))
print(hIndex([1,3,1]))

