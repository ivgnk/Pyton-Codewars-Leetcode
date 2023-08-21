'''
Дано слово. Вернуть средний символ слова.
Если длина слова нечетная, вернуть средний символ.
Если длина слова четная, вернуть средние 2 символа
https://www.codewars.com/kata/56747fd5cb988479af000028/train/python
Kata.getMiddle("test") should return "es"
Kata.getMiddle("testing") should return "t"
Kata.getMiddle("middle") should return "dd"
Kata.getMiddle("A") should return "A"
'''

def get_middle(s:str)->str:
    llen = len(s)
    if llen<=2:
        return s
    else:
        middle_len = llen // 2
        middle = llen % 2
        if middle == 0: # четное
            ss = s[middle_len-1:middle_len+1]
            return ss
        else: # нечетное
            return s[middle_len]

def thetest_get_middle()->None:
    s_lst = ["test", "testing", "middle", "A", "of", "resting", "mak", "amaka"]
    for s in s_lst:
        print(s, '  ',get_middle(s))

if __name__ == "__main__":
    thetest_get_middle()