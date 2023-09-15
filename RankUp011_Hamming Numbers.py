'''
RankUp 011
A Hamming number is a positive integer of the form (2**i)*(3**j)*(5**k),
for some non-negative integers i, j, and k.
Write a function that computes the nth smallest Hamming number.

Specifically:

The first smallest Hamming number is 1 = 203050
The second smallest Hamming number is 2 = 213050
The third smallest Hamming number is 3 = 203150
The fourth smallest Hamming number is 4 = 223050
The fifth smallest Hamming number is 5 = 203051
https://www.codewars.com/kata/526d84b98f428f14a60008da/train/python
 '''
import sys
import time
import pprint
import test
from dataclasses import dataclass

# The program first calculates and stores in a global variable a list of objects with Hamming numbers
# (the list is sorted in ascending order of numbers). And then the desired number is selected from this list by.
# This is because the test server has time limits for each test.
# An attempt to memorize numbers was also implemented using closures, but it failed.
# I didn't rewrite the code, the closures remained, but the whole point is to save it in a global variable

@dataclass
class Ham:
    # n:int # номер попорядку
    i:int
    j:int
    k:int
    dat:int # само число  Хэмминга

nnum =-1
nnn = 100
nnn3 = nnn**3
llst = [None]*nnn3

def hamming(n):
    def inner_func():
        # start_time = time.time()
        global llst
        global nnum
        if nnum<0:
            print('calc')
            nnum = 1
            i_lst = [1]*nnn
            ii = 1
            for i in range(nnn):
                i_lst[i] = ii
                ii = ii*2

            j_lst = [1]*nnn
            jj = 1
            for j in range(nnn):
                j_lst[j] = jj
                jj = jj*3

            k_lst = [1]*nnn
            kk = 1
            for k in range(nnn):
                k_lst[k] = kk
                kk = kk*5

            num:int = 0
            # print("--- %s seconds ---" % (time.time() - start_time))
            # sys.exit()
            for i in range(nnn):
                # print(f'_ { num=}')
                ii = i_lst[i]
                for j in range(nnn):
                    iijj = ii*j_lst[j]
                    for k in range(nnn):
                        dat = iijj*k_lst[k]
                        llst[num] = (Ham(i,j,k, dat))
                        num +=1
            # print("--- %s seconds ---" % (time.time() - start_time))
            # https://pythonim.ru/list/metod-sort-python
            def custom_key(ham_num:Ham):
                return ham_num.dat #
            llst.sort(key=custom_key)
            # for i in range(1,20):
            #     print(f'{i}  {llst[i-1]}')
                # if (i % 100 == 0) and (i != 0) : input()
            # print(llst[n])
            # print("--- %s seconds ---" % (time.time() - start_time))
            # print(n)
        return llst[n-1].dat
    return inner_func()


def thetest_hamming():
    start_time = time.time()
    d = hamming(10)
    print(f'{d=}')
    print("--- %s seconds ---" % (time.time() - start_time))
    d = hamming(5000)
    print(f'{d=}')
    print("--- %s seconds ---" % (time.time() - start_time))
    # test.expect(hamming(1) == 1, "hamming(1) should be 1");


thetest_hamming()