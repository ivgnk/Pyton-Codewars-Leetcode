"""
Done 22.06.2024. Topics: Math, Sorting

2165. Smallest Value of the Rearranged Number
https://leetcode.com/problems/smallest-value-of-the-rearranged-number/description/

You are given an integer num. Rearrange the digits of num such that its value is minimized and it does not contain any leading zeros.
Return the rearranged number with minimal value.
Note that the sign of the number does not change after rearranging the digits.

Example 1:
Input: num = 310
Output: 103
Explanation: The possible arrangements for the digits of 310 are 013, 031, 103, 130, 301, 310.
The arrangement with the smallest value that does not contain any leading zeros is 103.

Example 2:
Input: num = -7605
Output: -7650
Explanation: Some possible arrangements for the digits of -7605 are -7650, -6705, -5076, -0567.
The arrangement with the smallest value that does not contain any leading zeros is -7650.

Hint 1
For positive numbers, the leading digit should be the smallest nonzero digit. Then the remaining digits follow in ascending order.
Hint 2
For negative numbers, the digits should be arranged in descending order.
"""


# Runtime 18 ms Beats 31.43%
# Memory 11.66 MB Beats 34.29%
# Runtime 15 ms Beats 57.14%
# Memory 11.57 MB Beats 60.00%
# Runtime 14 ms Beats 62.86%
# Memory 11.56 MB Beats 60.00%
def smallestNumber2(num):
    """
    :type num: int
    :rtype: int
    """
    if num == 0: return num

    s=str(num)
    if num<0:
        s=s[1:]
        s=sorted(s,reverse=True)
    else:
        s=sorted(s)
    if num<0:
        s=["-"]+s
    else:
        n=s.count('0')
        if n !=0:
            s=s[n:]
            s=[s[0]]+['0' for i in range(n)]+s[1:]
    return int(''.join(s))

# Runtime 12 ms Beats 71.43%
# Memory 11.45 MB Beats 97.14%
def smallestNumber3(num):
    """
    :type num: int
    :rtype: int
    """
    if num == 0: return num

    s=str(num)
    if num<0:
        s = sorted(s[1:], reverse=True)
    else:
        s=sorted(s)
    if num<0:
        ns=["-"]+s
    else:
        n=s.count('0')
        if n !=0:
            s=s[n:]
            s=[s[0]]+['0' for i in range(n)]+s[1:]
    return int(''.join(s))


# Runtime 9 ms Beats 85.71%
# Memory 11.44 MB Beats 97.14%
def smallestNumber(num):
    """
    :type num: int
    :rtype: int
    """
    if num == 0: return num

    s=str(num)
    if num<0:
        s = sorted(s[1:], reverse=True)
    else:
        s=sorted(s)
    if num<0:
        ns="-"+''.join(s)
    else:
        n=s.count('0')
        if n !=0:
            s=s[n:]
            ns=s[0]+'0'*n+''.join(s[1:])
        else:
            ns=''.join(s)
    return int(ns)


print(smallestNumber(310))
print(smallestNumber(-7605))