'''
Fundamentals 015
Учитывая случайное неотрицательное число,
вам необходимо вернуть цифры этого числа в массиве в обратном порядке.
35231 => [1,3,2,5,3]
0 => [0]
23582357 => [7,5,3,2,8,5,3,2]
984764738 => [8,3,7,4,6,7,4,8,9]
45762893920 => [0,2,9,3,9,8,2,6,7,5,4]
548702838394 => [4,9,3,8,3,8,2,0,7,8,4,5]

https://www.codewars.com/kata/5583090cbe83f4fd8c000051/train/python
'''

def digitize(dat:int)->list:
    s = str(dat)
    lst:list=[]
    for cchr in s:
        iint = int(cchr)
        lst.append(iint)
    lst.reverse()
    return lst
def thetest_digitize()->None:
    print('result = ', digitize(35231))
    print('result = ', digitize(0))
    print('result = ', digitize(23582357))
    print('result = ', digitize(45762893920))
    print('result = ', digitize(548702838394))

if __name__ == "__main__":
    thetest_digitize()
