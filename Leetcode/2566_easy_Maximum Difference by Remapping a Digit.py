"""
Done 18.09.2024. Topics: Math, Greedy
2566. Maximum Difference by Remapping a Digit

You are given an integer num.
You know that Bob will sneakily remap one of the 10 possible digits (0 to 9) to another digit.

Return the difference between the maximum and minimum values
Bob can make by remapping exactly one digit in num.

Notes:
When Bob remaps a digit d1 to another digit d2, Bob replaces all occurrences of d1 in num with d2.
Bob can remap a digit to itself, in which case num does not change.
Bob can remap different digits for obtaining minimum and maximum values respectively.
The resulting number after remapping can contain leading zeroes.

Example 1:
Input: num = 11891
Output: 99009
Explanation:
To achieve the maximum value, Bob can remap the digit 1 to the digit 9 to yield 99899.
To achieve the minimum value, Bob can remap the digit 1 to the digit 0, yielding 890.
The difference between these two numbers is 99009.

Example 2:
Input: num = 90
Output: 99
Explanation:
The maximum value that can be returned by the function is 99 (if 0 is replaced by 9) and the minimum value that can be returned by the function is 0 (if 9 is replaced by 0).
Thus, we return 99.

Constraints:
1 <= num <= 108

Hint 1
Try to remap the first non-nine digit to 9 to obtain the maximum number.
Hint 2
Try to remap the first non-zero digit to 0 to obtain the minimum number.
"""

# Runtime 3 ms Beats 100.00%
# Memory 11.56 MB Beats 63.16%
def minMaxDifference(num):
    """
    :type num: int
    :rtype: int
    """
    s = str(num)
    for i in range(len(s)):
        if s[i] != '9':
            smax = s.replace(s[i], '9')
            break
    else: smax = s
    smin = s.replace(s[0], '0')
    return int(smax) - int(smin)


print(minMaxDifference(num = 11891))
print(minMaxDifference(num = 90))