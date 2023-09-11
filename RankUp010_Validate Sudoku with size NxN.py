'''
Решено правильно за исключением вырожденных случаев с 1 элементом

RankUp 010
Правила судоку можно найти в статье в Википедии.
http://en.wikipedia.org/wiki/Sudoku

Given a Sudoku data structure with size NxN, N > 0 and √N == integer,
write a method to validate if it has been filled out correctly.
The data structure is a multi-dimensional Array, i.e

[
  [7,8,4,  1,5,9,  3,2,6],
  [5,3,9,  6,7,2,  8,4,1],
  [6,1,2,  4,3,8,  7,5,9],

  [9,2,8,  7,1,5,  4,6,3],
  [3,5,7,  8,4,6,  1,9,2],
  [4,6,1,  9,2,3,  5,8,7],

  [8,7,6,  3,9,4,  2,1,5],
  [2,4,3,  5,6,1,  9,7,8],
  [1,9,5,  2,8,7,  6,3,4]
]
Rules for validation

Data structure dimension: NxN where N > 0 and √N == integer
Rows may only contain integers: 1..N (N included)
Columns may only contain integers: 1..N (N included)
'Little squares' (3x3 in example above) may also only contain integers: 1..N (N included)

https://www.codewars.com/kata/540afbe2dc9f615d5e000425/train/python
 '''

import numpy as np
import math

num = 0
class Sudoku(object):
    num = 0
    def __init__(self, data):
        global num
        num = num +1
        print(f'\n{num=}')
        self.is_valid_ = False
        try:
            self.data_ = np.array(data)
        except:
            self.is_valid_ = False
        else:
            self.is_valid_ =True
            self.row, self.col = self.data_.shape
            print(data)
            print(self.row, self.col)
            self.is_valid_ = (self.row == self.col) and (self.row >1)
            if self.is_valid_:
                self.all_int_ = self.all_int()
                self.is_valid_ = self.all_int_

        print(f'11 {self.is_valid_=}')

    def all_int(self)->bool:
        res = True
        for i in range(self.row):
            for j in range(self.col):
                a = (self.data_[i,j] % 1) == 0
                res = res and a
        return res

    def is_valid_data(self)->bool:
        the_valid_data = True
        good_ = np.linspace(1, self.row, self.row)
        for i in range(self.row):
            dat = self.data_[i,:]
            b1 = np.sort(dat)
            the_valid_data = the_valid_data and np.all(good_ == b1)
        for i in range(self.col):
            dat = self.data_[:,i]
            b1 = np.sort(dat)
            the_valid_data = the_valid_data and np.all(good_ == b1)
        return the_valid_data


    def is_valid(self):
        print(f'2 {self.is_valid_=}')
        if self.is_valid_:
            root_ = math.sqrt(self.col)
            self.is_valid_ = (self.row == self.col) and (self.col > 1) and root_.is_integer() and self.is_valid_data()
        print(f'3 {self.is_valid_=}')
        return self.is_valid_


def thetest_sudoku():
    print('test')
    print('\nFirst')
    t = [
    [7, 8, 4, 1, 5, 9, 3, 2, 6],
    [5, 3, 9, 6, 7, 2, 8, 4, 1],
    [6, 1, 2, 4, 3, 8, 7, 5, 9],

    [9, 2, 8, 7, 1, 5, 4, 6, 3],
    [3, 5, 7, 8, 4, 6, 1, 9, 2],
    [4, 6, 1, 9, 2, 3, 5, 8, 7],

    [8, 7, 6, 3, 9, 4, 2, 1, 5],
    [2, 4, 3, 5, 6, 1, 9, 7, 8],
    [1, 9, 5, 2, 8, 7, 6, 3, 4]]
    the_sudoku = Sudoku(t)
    print('First ',the_sudoku.is_valid())

    print('\nSecond ')
    t = ([
      [1,4, 2,3],
      [3,2, 4,1],

      [4,1, 3,2],
      [2,3, 1,4]
    ])
    the_sudoku = Sudoku(t)
    print('Second ',the_sudoku.is_valid())

    print('\nТретий ')
    t = [
      [0,2,3, 4,5,6, 7,8,9],
      [1,2,3, 4,5,6, 7,8,9],
      [1,2,3, 4,5,6, 7,8,9],

      [1,2,3, 4,5,6, 7,8,9],
      [1,2,3, 4,5,6, 7,8,9],
      [1,2,3, 4,5,6, 7,8,9],

      [1,2,3, 4,5,6, 7,8,9],
      [1,2,3, 4,5,6, 7,8,9],
      [1,2,3, 4,5,6, 7,8,9]
    ]
    the_sudoku = Sudoku(t)
    print('Третий ',the_sudoku.is_valid())

    print('\nЧетвертый ')
    t = [
      [1,2,3,4,5],
      [1,2,3,4],
      [1,2,3,4],
      [1]
    ]
    the_sudoku = Sudoku(t)
    print('Четвертый ',the_sudoku.is_valid())



thetest_sudoku()