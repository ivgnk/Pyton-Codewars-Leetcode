"""
https://docs-python.ru/standart-library/modul-queue-python/funktsija-priorityqueue-modulja-queue/
"""
from icecream import ic
from random import *
from queue import *

n=30; nn=100
seed(nn)
lst=[randint(0,nn) for i in range(n)]
ic(lst)
lsts=sorted(lst)
ic(lsts[0],lsts[n-1])
ic(lsts)
q=PriorityQueue()
for i in range(n):
    q.put(lst[i])
job = q.get()
ic(job)

