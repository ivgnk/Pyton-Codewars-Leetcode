'''
Учитывая два целых числа a и b,
которые могут быть положительными или отрицательными,
найдите сумму всех целых чисел между ними и включая их, и верните ее.
Если два числа равны, верните a или b.
Примечание: a и b не упорядочены!
'''

def get_sum(a,b)->int:
    if a==b:
        res = a
    else:
        if b < a:
            a,b = b, a
        res = sum(range(a,b+1))
    return res

def thetest_get_sum():
    for i in range(4):
        for j in range(4):
            s = get_sum(i, j)

if __name__ == "__main__":
    thetest_get_sum()
