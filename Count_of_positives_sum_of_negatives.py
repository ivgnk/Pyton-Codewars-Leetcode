'''
Fundamentals

Задан массив целых чисел.
Возвращает массив, где первый элемент - это количество положительных чисел,
а второй элемент - сумма отрицательных чисел. 0 не является ни положительным, ни отрицательным.
Если входные данные представляют собой пустой массив или имеют значение null, верните пустой массив.
Массив в ссмысле список

test.assert_equals(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]),[10,-65])
test.assert_equals(count_positives_sum_negatives([0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14]),[8,-50])
test.assert_equals(count_positives_sum_negatives([1]),[1,0])
test.assert_equals(count_positives_sum_negatives([-1]),[0,-1])
test.assert_equals(count_positives_sum_negatives([0,0,0,0,0,0,0,0,0]),[0,0])
test.assert_equals(count_positives_sum_negatives([]),[])
https://www.codewars.com/kata/576bb71bbbcf0951d5000044/train/python
'''

def count_positives_sum_negatives(arr:list)->list:
    if (arr is None) or (not arr):
        res = []
    else:
        n_pos = 0
        sum_neg = 0
        for dat in arr:
            if dat>0:
                n_pos = n_pos + 1
            elif dat<0:
                sum_neg = sum_neg + dat
        res = [n_pos, sum_neg]
    return res


def thetest_count_positives_sum_negatives()->None:
    dat = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]
    print('result = ', count_positives_sum_negatives(dat))
    dat = [1, 0]
    print('result = ', count_positives_sum_negatives(dat))
    dat = [-1]
    print('result = ', count_positives_sum_negatives(dat))
    dat = [0,0,0,0,0,0,0,0,0]
    print('result = ', count_positives_sum_negatives(dat))
    dat = []
    print('result = ', count_positives_sum_negatives(dat))

if __name__ == "__main__":
    thetest_count_positives_sum_negatives()