'''
2259. Remove Digit From Number to Maximize Result
https://leetcode.com/problems/remove-digit-from-number-to-maximize-result/description/

You are given a string number representing a positive integer and a character digit.
Return the resulting string after removing exactly one occurrence of digit from number
such that the value of the resulting string in decimal form is maximized.
The test cases are generated such that digit occurs at least once in number.

Example 1:
Input: number = "123", digit = "3"
Output: "12"
Explanation: There is only one '3' in "123". After removing '3', the result is "12".

Example 2:
Input: number = "1231", digit = "1"
Output: "231"
Explanation: We can remove the first '1' to get "231" or remove the second '1' to get "123".
Since 231 > 123, we return "231".

Example 3:
Input: number = "551", digit = "5"
Output: "51"
Explanation: We can remove either the first or second '5' from "551".
Both result in the string "51".
'''

# https://stackoverflow.com/questions/4664850/how-to-find-all-occurrences-of-a-substring

# Runtime 12 ms Beats 81.00% of users with Python
# Memory 11.49 MB Beats 100.00% of users with Python

import re
def removeDigit(number:str, digit:str):
    """
    :type number: str
    :type digit: str
    :rtype: str
    """
    c=number.count(digit)
    if c==1: return number.replace(digit,'')

    ll= [m.start() for m in re.finditer(digit, number)]
    lli=[int(number[:lp] + number[lp+1:]) for lp in ll]
    return str(max(lli))

print(removeDigit( number = "1231", digit = "1"))