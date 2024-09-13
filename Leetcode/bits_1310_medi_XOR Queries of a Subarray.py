"""
13.09.2024. Topics: Bit Manipulation, Prefix Sum
1310. XOR Queries of a Subarray
https://leetcode.com/problems/xor-queries-of-a-subarray/description

You are given an array arr of positive integers.
You are also given the array queries where queries[i] = [lefti, righti].
For each query i compute the XOR of elements from lefti to righti
(that is, arr[lefti] XOR arr[lefti + 1] XOR ... XOR arr[righti] ).
Return an array answer where answer[i] is the answer to the ith query.

Example 1:
Input: arr = [1,3,4,8], queries = [[0,1],[1,2],[0,3],[3,3]]
Output: [2,7,14,8]
Explanation:
The binary representation of the elements in the array are:
1 = 0001
3 = 0011
4 = 0100
8 = 1000
The XOR values for queries are:
[0,1] = 1 xor 3 = 2
[1,2] = 3 xor 4 = 7
[0,3] = 1 xor 3 xor 4 xor 8 = 14
[3,3] = 8

Example 2:
Input: arr = [4,8,2,10], queries = [[2,3],[1,3],[0,0],[0,3]]
Output: [8,0,4,4]

Constraints:
1 <= arr.length, queries.length <= 3 * 104
1 <= arr[i] <= 109
queries[i].length == 2
0 <= lefti <= righti < arr.length

Hint 1
What is the result of x ^ y ^ x ?
Hint 2
Compute the prefix sum for XOR.

Hint 3
Process the queries with the prefix sum values.

A ^ A = 0 (any number XORed with itself is 0)
A ^ 0 = A (XORing with 0 leaves the number unchanged)
A ^ B = B ^ A (order doesn’t matter)
(A ^ B) ^ C = A ^ (B ^ C) (grouping doesn’t matter)
(A ^ B) ^ B = A (XORing twice cancels out)
https://leetcode.com/problems/xor-queries-of-a-subarray/description/comments/2623148

Assume the array is [a,b,c,d,e].
prefixXOR[0]=0(XOR of elements before the start)
prefixXOR[1]=a
prefixXOR[2]=a⊕b
prefixXOR[3]=a⊕b⊕c
prefixXOR[4]=a⊕b⊕c⊕d
prefixXOR[5]=a⊕b⊕c⊕d⊕e

To query the XOR from index 1 to 3:
prefixXOR[4]=a⊕b⊕c⊕d
prefixXOR[1]=a
prefixXOR[4]⊕prefixXOR[1]=(a⊕b⊕c⊕d)⊕a=b⊕c⊕
https://leetcode.com/problems/xor-queries-of-a-subarray/description/comments/2623240
"""

def xorQueries(a, q):
    """
    :type arr: List[int]
    :type queries: List[List[int]]
    :rtype: List[int]
    """
    n = len(a)
    prefix = [0] * n
    ans = []

    # Fill the prefix XOR array
    prefix[0] = a[0]
    for i in range(1, n):
        prefix[i] = prefix[i - 1] ^ a[i]

    # Process each query
    for left, right in q:
        if left == 0:
            ans.append(prefix[right])
        else:
            ans.append(prefix[right] ^ prefix[left - 1])

    return ans

print(xorQueries([1,3,4,8], [[0,1],[1,2],[0,3],[3,3]]))
print(xorQueries([4,8,2,10], q = [[2,3],[1,3],[0,0],[0,3]]))


# Time Limit Exceeded - 41 / 42 testcases passed
def xorQueries2(a, q):
    """
    :type arr: List[int]
    :type queries: List[List[int]]
    :rtype: List[int]
    """
    res=[]
    for i in range(len(q)):
        l,r=q[i][0],q[i][1]
        ress=a[l]
        for j in range(l+1,r+1):
            ress=ress ^ a[j]
        res.append(ress)
    return res
