"""
Done 07.07.2024. Topics: String
3211. Generate Binary Strings Without Adjacent Zeros
https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros/description/

You are given a positive integer n.
A binary string x is valid if all substrings
 of x of length 2 contain at least one "1".
Return all valid strings with length n, in any order.

Example 1:
Input: n = 3
Output: ["010","011","101","110","111"]
Explanation:
The valid strings of length 3 are: "010", "011", "101", "110", and "111".

Example 2:
Input: n = 1
Output: ["0","1"]
Explanation:
The valid strings of length 1 are: "0" and "1".

Constraints:
1 <= n <= 18

Hint 1
If we have a string s of length x, we can generate all strings of length x + 1.
Hint 2
If s has 0 as the last character, we can only append 1, whereas if the last character is 1, we can append both 0 and 1.
Hint 3
We can use recursion and backtracking to generate all such strings.
"""

# Runtime 42 ms Beats 100.00%
# Memory 12.78 MB Beats 100.00%
# Runtime 34 ms Beats 100.00%
# Memory 12.86 MB Beats 100.00%

# Time Complexity O(2**N)
# Space Complexity O(2**N)


from icecream import ic
def validStrings(n):
    """
    :type n: int
    :rtype: List[str]
    """
    arr=["0","1"]
    if n==1: return arr
    for i in range(1,n):
        narr=[]
        for j in range(len(arr)):
            if arr[j][-1]=='0':
                narr.append(arr[j]+'1')
            else:
                narr.append(arr[j]+'0')
                narr.append(arr[j]+'1')
        arr=narr
    return arr

# validStrings(2): ['01', '10', '11']
ic(validStrings(3))