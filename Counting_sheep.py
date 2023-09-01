'''
Рассмотрим массив / список овец, в котором некоторые овцы могут отсутствовать на своем месте.
Нам нужна функция, которая подсчитывает количество овец, присутствующих в массиве
(true означает "присутствует").
'''

def count_sheeps(sheep):
    i=0
    for j in sheep:
        i += int(bool(j))
    return i

def thetest_count_sheeps():
    llst = [True,  True,  True,  False, True,  True,  True,  True ,  True,  False, True,  False,
            True,  False, False, True ,  True,  True,  True,  True , False, False, True,  True]
    print(count_sheeps(llst))

if __name__ == "__main__":
    thetest_count_sheeps()
