'''
Ваша задача — отсортировать заданную строку.
Каждое слово в строке будет содержать одно число.
Это число — позиция, которую слово должно занимать в результате.
Примечание. Цифры могут быть от 1 до 9.
Таким образом, первым словом будет 1 (а не 0).
Если входная строка пуста, вернуть пустую строку.
Слова во входной строке будут содержать только допустимые последовательные числа.

"is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
"4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
""  -->  ""
'''
import string

def order(s:str)->str:
    llen = len(s)
    if llen == 0:
        return s
    else:
        in_list = s.split()
        llen2 = len(in_list)
        out_lst = [''] * llen2
        for ss in range(llen2): # цикл по словам в списке
            for ss2 in in_list[ss]: # цикл по символам в слове
                if ss2.isdigit():   # если символ - это цифра
                    num = int(ss2)  # переводим символ в целое число
                    out_lst[num-1] = in_list[ss]
                    break
        return ' '.join(out_lst)

def thetest_order()->None:
    s_lst = ["is2 Thi1s T4est 3a", "4of Fo1r pe6ople g3ood th5e the2"]
    for s in s_lst:
        print(s, '  order = ',order(s))

    # s_lst = ['2','T', 'a', '4']
    # for s in s_lst:
    #     print(s, '  ',s.isdigit())

    # s_lst = ["is2", "4of"]
    # print(' '.join(s_lst))

if __name__ == "__main__":
    thetest_order()
