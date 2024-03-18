'''
Calculating with Functions
https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39/train/python

This time we want to write calculations using functions and get the results.
Let's have a look at some examples:
seven(times(five())) # must return 35
four(plus(nine())) # must return 13
eight(minus(three())) # must return 5
six(divided_by(two())) # must return 3

Requirements:
There must be a function for each number from 0 ("zero") to 9 ("nine")
There must be a function for each of the following mathematical operations: plus, minus, times, divided_by
Each calculation consist of exactly one operation and two numbers
The most outer function represents the left operand, the most inner function represents the right operand
Division should be integer division. For example, this should return 2, not 2.666666...:
eight(divided_by(three()))
'''


def zero(n=None):
    if n is None: return '0'
    return eval('0' + n)

def one(n=None):
    if n is None: return '1'
    return eval('1' + n)

def two(n=None):
    if n is None: return '2'
    return eval('2' + n)

def three(n=None):
    if n is None: return '3'
    return eval('3' + n)

def four(n=None):
    if n is None: return '4'
    return eval('4' + n)

def five(n=None):
    if n is None: return '5'
    return eval('5' + n)

def six(n=None):
    if n is None: return '6'
    return eval('6' + n)

def seven(n=None):
    if n is None: return '7'
    return eval('7' + n)

def eight(n=None):
    if n is None: return '8'
    return eval('8' + n)

def nine(n=None):
    if n is None: return '9'
    return eval('9' + n)

# one of the Codewsrs best
# def zero(arg=""):  return eval("0" + arg)
# def one(arg=""):   return eval("1" + arg)
# def two(arg=""):   return eval("2" + arg)
# def three(arg=""): return eval("3" + arg)
# def four(arg=""):  return eval("4" + arg)
# def five(arg=""):  return eval("5" + arg)
# def six(arg=""):   return eval("6" + arg)
# def seven(arg=""): return eval("7" + arg)
# def eight(arg=""): return eval("8" + arg)
# def nine(arg=""):  return eval("9" + arg)
#
# def plus(n):       return '+' + str(n)
# def minus(n):      return '-' + str(n)
# def times(n):      return '*' + str(n)
# def divided_by(n): return '//' + str(n)


def plus(s: str):       return '+' + s
def minus(s: str):      return '-' + s
def times(s: str):      return '*' + s
def divided_by(s: str): return '//' + s

print(seven(times(five())))