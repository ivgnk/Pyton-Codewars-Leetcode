'''
2710. Remove Trailing Zeros From a String
https://leetcode.com/problems/remove-trailing-zeros-from-a-string/description/

Given a positive integer num represented as a string, return the integer num without trailing zeros as a string.

Example 1:
Input: num = "51230100"
Output: "512301"
Explanation: Integer "51230100" has 2 trailing zeros, we remove them and return integer "512301".

Example 2:
Input: num = "123"
Output: "123"
Explanation: Integer "123" has no trailing zeros, we return integer "123".
'''

def removeTrailingZeros(num):
    """
    :type num: str
    :rtype: str
    """
    while num[-1]=='0':
        num = num.rstrip('0')
        print(num); input()
    return num

print(removeTrailingZeros("51230100"))