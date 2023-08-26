'''
Fundamentals 015
Построить башню Построить башню в форме пирамиды в виде массива.

Например, a tower with 3 floors looks like this:
[
  "  *  ",
  " *** ",
  "*****"
]
https://www.codewars.com/kata/576757b1df89ecf5bd00073b/train/python
'''

def tower_builder(n_floors:int)->list:
    res = []
    max_len = 2*n_floors-1
    for i in range(n_floors):
        curr_len = 1+2*i
        s = '*'*curr_len
        s = s.center(max_len,' ')
        res.append(s)
    return res

def thetest_tower_builder()->None:
    print('result = ', tower_builder(1))
    print('result = ', tower_builder(2))
    print('result = ', tower_builder(3))

if __name__ == "__main__":
    thetest_tower_builder()
