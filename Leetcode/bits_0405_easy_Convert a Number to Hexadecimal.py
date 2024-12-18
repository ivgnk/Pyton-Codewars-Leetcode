"""
Done 18.12.2024. Topics: Math, Bit Manipulation
405. Convert a Number to Hexadecimal
https://leetcode.com/problems/convert-a-number-to-hexadecimal/description/

Given a 32-bit integer num,
return a string representing its hexadecimal representation.
For negative integers, two’s complement method is used.

All the letters in the answer string should be lowercase characters,
and there should not be any leading zeros in the answer except for the zero itself.

Note: You are not allowed to use any built-in library method to directly solve this problem.

Example 1:
Input: num = 26
Output: "1a"

Example 2:
Input: num = -1
Output: "ffffffff"

Constraints:
-231 <= num <= 231 - 1

https://en.wikipedia.org/wiki/Two%27s_complement
Дополнительный код (англ. "two’s complement", иногда "twos-complement") — наиболее распространённый способ представления
отрицательных целых чисел в компьютерах. Он позволяет заменить операцию вычитания на операцию сложения и сделать операции
сложения и вычитания одинаковыми для знаковых и беззнаковых чисел, что упрощает архитектуру ЭВМ. В англоязычной литературе
«обратный код» (инверсия прямого кода) называют «первым дополнением» (англ. "ones' complement"), а «дополнительный код»
называют «вторым дополнением» (англ. "two’s complement").

Дополнительный код для отрицательного числа можно получить инвертированием его двоичного модуля
(получается "первое дополнение") и прибавлением к инверсии единицы (получается "второе дополнение"),
либо вычитанием числа из нуля (сразу получается "второе дополнение").
10-ное      двоич.прямой        двоич.обратн.       двоич.дополнит.
−2       	1000 0010       	1111 1101       	1111 1110

My solution https://leetcode.com/problems/convert-a-number-to-hexadecimal/solutions/6160401/fast-0-ms-and-easy-python-solution-for-p-2yqh/
✏️ Fast (0 ms) and easy Python solution for Problem 0405, based on tip in discussion
Intuition
1) Use hex function if num>=0
2) For negative numbers, num=2^32+num
https://leetcode.com/problems/convert-a-number-to-hexadecimal/description/comments/1726347
"""

def toHex(num):
    """
    :type num: int
    :rtype: str
    """
    # For negative numbers, num=2^32+num
    if num>=0:
        s = hex(num)
    else:
        s = hex(2**32+num)
    return s[2:]

# Runtime 0 ms Beats 100.00%
# Memory 12.48 MB Beats 5.03%
# Time Complexity O(1)
# Space Complexity O(1)
# For negative numbers, num=2^32+num
# https://leetcode.com/problems/convert-a-number-to-hexadecimal/description/comments/1726347
dat = 2 ** 32
class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num >= 0:
            s = hex(num)
        else:
            s = hex(dat + num)
        return s[2:]
