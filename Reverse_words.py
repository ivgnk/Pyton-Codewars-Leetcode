'''
Завершите функцию, которая принимает строковый параметр и
меняет местами (на обратный порядок) в каждом слове в строке.
Все пробелы в строке должны быть сохранены.
'''
import string

def reverse_words(s:str):
    s = s.replace(" ", ",")
    llst = s.split(',')
    new_llst = []
    for ss in llst:
        new_llst.append(ss[::-1])
    s2 = " ".join(new_llst)
    return s2.replace(",", " ")

def thetest_reverse_words()->None:
    s = 'The quick brown fox jumps over the lazy dog'
    print(s, ' = ', reverse_words(s))
    s = 'apple'
    print(s, ' = ', reverse_words(s))
    s = 'a b c d'
    print(s, ' = ', reverse_words(s))
    s = 'double  spaced  words'
    print(s, ' = ', reverse_words(s))


if __name__ == "__main__":
    thetest_reverse_words()