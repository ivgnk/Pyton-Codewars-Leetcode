"""
12.04.2024. Topics: Array, Sorting
2406. Divide Intervals Into Minimum Number of Groups
https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/description/

You are given a 2D integer array intervals where intervals[i] = [lefti, righti]
represents the inclusive interval [lefti, righti].
You have to divide the intervals into one or more groups such that each interval is in exactly one group,
and no two intervals that are in the same group intersect each other.

Return the minimum number of groups you need to make.
Two intervals intersect if there is at least one common number between them.
For example, the intervals [1, 5] and [5, 8] intersect.

Example 1:
Input: intervals = [[5,10],[6,8],[1,5],[2,3],[1,10]]
Output: 3
Explanation: We can divide the intervals into the following groups:
- Group 1: [1, 5], [6, 8].
- Group 2: [2, 3], [5, 10].
- Group 3: [1, 10].
It can be proven that it is not possible to divide the intervals into fewer than 3 groups.

Example 2:
Input: intervals = [[1,3],[5,6],[8,10],[11,13]]
Output: 1
Explanation: None of the intervals overlap, so we can put all of them in one group.

Constraints:
1 <= intervals.length <= 105
intervals[i].length == 2
1 <= lefti <= righti <= 106

Hint 1
Can you find a different way to describe the question?
Hint 2
The minimum number of groups we need is equivalent to the maximum number of intervals
that overlap at some point. How can you find that?
"""

# Time Limit Exceeded - 21 / 35 testcases passed
def minGroups2(intervals):
    ma = -1;    mi = 3000
    print(len(intervals))
    for x1, x2 in intervals:
        mi = min(x1, mi)
        ma = max(x2, ma)
    dd = {i: 0 for i in range(mi, ma)}
    for x1, x2 in intervals:
        for i in range(x1, x2):
            dd[i] += 1
    return max([v for v in dd.values()])

# Time Limit Exceeded - 20 / 35 testcases passed
def minGroups3(intervals):
    dd=dict()
    for x1,x2 in intervals:
        for i in range(x1,x2+1):
            if i in dd:
                dd[i]+=1
            else:
                dd[i] = 1
    return max([v for v in dd.values()])

# Time Limit Exceeded - 14 / 35 testcases passed
def minGroups4(intervals):
    ll=len(intervals)
    if ll==1: return 1
    res = list(range(intervals[0][0],intervals[0][1]+1))
    for i in range(1,ll):
        res = res+list(range(intervals[i][0],intervals[i][1]+1))
    dd=dict()
    for i in res:
        if i in dd:
            dd[i]+=1
        else:
            dd[i] = 1
    return max([v for v in dd.values()])

def minGroups__(intervals):
    ll=len(intervals)
    dd=dict()
    dd[intervals[0][0]]=1
    dd[intervals[0][1]]=1
    for i in range(1,ll):
        if dd[intervals[i][0]] in dd: dd[intervals[0][0]] += 1
        else: dd[intervals[i][0]] = 1
        if dd[intervals[i][1]] in dd: dd[intervals[0][1]] += 1
        else: dd[intervals[i][1]] = 1



# Time Limit Exceeded - 22 / 35 testcases passed
def minGroups5(intervals):
    dat=[0]*1000000
    for x1, x2 in intervals:
        for i in range(x1,x2+1):
            dat[i] +=1
    return max(dat)

# Time Limit Exceeded - 15 / 35 testcases passed
from collections import Counter
def minGroups6(intervals):
    ll=len(intervals)
    res = list(range(intervals[0][0],intervals[0][1]+1))
    for i in range(1,ll):
        res = res+list(range(intervals[i][0],intervals[i][1]+1))
    dd=Counter(res)
    return max([v for v in dd.values()])

# https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/editorial/
# Runtime 1109 ms Beats 56.96%
# Memory 61.36 MB Beats 15.61%
from collections import defaultdict
def minGroups(intervals):
    ll=len(intervals)
    if ll==1: return 1
    dd=defaultdict(int)
    # print(dd)
    for d in intervals:
        dd[d[0]] += 1
        dd[d[1]+1] -= 1
    lst=sorted(dd)
    print(dd)
    print(lst)
    c_int = 0
    m_int = 0
    for dat in lst:
        c_int+=dd[dat]
        m_int=max(m_int, c_int)
    return m_int

print(minGroups( [[5,10],[6,8],[1,5],[2,3],[1,10]]))
# a=[1,2]+[2,3]
# print(a)
# dd=dict.fromkeys(a)
# print(dd)
# print(sum([1,2],[2,3]))

##################### C++
# class Solution {
# public:
#     int minGroups(vector<vector<int>>& intervals) {
#         if(intervals.size() == 1)
#             return 1;
#         int mx = INT_MIN;
#         for(auto interval : intervals){
#             mx = max(mx, interval[1]);
#         }
#         int visited[mx + 2];
#         memset(visited,0,sizeof(visited));
#
#         for(auto interval : intervals){
#             visited[interval[0]]++;
#             visited[interval[1] + 1]--;
#         }
#         int ans = INT_MIN;
#         int sum = 0;
#
#         for(auto num : visited){
#             sum += num;
#             ans = max(ans, sum);
#         }
#         return ans;
#     }
# };