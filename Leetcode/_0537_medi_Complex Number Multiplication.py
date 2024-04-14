"""
537. Complex Number Multiplication
https://leetcode.com/problems/complex-number-multiplication/description/

A complex number can be represented as a string on the form "real+imaginaryi" where:
real is the real part and is an integer in the range [-100, 100].
imaginary is the imaginary part and is an integer in the range [-100, 100].
i2 == -1.
Given two complex numbers num1 and num2 as strings, return a string of the complex number that represents their multiplications.

Example 1:
Input: num1 = "1+1i", num2 = "1+1i"
Output: "0+2i"
Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.

Example 2:
Input: num1 = "1+-1i", num2 = "1+-1i"
Output: "0+-2i"
Explanation: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert it to the form of 0+-2i.
"""
import re

# in leetcode do not work "complex"

def complexNumberMultiply2(num1, num2):
    """
    :type num1: str
    :type num2: str
    :rtype: str
    """
    num1=num1.replace('i','j')
    num2=num2.replace('i','j')
    mm=complex(num1) * complex(num2)
    s=str(mm)
    if mm.real==0: s='0+'+s
    return s.replace('j','i')

# def complexNumberMultiply(num1, num2):
#     """
#     :type num1: str
#     :type num2: str
#     :rtype: str
#     """
#     num1=num1.replace('i','j')
#     num2=num2.replace('i','j')
#     # https://stackoverflow.com/questions/4998629/split-string-with-multiple-delimiters-in-python
#     n1=[int(s1) for s1 in re.split("\+|j", num1) if s1 !='']
#     n2=[int(s2) for s2 in re.split("\+|j", num2) if s2 !='']
#     print(n1)
#     print(n2)
#     num2=num2.replace('i','j')


# print(complexNumberMultiply(num1 = "1+1i", num2 = "1+1i"))
print(complexNumberMultiply2(num1 = "1+1i", num2 = "1+1i"))