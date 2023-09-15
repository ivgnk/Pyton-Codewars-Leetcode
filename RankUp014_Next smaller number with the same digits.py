'''
Тесты пройдены, но на длинной задаче сработало ограничение по времени

RankUp 014
Напишите функцию, которая принимает положительное целое число и
возвращает следующее меньшее положительное целое число,
содержащее те же цифры.

Вернуть -1 , если не существует меньшего числа, содержащего те же цифры.
Также верните -1, если следующее меньшее число с теми же цифрами потребует,
чтобы первая цифра была равна нулю.
https://www.codewars.com/kata/5659c6d896bc135c4c00021e/train/python
 '''
import itertools

def next_smaller(n):
    # Перестановки строки
    # https://pythonim.ru/osnovy/perestanovki-kombinatsii-python
    # print(f'\n{n=}')
    s = str(n)
    if len(s) == 1:
        return -1
    else:
        perm_set = list(itertools.permutations(s))
        str_list = []
        for tup in perm_set:
            ss = ''.join(tup)
            # print(ss)
            str_list.append(ss)
        str_list.sort()
        # print(str_list)

        num_list = [int(elem) for elem in str_list]
        ind = num_list.index(n)
        if (ind == 0) or (str_list[ind-1][0]=='0'):
            return -1
        else:
            # print(num_list,'  ',num_list[ind-1])
            # return str_list[0], str_list[0][0]
            return num_list[ind-1]



def thetest_next_smaller():
    # s = 21
    # print(next_smaller(s))
    # s = 531
    # print(next_smaller(s))
    # s =  2071
    # print(next_smaller(s))
    # s = 9
    # print(next_smaller(s))
    # s = 135
    # print(next_smaller(s))
    s = 1027
    print(next_smaller(s))
    # s = 123456789
    # print(next_smaller(s))
    # s = 1234567908
    # print(next_smaller(s))

thetest_next_smaller()