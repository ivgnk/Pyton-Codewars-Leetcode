'''
2423. Remove Letter To Equalize Frequency
https://leetcode.com/problems/remove-letter-to-equalize-frequency/description/

Вам дано строка, состоящая из строчных английских букв.
Вам нужно выбрать один индекс и удалить букву с этим
индексом из слова так, чтобы частота каждой буквы,
присутствующей в слове, была одинаковой.
Возвращайте true, если можно удалить одну букву,
чтобы частота всех букв в слове была одинаковой,
и false в противном случае. Примечание. Ч
астота буквы x — это количество раз, когда она встречается в строке.
Вы должны удалить ровно одну букву и не можете ничего не делать.
'''

def equalFrequency(word):
    """
    :type word: str
    :rtype: bool
    """
    the_set = set(word)
    word_len = len(word)
    set_len = len(the_set)
    if set_len==1: return True;
    IsOdd = (set_len % 2) != 0
    print(f'{word=}    {len(the_set)=}    {IsOdd=}')
    the_dict = {el:0 for el in the_set}
    for el in word:
       the_dict[el]=the_dict[el]+1
    the_num_lst = [the_dict[el] for el in the_dict]

    the_num_lst.sort(); llen = len(the_num_lst)
    print(the_num_lst)

    alleq = True
    for i in range(1,llen):
        alleq = alleq and (the_num_lst[i]==the_num_lst[i-1])
    if alleq and (the_num_lst[0] > 1): return False

    if (set_len==2):
        if the_num_lst[0]==1: return True
        # if (abs(the_num_lst[1] - the_num_lst[0]) > 1): return False
    if (set_len==3) and (the_num_lst[0]==1) and (the_num_lst[1]==the_num_lst[2]): return True

    True1='True1'; True2='True2'; True3='True3'; True4='True4'

    if ((the_num_lst[0] == the_num_lst[1]) and (the_num_lst[llen - 2] == the_num_lst[0]) and
            (the_num_lst[llen - 2] != the_num_lst[llen - 1]) and
            (the_num_lst[llen - 1] - the_num_lst[llen - 2]) == 1): return True1  # неповторяющийся в конце

    if ((the_num_lst[0] != the_num_lst[1]) and (the_num_lst[llen - 2] == the_num_lst[1]) and
            (the_num_lst[llen - 2] == the_num_lst[llen - 1]) and (the_num_lst[1] - the_num_lst[0]) == 1 and
            (the_num_lst[0] == 1)): return True  # неповторяющийся вначале

    if ((the_num_lst[0] == the_num_lst[1]) and (the_num_lst[llen - 2] == the_num_lst[0]) and
            (the_num_lst[llen - 2] == the_num_lst[llen - 1]) and IsOdd): return True3

    if ((the_num_lst[0] == the_num_lst[1]) and (the_num_lst[llen - 2] == the_num_lst[0]) and
            (the_num_lst[llen - 2] == the_num_lst[llen - 1]) and (word_len == set_len)): return True4

    if ((word_len) == 3) and (set_len == 2): return True
    if ((abs(the_num_lst[0]-the_num_lst[1]) == 1) and (set_len == 2)): return True
    return False

# print(equalFrequency("abcc"))
# print(equalFrequency("aazz"))
# print(equalFrequency("bac"))
# print(equalFrequency("cccaa"))
# print(equalFrequency("zz"))
# print(equalFrequency("huunhn"))
# print(equalFrequency("cccd")) # Expected true
# print(equalFrequency("ceeeec")) # Expected false
# print(equalFrequency("aaaabbbbccc")) # Expected false
print(equalFrequency("abbbccc")) # Expected True



