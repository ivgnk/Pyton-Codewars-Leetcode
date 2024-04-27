"""
1720. Decode XORed Array
There is a hidden integer array arr that consists of n non-negative integers.
It was encoded into another integer array encoded of length n - 1, such that
encoded[i] = arr[i] XOR arr[i + 1].
For example, if arr = [1,0,2,1], then encoded = [1,2,3].
You are given the encoded array.
You are also given an integer first, that is the first element of arr, i.e. arr[0].
Return the original array arr. It can be proved that the answer exists and is unique.

Example 1:
Input: encoded = [1,2,3], first = 1
Output: [1,0,2,1]
Explanation: If arr = [1,0,2,1], then first = 1 and encoded = [1 XOR 0, 0 XOR 2, 2 XOR 1] = [1,2,3]

Example 2:
Input: encoded = [6,2,7,3], first = 4
Output: [4,2,0,7,4]

Hint 1
Since that encoded[i] = arr[i] XOR arr[i+1], then arr[i+1] = encoded[i] XOR arr[i].
Hint 2
Iterate on i from beginning to end, and set arr[i+1] = encoded[i] XOR arr[i].
"""

# Runtime 153 ms Beats 90.95% of users with Python
# Memory 13.52 MB Beats 10.00% of users with Python


def decode(encoded, first):
    """
    :type encoded: List[int]
    :type first: int
    :rtype: List[int]
    """
    res=[first]
    for i in range(1,len(encoded)+1):
        res.append(encoded[i-1] ^ res[i-1])
    return res

print(decode(encoded = [1,2,3], first = 1))
