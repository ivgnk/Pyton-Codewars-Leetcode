"""
30.07.2024. Тестирование времени циклов
https://thecode.media/python-timing/
"""
import datetime
import random

n=100000
s=[0 for i in range(n)]
###---------- 1
b=0
start = datetime.datetime.now()
for i in range(n):
    b=s[i]
finish = datetime.datetime.now()
print('for i in range(n): ',finish - start)

###---------- 2
b=0
start = datetime.datetime.now()
i=0
while i<=n-1:
    b=s[i]
    i=i+1
finish = datetime.datetime.now()
print('     while i<=n-1: ',finish - start)

###---------- 3
b=0
start = datetime.datetime.now()
for s1 in s:
    b=s1
finish = datetime.datetime.now()
print('      for s1 in s: ',finish - start)

###---------- 4
b=0
start = datetime.datetime.now()
for i,s1 in enumerate(s):
    b=s1
finish = datetime.datetime.now()
print('for i,s1 in enumerate(s): ',finish - start)

