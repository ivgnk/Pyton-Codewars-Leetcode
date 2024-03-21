# 7 kyu Sum of odd numbers
# https://www.codewars.com/kata/55fd2d567d94ac3bc9000064/train/python

# Given the triangle of consecutive odd numbers:
#
#              1
#           3     5
#        7     9    11
#    13    15    17    19
# 21    23    25    27    29
# ...
# Calculate the sum of the numbers in the nth row of this triangle (starting at index 1) e.g.: (Input --> Output)
#
# 1 -->  1
# 2 --> 3 + 5 = 8

import numpy as np
# https://pygame.ru/blog/python-uravnenie-pryamoy.php
# https://www.delftstack.com/howto/matplotlib/plot-numpy-linear-fit-matplotlib-python/
def calc_appr():
    x = np.array([1, 2, 3, 4, 5])
    y = np.array([1, 3, 7, 13, 21])
    coeff = np.polyfit(x, y, 2)
    print(coeff)
    a = int(coeff[0])
    b = int(coeff[1])
    c = int(coeff[2])
    print(a,b,c)

    def yaxb(a,b,c,x):
        return a*x**2 + b*x+c

    print(yaxb(a,b,c,4))

def row_sum_odd_numbers(n):
    a = 1; b=-1; c = 1
    first =a*n**2 + b*n+ c
    res=[first]
    for i in range(n-1):
        first = first+2
        res.append(first)
    return sum(res)

# Best of codevars
#
# def row_sum_odd_numbers(n):
#     return n ** 3
# def row_sum_odd_numbers(n):
#     sum(range(n*(n-1)+1, n*(n+1), 2))


print(row_sum_odd_numbers(3))
