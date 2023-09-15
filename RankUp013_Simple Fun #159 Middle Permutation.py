'''
Тесты пройдены, но на длинной задаче сработало ограничение по времени

RankUp 013
Задача Вам дана строка s. Каждая буква в s встречается один раз.
Рассмотрим все строки, образованные перестановкой букв в s.
Упорядочив эти строки в словарном порядке, верните средний термин.
(Если последовательность имеет четную длину n, определите ее средний член как (n/2))

For s = "abc", the result should be "bac".
The permutations in order are: "abc", "acb", "bac", "bca", "cab", "cba" So, The middle term is "bac".
https://www.codewars.com/kata/58ad317d1541651a740000c5/train/python
 '''
import itertools


def middle_permutation(s:str):
    # Перестановки строки
    # https://pythonim.ru/osnovy/perestanovki-kombinatsii-python
    perm_set = list(itertools.permutations(s))
    str_list = []
    for tup in perm_set:
        ss = ''.join(tup)
        # print(ss)
        str_list.append(ss)
    str_list.sort()
    llen = (len(str_list) // 2) - 1
    print(str_list,' ',len(str_list),' ',llen)
    return str_list[llen]



def thetest_middle_permutation():
    s = "abc"
    print(middle_permutation(s))
    s = "abcd"
    print(middle_permutation(s))
    s =  'abcdx'
    print(middle_permutation(s))
    s = 'abcdxg'
    print(middle_permutation(s))
    s = 'abcdxgz'
    print(middle_permutation(s))

thetest_middle_permutation()