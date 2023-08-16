'''
https://www.codewars.com/kata/545cedaa9943f7fe7b000048/train/python
Панграмма — это предложение, в котором каждая буква алфавита встречается хотя бы по одному разу.
Например, предложение The quick brown fox jumps over the lazy dog
(«Быстрая коричневая лиса перепрыгивает через ленивую собаку»)
является панграммой, потому что в нем хотя бы один раз используются буквы A-Z (регистр значения не имеет).
Учитывая строку, определите, является ли она панграммой.
Возвращает True, если это так, False, если нет.
Не обращайте внимания на цифры и знаки препинания
'''
import string

def is_pangram(s)->bool:
    sm = s.lower()
    sl = string.ascii_lowercase
    res = True
    for sl2 in sl:
        res2 = False
        for sm2 in sm:
            res2 = res2 or (sm2 == sl2)
        res = res and res2
    return res

def thetest_pangram()->None:
    s = 'The quick brown fox jumps over the lazy dog 234565 FipPIo'
    print('is_pangram = ', is_pangram(s))

if __name__ == "__main__":
    thetest_pangram()