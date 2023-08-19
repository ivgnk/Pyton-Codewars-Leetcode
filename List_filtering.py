'''
функция, которая принимает список неотрицательных целых чисел и строк и
возвращает новый список только с числами.
'''

def filter_list(llst:list)->list:
    new_list=[]
    for dat in llst:
        if type(dat) == int:
            new_list.append(dat)
    return new_list

def thetest_filter_list():
    llst = [1, 2, 'a', 'b']
    print(filter_list(llst))
    llst = [1, 'a', 'b', 0, 15]
    print(filter_list(llst))
    llst = [1, 2, 'aasf', '1', '123', 123]
    print(filter_list(llst))

if __name__ == "__main__":
    # print(np.finfo(float).eps) # машинный ноль
    thetest_filter_list()
