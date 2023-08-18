'''
Реализуйте функцию, которая складывает два числа вместе и
возвращает их сумму в двоичном виде.
Преобразование может быть выполнено как до, так и после добавления.
Возвращаемое двоичное число должно быть строкой (без лиирующих 0b).
'''

def add_binary(a,b)->str:
    c = bin(a + b)
    # c.replace('0b', '')
    return c[2:]

def thetest_add_binary()->None:
    for i in range(4):
        for j in range(4):
            print(add_binary(i, j))

if __name__ == "__main__":
    thetest_add_binary()
