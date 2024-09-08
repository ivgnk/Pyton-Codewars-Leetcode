"""
Done 09.09.2024. Topics: String
3280. Convert Date to Binary

You are given a string date representing a Gregorian calendar date in the yyyy-mm-dd format.

date can be written in its binary representation obtained by converting year, month, and day
to their binary representations without any leading zeroes and writing them down in year-month-day format.

Return the binary representation of date.

Example 1:
Input: date = "2080-02-29"
Output: "100000100000-10-11101"
Explanation:
100000100000, 10, and 11101 are the binary representations of 2080, 02, and 29 respectively.

Example 2:
Input: date = "1900-01-01"
Output: "11101101100-1-1"
Explanation:
11101101100, 1, and 1 are the binary representations of 1900, 1, and 1 respectively.

Constraints:
date.length == 10
date[4] == date[7] == '-', and all other date[i]'s are digits.
The input is generated such that date represents a valid Gregorian calendar date between Jan 1st,
1900 and Dec 31st, 2100 (both inclusive)
"""

# Runtime 30 ms Beats 100.00%
# Memory 16.35 MB Beats 100.00%
def convertDateToBinary(date):
    """
    :type date: str
    :rtype: str
    """
    s=date.split(sep='-')
    y=bin(int(s[0]))[2:]
    m=bin(int(s[1]))[2:]
    d=bin(int(s[2]))[2:]
    return y+'-'+m+'-'+d

# Runtime 35 ms Beats 100.00%
# Memory 16.58 MB Beats 100.00%
def convertDateToBinary2(date: str) -> str:
    s=date.split(sep='-')
    r=[bin(int(s[i]))[2:] for i in range(3)]
    return '-'.join(r)


# Runtime 38 ms Beats 100.00%
# Memory 16.36 MB Beats 100.00%

print(convertDateToBinary("2080-02-29"))

def convertDateToBinary3(date: str) -> str:
    s = date.split(sep='-')
    return '-'.join([bin(int(s[i]))[2:] for i in range(3)])
