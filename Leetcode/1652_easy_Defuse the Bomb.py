"""
Done 29.09.2024. Topics: Array, Sliding Window
1652. Defuse the Bomb. Topics: Array, Sliding Window
https://leetcode.com/problems/defuse-the-bomb/description/

You have a bomb to defuse, and your time is running out!
Your informer will provide you with a circular array code of length of n and a key k.
To decrypt the code, you must replace every number. All the numbers are replaced simultaneously.

If k > 0, replace the ith number with the sum of the next k numbers.
If k < 0, replace the ith number with the sum of the previous k numbers.
If k == 0, replace the ith number with 0.
As code is circular, the next element of code[n-1] is code[0],
and the previous element of code[0] is code[n-1].

Given the circular array code and an integer key k, return the decrypted code to defuse the bomb!

Example 1:
Input: code = [5,7,1,4], k = 3
Output: [12,10,16,13]
Explanation: Each number is replaced by the sum of the next 3 numbers. The decrypted code is [7+1+4, 1+4+5, 4+5+7, 5+7+1]. Notice that the numbers wrap around.

Example 2:
Input: code = [1,2,3,4], k = 0
Output: [0,0,0,0]
Explanation: When k is zero, the numbers are replaced by 0.

Example 3:
Input: code = [2,4,9,3], k = -2
Output: [12,5,6,13]
Explanation: The decrypted code is [3+9, 2+3, 4+2, 9+4]. Notice that the numbers wrap around again. If k is negative, the sum is of the previous numbers.

Constraints:
n == code.length
1 <= n <= 100
1 <= code[i] <= 100
-(n - 1) <= k <= n - 1

Hint 1
As the array is circular, use modulo to find the correct index.
Hint 2
The constraints are low enough for a brute-force solution.

Solution
✏️ Easy Python solution with extended array
Intuition
Expand the array to avoid thinking about indexing
"""

# Runtime 18 ms Beats 89.33%
# Memory 11.38 MB Beats 100.00%
def decrypt(code, k):
    """
    :type code: List[int]
    :type k: int
    :rtype: List[int]
    """
    ll=len(code)
    if k==0:
        res = [0]*ll
    elif k>0:
        code=code+code+code
        res=[]
        for i in range(ll,ll+ll):
            s=i+1
            e=i+1+k
            res.append(sum(code[s:e]))
    else:
        code2=code+code+code
        res=[]
        for i in range(ll):
            s=i+k+ll
            e=i+ll
            res.append(sum(code2[s:e]))
    return res

# print(decrypt(code = [5,7,1,4], k = 3))
# print(decrypt(code = [1,2,3,4], k = 0))
print(decrypt(code = [2,4,9,3], k = -2))
