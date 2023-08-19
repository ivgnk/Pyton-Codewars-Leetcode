'''
Есть строка чисел, разделенных пробелами, и вы должны вернуть наибольшее и наименьшее число
в строке, разделенные пробелами
'''

def high_and_low(s):
    llst = s.split()
    new_llst = [int(s) for s in llst]
    mmax =max(new_llst)
    mmin =min(new_llst)
    return str(mmax)+' '+str(mmin)

def thetest_high_and_low():
    '''
        high_and_low("1 2 3 4 5")
        high_and_low("1 2 -3 4 5") # return "5 -3"
        high_and_low("1 9 3 4 -5") # return "9 -5"
    '''
    s = "1 2 3 4 5"; print(high_and_low(s)) # return "5 1"
    s = "1 2 -3 4 5"; print(high_and_low(s)) # return "5 -3"
    s = "1 9 3 4 -5"; print(high_and_low(s)) # return "9 -5"

if __name__ == "__main__":
    thetest_high_and_low()
