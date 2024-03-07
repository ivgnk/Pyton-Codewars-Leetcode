'''
Не проходит один неправильно заданный тест на Codewars
'''
def comp(array1, array2):
    # your code
    if (array1 is None) and (array2 is None) : return True
    if (array1 is None) or (array2 is None) : return False

    if len(array1) != len(array2): return False
    if len(array1)==0: return False
    if len(array2)==0: return False
    array1.sort()
    array2.sort()
    for i in range(len(array1)):
        if (array1[i]*array1[i]-array2[i] !=0): return False
    return True

a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
print(comp(a1,a2))