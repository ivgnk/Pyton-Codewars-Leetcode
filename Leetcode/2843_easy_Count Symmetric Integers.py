"""
Done 27.06.2024. Topics: Math, Enumeration
2843. Count Symmetric Integers
https://leetcode.com/problems/count-symmetric-integers/description/

You are given two positive integers low and high.
An integer x consisting of 2 * n digits is symmetric if the sum of the first n digits of x
is equal to the sum of the last n digits of x. Numbers with an odd number of digits are never symmetric.
Return the number of symmetric integers in the range [low, high].

Example 1:
Input: low = 1, high = 100
Output: 9
Explanation: There are 9 symmetric integers between 1 and 100: 11, 22, 33, 44, 55, 66, 77, 88, and 99.

Example 2:
Input: low = 1200, high = 1230
Output: 4
Explanation: There are 4 symmetric integers between 1200 and 1230: 1203, 1212, 1221, and 1230.

Hint 1
Iterate over all numbers from low to high
Hint 2
Convert each number to a string and compare the sum of the first half with that of the second.
"""


# Runtime 1092 ms Beats 84.48%
# Memory 11.87 MB Beats 75.00%
# Runtime 1079 ms Beats 86.21%
# Memory 12.06 MB Beats 12.93%

def countSymmetricIntegers(low, high):
    """
    :type low: int
    :type high: int
    :rtype: int
    """
    n=0
    for i in range(low,high+1):
        s=str(i)
        ll=len(s)
        if ll%2==0:
            ll2=ll//2
            s1=s[:ll2]; ss1=0
            s2=s[ll2:]; ss2=0
            for j in range(ll2):
                ss1=ss1+int(s1[j])
                ss2=ss2+int(s2[j])
            if ss1==ss2:
                n=n+1
    return n

print(countSymmetricIntegers(low = 1, high = 100))
print(countSymmetricIntegers(low = 1200, high = 1230))
