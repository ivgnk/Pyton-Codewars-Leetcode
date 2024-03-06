'''
https://leetcode.com/problems/integer-to-roman/
Решение с помощью готовой библиотеки
'''
import roman

def intToRoman(num):
    """
    :type num: int
    :rtype: str
    """
    return roman.toRoman(num)

print(intToRoman(14))
print(intToRoman(114))
print(intToRoman(2114))