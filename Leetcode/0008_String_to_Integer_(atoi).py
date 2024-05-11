'''
Done 11.05.2024. Topics: String
8. String to Integer (atoi)
https://leetcode.com/problems/string-to-integer-atoi/description/

Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.
The algorithm for myAtoi(string s) is as follows:

Whitespace: Ignore any leading whitespace (" ").
Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity is neither present.
Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or
the end of the string is reached. If no digits were read, then the result is 0.
Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1],
then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231,
and integers greater than 231 - 1 should be rounded to 231 - 1.
Return the integer as the final result.

Example 1:
Input: s = "42"
Output: 42
Explanation:
The underlined characters are what is read in and the caret is the current reader position.
Step 1: "42" (no characters read because there is no leading whitespace)
         ^
Step 2: "42" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "42" ("42" is read in)
           ^
Example 2:
Input: s = " -042"
Output: -42
Explanation:
Step 1: "   -042" (leading whitespace is read and ignored)
            ^
Step 2: "   -042" ('-' is read, so the result should be negative)
             ^
Step 3: "   -042" ("042" is read in, leading zeros ignored in the result)
               ^
Example 3:
Input: s = "1337c0d3"
Output: 1337
Explanation:
Step 1: "1337c0d3" (no characters read because there is no leading whitespace)
         ^
Step 2: "1337c0d3" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "1337c0d3" ("1337" is read in; reading stops because the next character is a non-digit)
             ^
Example 4:
Input: s = "0-1"
Output: 0
Explanation:
Step 1: "0-1" (no characters read because there is no leading whitespace)
         ^
Step 2: "0-1" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "0-1" ("0" is read in; reading stops because the next character is a non-digit)
          ^
Example 5:
Input: s = "words and 987"
Output: 0
Explanation:
Reading stops at the first non-digit character 'w'.
'''

ascii_lowercase= 'abcdefghijklmnopqrstuvwxyz '
ascii_lowercase2= 'abcdefghijklmnopqrstuvwxyz +'

# Runtime 34 ms Beats 81.45% of users with Python3
# Memory 16.60 MB Beats 78.85% of users with Python3

def repl_(s2,bads):
    fa=-1
    for i in range(len(s2)):
        if s2[i] in bads: #ascii_lowercase
            fa=i; break
    if fa !=-1:
        return s2[:fa]
    else:
        return s2

def repl_last(s2):
    if s2[-1]=='-': return s2[:-1]
    else: return s2

def myAtoi(s):
    """
    :type s: str
    :rtype: int
    """
    s2 = str.strip(s)
    ll = len(s2)
    if ll == 0: return 0
    if (s2 == "+") or (s2 == "-"): return 0
    if s2[0].isalpha(): return 0;

    s2 = repl_(s2, ascii_lowercase)

    if s2.find('+-') != -1: return 0
    if s2.find('-+') != -1: return 0
    if s2.find('-') != 0:
        s2 = repl_(s2, '-')
    if s2.isnumeric() or s2[1:].isnumeric():
        if s2.find('.') == -1:
            rr = int(s2)
        else:
            rr = int(float(s2))
        if rr <= -2147483648: return -2147483648
        if rr >= 2147483647: return 2147483647
        return rr
    s2 = repl_last(s2)
    s2 = repl_(s2, ascii_lowercase2)
    if not s2[1:].isnumeric() and s2.find('.') == -1: return 0
    if s2.find('.') == -1:
        rr = int(s2)
    else:
        rr = int(float(s2))
    if rr <= -2147483648: return -2147483648
    if rr >= 2147483647: return 2147483647
    return rr


print(myAtoi("-13+8"))
# print(myAtoi("-4193 with words"))
# print(myAtoi("words and 987"))
# print(myAtoi("3.14159"))
# print(myAtoi("00000-42a1234"))

