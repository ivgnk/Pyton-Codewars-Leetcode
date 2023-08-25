'''
RankUp 004
создать все перестановки непустой входной строки и удалить дубликаты, если они есть.
Создайте как можно больше «перетасовок»!

With input 'a': Your function should return: ['a']
With input 'ab': Your function should return ['ab', 'ba']
With input 'abc': Your function should return ['abc','acb','bac','bca','cab','cba']
With input 'aabb':
Your function should return ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
https://www.codewars.com/kata/5254ca2719453dcc0b00027d/train/python
'''

import itertools

def permutations(s):
    '''
    см. https://stackoverflow.com/questions/8306654/finding-all-possible-permutations-of-a-given-string-in-python
    '''
    perms = [''.join(p) for p in itertools.permutations(s)]
    pp = set(perms)
    perms = list(pp)
    return perms

def thetest_permutations()->None:
    print('result = ', permutations('a'))
    print('result = ', permutations('ab'))
    print('result = ', permutations('abc'))
    print('result = ', permutations('aabb'))

if __name__ == "__main__":
    thetest_permutations()
