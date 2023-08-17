'''
Дано целое число, определите, является ли оно квадратом числа

В математике квадратное число или совершенный квадрат -
это целое число, которое является квадратом целого числа;
другими словами, это произведение некоторого целого числа на само себя.
'''
import numpy as np

def is_square(n):
    the_sqrt = np.sqrt(float(n))
    decimal_part = the_sqrt % 1
    if decimal_part <= np.finfo(float).eps:
        res = True
    else:
        res = False
    return res

def thetest_is_square()->None:
    llst = [1, 2, 4, 4 , 5, 16, 18, 27, 39, 49]
    for i in llst:
        print(i,' is square = ',is_square(i))

if __name__ == "__main__":
    # print(np.finfo(float).eps) # машинный ноль
    thetest_is_square()