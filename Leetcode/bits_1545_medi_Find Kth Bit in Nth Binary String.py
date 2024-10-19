"""
Done 19.10.2024. Topics: String, Recursion, Simulation
1545. Find Kth Bit in Nth Binary String
https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

Given two positive integers n and k, the binary string Sn is formed as follows:
S1 = "0"
Si = Si - 1 + "1" + reverse(invert(Si - 1)) for i > 1
Where + denotes the concatenation operation,
reverse(x) returns the reversed string x,
and invert(x) inverts all the bits in x (0 changes to 1 and 1 changes to 0).

For example, the first four strings in the above sequence are:
S1 = "0"
S2 = "011"
S3 = "0111001"
S4 = "011100110110001"
Return the kth bit in Sn. It is guaranteed that k is valid for the given n.

Example 1:
Input: n = 3, k = 1
Output: "0"
Explanation: S3 is "0111001".
The 1st bit is "0".

Example 2:
Input: n = 4, k = 11
Output: "1"
Explanation: S4 is "011100110110001".
The 11th bit is "1".

Constraints:
1 <= n <= 20
1 <= k <= 2n - 1

Hint 1
Since n is small, we can simply simulate the process of constructing S1 to Sn.

My solution
https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/solutions/5938147/easy-python-solution-with-result-ccumulation-in-string
"""
sn=[0]
nn1=1

# Runtime 45 ms Beats 56.52%
# Memory 37.82 MB Beats 8.70%
def findKthBit3(n, k):
    global sn
    global nn1
    if nn1>=n: return str(sn[k-1])
    else:
        for i in range(nn1,n):
            s1=[1 if ss==0 else 0 for ss in sn]
            sn=sn+[1]+s1[::-1]
        nn1=n
        return str(sn[k-1])

print(findKthBit3(n = 3, k = 1))
print(findKthBit3(n = 4, k = 11))

s="0"
nn=1
# Runtime 43 ms Beats 56.52%
# Memory 19.37 MB Beats 39.13%
# Time Complexity O(N)
# Space Complexity O(1)
def findKthBit2(n, k):
    """
    :type n: int
    :type k: int
    :rtype: str
    """
    global s
    global nn
    if nn>=n: return s[k-1]
    else:
        for i in range(nn,n):
            s1=''.join(['1' if ss=='0' else '0' for ss in s])
            s=s+'1'+s1[::-1]
        nn=n
        return s[k-1]

# print(findKthBit2(n = 3, k = 1))
# print(findKthBit2(n = 4, k = 11))