'''
Завершите функцию square sum таким образом,
чтобы она возводила в квадрат каждое переданное в нее число,
а затем суммировала результаты вместе.
https://www.codewars.com/kata/515e271a311df0350d00000f/train/python
'''

import numpy as np

def square_sum(numbers):
    dat = np.array(numbers)
    return np.sum(np.square(numbers))
def thetest_square_sum():
    llst = [i for i in range(5)]
    print(llst)
    ss = square_sum(llst)
    print(ss)

if __name__ == "__main__":
    thetest_square_sum()
