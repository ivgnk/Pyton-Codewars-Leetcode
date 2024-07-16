"""
Done 16.07.2024. Topics: Array, Prefix Sum
3152. Special Array II
https://leetcode.com/problems/special-array-ii/description/

An array is considered special if every pair of its adjacent elements contains two numbers with different parity.
You are given an array of integer nums and a 2D integer matrix queries,
where for queries[i] = [fromi, toi] your task is to check that subarray  nums[fromi..toi] is special or not.

Return an array of booleans answer such that answer[i] is true if nums[fromi..toi] is special.

Example 1:
Input: nums = [3,4,1,2,6], queries = [[0,4]]
Output: [false]
Explanation:
The subarray is [3,4,1,2,6]. 2 and 6 are both even.

Example 2:
Input: nums = [4,3,1,6], queries = [[0,2],[2,3]]
Output: [false,true]
Explanation:
The subarray is [4,3,1]. 3 and 1 are both odd. So the answer to this query is false.
The subarray is [1,6]. There is only one pair: (1,6) and it contains numbers with different parity. So the answer to this query is true.

Constraints:
1 <= nums.length <= 105
1 <= nums[i] <= 105
1 <= queries.length <= 105
queries[i].length == 2
0 <= queries[i][0] <= queries[i][1] <= nums.length - 1

An array is considered special if every pair of its adjacent elements contains two numbers with different parity.

You are given an array of integer nums and a 2D integer matrix queries,
where for queries[i] = [fromi, toi] your task is to check that subarray  nums[fromi..toi] is special or not.

Return an array of booleans answer such that answer[i] is true if nums[fromi..toi] is special.

Example 1:
Input: nums = [3,4,1,2,6], queries = [[0,4]]
Output: [false]
Explanation:
The subarray is [3,4,1,2,6]. 2 and 6 are both even.

Example 2:
Input: nums = [4,3,1,6], queries = [[0,2],[2,3]]
Output: [false,true]
Explanation:
The subarray is [4,3,1]. 3 and 1 are both odd. So the answer to this query is false.
The subarray is [1,6]. There is only one pair: (1,6) and it contains numbers with different parity. So the answer to this query is true.

Constraints:
1 <= nums.length <= 10**5
1 <= nums[i] <= 10**5
1 <= queries.length <= 10**5
queries[i].length == 2
0 <= queries[i][0] <= queries[i][1] <= nums.length - 1

Hint 1
Try to split the array into some non-intersected continuous special subarrays.
Hint 2
For each query check that the first and the last elements of that query are in the same subarray or not.

My solution
https://leetcode.com/problems/special-array-ii/solutions/5484716/not-quite-simple-python-solution/
Intuition
Only part of what you need is written in the Нints.
The most important thing: how to store the resulting boundaries of special subarrays.
If stored in a list as sublists of separate boundaries, then comparison with an array of queries will lead to a
TLE error on the last tests. That is, the boundaries should be stored in a simple list.
Two storage options are possible: indexes that grow as the special subarray grows, or in the form of constant values
for each such array. In my approach, the second approach was chosen as it is more understandable.

Approach
Implement the search for boundaries as written in Intuition, and then iterate through the query array: if the values
in the previously obtained array at the boundary indices are not equal, then the subarray is not special.
"""

# Time Limit Exceeded - 523 / 536 testcases passed
# len(nums),len(queries) = 100000, 100000
def isArraySpecial2(nums, queries):
    """
    :type nums: List[int]
    :type queries: List[List[int]]
    :rtype: List[bool]
    """
    pa_ind=[n%2==00 for n in nums]
    res=[]
    for q in queries:
        ss=pa_ind[q[0]:q[1]+1]
        res.append(all([ss[i-1] != ss[i] for i in range(1,len(ss))]))
    return res

# Time Limit Exceeded - 523 / 536 testcases passed
def isArraySpecial3(nums, queries):
    """
    :type nums: List[int]
    :type queries: List[List[int]]
    :rtype: List[bool]
    """
    ll=len(nums)

    # lq = len(queries)
    # testq=[queries[i][0] == queries[i][1] for i in range(lq)]
    # if all(testq):
    #     return testq

    pa_ind=[n%2==00 for n in nums]
    res=[]
    prev, next = 0, 0
    for i in range(1,ll):
        if pa_ind[i] != pa_ind[i-1]:
            next=i
        else:
            res.append([prev,next])
            prev=i; next=i
    if prev != next: res.append([prev,next])
    res2=[]
    for q in queries:
        if q[0]==q[1]:
            res2.append(True)
        else:
            tr=False
            for ress in res:
                if ress[0]<=q[0] and q[1]<=ress[1]:
                    tr=True
                    break
            res2.append(tr)

    return res2

# https://leetcode.com/problems/special-array-ii/solutions/5177107/explained-convert-the-array-ii/
# Runtime 950 ms Beats 67.37%
# Memory 54.05 MB Beats 22.46%
# Runtime 938 ms Beats 82.93%
# Memory 53.80 MB Beats 94.01%
def isArraySpecial(nums, queries):
    ll=len(nums)
    pa_ind=[n%2==00 for n in nums]
    mn_ind=[0]*ll; j=0
    for i in range(1,ll):
        if pa_ind[i] != pa_ind[i-1]:
            mn_ind[i]=mn_ind[i-1]
        else:
            j=j+1
            mn_ind[i] = j

    res2=[]
    for q in queries:
        if q[0]==q[1]:
            res2.append(True)
        else: res2.append(mn_ind[q[0]]==mn_ind[q[1]])
    return res2

print(isArraySpecial(nums = [3,4,1,2,6], queries = [[0,4]]))
print(isArraySpecial( nums = [4,3,1,6], queries = [[0,2],[2,3]]))
print(isArraySpecial(nums = [7,5,1,8,1,1], queries = [[0,3],[0,1],[5,5]]))

