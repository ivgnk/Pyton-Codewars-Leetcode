'''
Take an integer n (n >= 0) and a digit d (0 <= d <= 9) as an integer.
Square all numbers k (0 <= k <= n) between 0 and n.
Count the numbers of digits d used in the writing of all the k**2.
Implement the function taking n and d as parameters and returning this count.

n = 10, d = 1
the k*k are 0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100
We are using the digit 1 in: 1, 16, 81, 100. The total count is then 4.

The function, when given n = 25 and d = 1 as argument, should return 11 since
the k*k that contain the digit 1 are:
1, 16, 81, 100, 121, 144, 169, 196, 361, 441.
So there are 11 digits 1 for the squares of numbers between 0 and 25.
'''

def nb_dig(n:int, d:int)->int:
    n1 = 60000
    arr_s = ['']*n1
    nn = 0
    for i in range(n+1):
        arr_s[i] = str(i * i)
        nn +=1
    nd=0
    ds=str(d)
    for i in range (nn+1):
        nd = nd + arr_s[i].count(ds)
    return nd


def thetest_nb_dig():
    print(nb_dig(5750, 0)) # 4700)
    print(nb_dig(11011, 2)) # 9481
    print(nb_dig(12224, 8)) # 7733
    print(nb_dig(11549, 1)) # 11905
    print(nb_dig(14550, 7)) # 8014
    print(nb_dig(8304, 7)) # 3927
    print(nb_dig(10576, 9)) # 7860

thetest_nb_dig()