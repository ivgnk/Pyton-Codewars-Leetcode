"""
Done 03.06.2024. Topics: Hash Table, Math, String
13. Roman to Integer
https://leetcode.com/problems/roman-to-integer/description/

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together.
12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII.
Instead, the number four is written as IV. Because the one is before the five we subtract it making four.
The same principle applies to the number nine, which is written as IX.
There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

Example 1:
Input: s = "III"
Output: 3
Explanation: III = 3.

Example 2:
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 3:
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4

Hint 1
Problem is simpler to solve by working the string from back to front and using a map.
"""

# Runtime 38 ms Beats 91.48% of users with Python3
# Memory 16.48 MB Beats 94.46% of users with Python3

from collections import Counter
from icecream import ic

def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    s=s[::-1]; ll=len(s)
    n = [0,0,0,0]
    withv, withx=False,False
    withl, withc=False,False
    withd, withm=False,False
    for i in range(ll):
        match s[i]:
            case 'I':
                if not withv and not withx: n[0]=n[0]+1
                elif withv: n[0] = 4
                elif withx: n[0] = 9; n[1]=n[1]-10
            case 'V':
                if n[0]<=3: n[0]=n[0]+5
                withv=True

            case 'X':
                if not withl and not withc: n[1]=n[1]+10
                elif withl: n[1] = 40
                elif withc: n[1] = 90; n[2]=n[2]-100
                withx = True

            case 'L':
                if n[1] <= 30: n[1] = n[1] + 50
                withl=True
            # ----------------------------
            case 'C':
                if not withd and not withm: n[2]=n[2]+100
                elif withd: n[2] = 400
                elif withm: n[2] = 900; n[3]=n[3]-1000
                withc = True
            case 'D':
                if n[2] <= 300: n[2] = n[2] + 500
                withd=True
            case 'M':
                if n[3] <= 3000: n[3] = n[3] + 1000
                withm=True
        print(i,s[i],n)
    return sum(n)
# ic(romanToInt("III"))
# ic(romanToInt("LVIII"))
# ic(romanToInt("MCMXCIV"))
ic(romanToInt("MMCCCXCIX"))