'''
RankUp 003
Формат выражения упорядоченного списка целых чисел заключается
в использовании списка отдельных целых чисел, разделенных запятыми,
или диапазона целых чисел, обозначенного начальным целым числом,
отделенным от конечного целого числа в диапазоне тире «-».
Диапазон включает все целые числа в интервале, включая обе конечные точки.
Он не считается диапазоном, если он не охватывает как минимум 3 числа.
Например, «12,13,15-17».
Завершите решение так, чтобы оно принимало список целых чисел в
порядке возрастания и возвращало правильно отформатированную строку в формате диапазона.
https://www.codewars.com/kata/51ba717bb08c1cd60f00002f/train/python
[-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20] => '-6,-3-1,3-5,7-11,14,15,17-20'
[-3,-2,-1,2,10,15,16,18,19,20] => '-3--1,2,10,15,16,18-20'

Примечание: список уже отсортированный
'''

# Потому что после вставки списка в в список
# новые операции с ним изменяют вставленный список
from copy import deepcopy

def solution(lst:list)->str:
    #--- Часть 1 сначала группировка чисел в новом списке
    llen = len(lst)
    res_lst = []
    diap = [None,None]
    prev = lst[0]
    diap[0] = prev
    for i in range(1,llen):
        # ряд продолжается
        # print(i, lst[i], res_lst,diap, lst[i]-prev == 1)
        if lst[i]-prev == 1:
            prev = lst[i]
            diap[1] = lst[i]
        else: # ряд прервался
            if diap[1] is None: # ряд прервался на первом числе
                res_lst.append(deepcopy(prev))
                diap[0] = lst[i]
                prev = lst[i]
            else: # ряд прервался не на первом числе
                res_lst.append(deepcopy(diap))
                diap[0] = lst[i]
                diap[1] = None
                prev = lst[i]
                # print('append ', res_lst)
    if not (diap[1] is None):
        res_lst.append(deepcopy(diap))
    #--- Часть 2 группировка списка по правилу
    res_str =  ''
    for lstitem in res_lst:
        if type(lstitem) == int:
            res_str = res_str +str(lstitem)+','
        else:
            llen = len(lstitem)
            if lstitem[1]-lstitem[0] < 2:
                for i in range(llen):
                    res_str = res_str + str(lstitem[i]) + ','
            else:
                res_str = res_str +str(lstitem[0])+'-'+str(lstitem[llen-1])+','
    # удаление конечной запятой
    nl = len(res_str)-1
    if res_str[nl]==',':
        res_str = res_str[:nl]
    return  res_str

def thetest_solution()->None:
    # '-6,-3-1,3-5,7-11,14,15,17-20'
    print('result = ', solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]))
    # '-3--1,2,10,15,16,18-20'
    print('result = ', solution([-3,-2,-1,2,10,15,16,18,19,20]))

if __name__ == "__main__":
    thetest_solution()
