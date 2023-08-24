'''
Fundamentals 014
Напишите алгоритм, который берет массив и перемещает все нули в конец, сохраняя порядок остальных элементов.

 [1, 2, 0, 1, 0, 1, 0, 3, 0, 1] =>   [1, 2, 1, 1, 3, 1, 0, 0, 0, 0])
 [9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9] =>
 [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
 [0, 0] => [0, 0]
 [0] => [0]
 [] => []
https://www.codewars.com/kata/52597aa56021e91c93000cb0/train/python
'''

def move_zeros(lst:list)->list:
    llen = len(lst)
    if (llen == 0) or (llen == 1):
        return lst
    else:
        nzlst = []
        zlst = []
        for i in range(llen):
            if lst[i] == 0:
                zlst.append(lst[i])
            else:
                nzlst.append(lst[i])
        return nzlst+zlst

def thetest_move_zeros()->None:
    print('result = ', move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]))
    print('result = ', move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]))
    print('result = ', move_zeros([0, 0]))
    print('result = ', move_zeros([0]))
    print('result = ', move_zeros([] ))

if __name__ == "__main__":
    thetest_move_zeros()
