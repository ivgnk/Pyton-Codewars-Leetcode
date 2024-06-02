'''
Done 0206.2024. Topics: Hash Table, Math, String
12. Integer to Roman
https://leetcode.com/problems/integer-to-roman/

Seven different symbols represent Roman numerals with the following values:
Symbol	Value
I	1
V	5
X	10
L	50
C	100
D	500
M	1000
Roman numerals are formed by appending the conversions of decimal place values from highest to lowest. Converting a decimal place value into a Roman numeral has the following rules:

If the value does not start with 4 or 9, select the symbol of the maximal value that can be subtracted from the input,
append that symbol to the result, subtract its value, and convert the remainder to a Roman numeral.
If the value starts with 4 or 9 use the subtractive form representing one symbol subtracted from the following symbol,
for example, 4 is 1 (I) less than 5 (V): IV and 9 is 1 (I) less than 10 (X): IX. Only the following subtractive forms are used: 4 (IV), 9 (IX), 40 (XL), 90 (XC), 400 (CD) and 900 (CM).
Only powers of 10 (I, X, C, M) can be appended consecutively at most 3 times to represent multiples of 10.
You cannot append 5 (V), 50 (L), or 500 (D) multiple times. If you need to append a symbol 4 times use the subtractive form.
Given an integer, convert it to a Roman numeral.



Example 1:

Input: num = 3749

Output: "MMMDCCXLIX"

Explanation:

3000 = MMM as 1000 (M) + 1000 (M) + 1000 (M)
 700 = DCC as 500 (D) + 100 (C) + 100 (C)
  40 = XL as 10 (X) less of 50 (L)
   9 = IX as 1 (I) less of 10 (X)
Note: 49 is not 1 (I) less of 50 (L) because the conversion is based on decimal places
Example 2:

Input: num = 58

Output: "LVIII"

Explanation:

50 = L
 8 = VIII
Example 3:

Input: num = 1994

Output: "MCMXCIV"

Explanation:

1000 = M
 900 = CM
  90 = XC
   4 = IV
'''

# Преобразование значения десятичного знака в римскую цифру осуществляется по следующим правилам:
# если значение не начинается с 4 или 9, выберите символ максимального значения,
# которое можно вычесть из входных данных, добавьте этот символ к результату, вычтите его значение
# и преобразуем остаток в римскую цифру.
#
# Если значение начинается с 4 или 9, используйте вычитающую форму, представляющую один символ,
# вычтенный из следующего символа, например 4 равно 1 (I) меньше 5 (V): IV и 9 равно 1 (I)
# меньше 10 (X). ): IX.
# Используются только следующие субтрактивные формы: 4 (IV), 9 (IX),40 (XL), 90 (XC), 400 (CD) и 900 (CM).
#
# Только степени 10 (I, X, C, M) можно складывать последовательно не более 3 раз, чтобы представить числа, кратные 10.
# Нельзя складывать 5 (V), 50 (L) или 500 (D) несколько раз.
# Если вам нужно добавить символ 4 раза, используйте вычитающую форму.

from icecream import ic

# Runtime 27 ms Beats 73.60% of users with Python
# Memory 11.47 MB Beats 94.52% of users with Python
# Runtime 23 ms Beats 86.11% of users with Python
# Memory 11.53 MB Beats 74.35% of users with Python

def intToRoman(num):
    """
    :type num: int
    :rtype: str
    """
    def the4_9(n,por):
        if n ==4:
            if por == 3: return 'CD'
            elif por == 2: return 'XL'
            elif por == 1: return 'IV'
        else: # n==9
            if por == 3: return 'CM'
            elif por == 2: return 'XC'
            elif por == 1: return 'IX'

    def no4_9(n,por):
        if por==3:
            if n == 5: return 'D'
            elif n<4: return 'C'*n
            else: return 'D'+(n-5)*'C'
        elif por==2:
            if n==5: return 'L'
            elif n<4: return 'X'*n
            else: return 'L'+(n-5)*'X'
        elif por==1:
            if n==5: return 'V'
            elif n<4: return 'I'*n
            else: return 'V'+(n-5)*'I'

    d = list(map(int, str(num))); ll=len(d)
    d.reverse()
    res=''

    if ll>3: res='M'*d[3] #4

    if ll>2: #3
        if d[2]!=4 and d[2]!=9:  res=res+no4_9(d[2],3)
        else:  res = res + the4_9(d[2], 3)

    if ll>1: #2
        if d[1] != 4 and d[1] != 9: res = res + no4_9(d[1], 2)
        else: res = res + the4_9(d[1], 2)

    if d[0] != 4 and d[0] != 9: res = res + no4_9(d[0], 1)
    else: res = res + the4_9(d[0], 1)

    return res
# print(intToRoman(14))
# print(intToRoman(114))
ic(intToRoman(3749))
ic(intToRoman(58))
ic(intToRoman(1994))

import roman

def intToRoman2(num):
    """
    :type num: int
    :rtype: str
    """
    return roman.toRoman(num)

# ic(intToRoman2(40))

# https://pygame.ru/blog/python-kak-chislo-razbit-na-tsifri.php
# digits = list(map(int, str(6749)))
# print (digits)