'''
Fundamentals 13

Некоторые числа обладают забавными свойствами. Например:
89 --> 8¹ + 9² = 89 * 1
695 --> 6² + 9³ + 5⁴= 1390 = 695 * 2
46288 --> 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51

Дано положительное целое число n, записанное как abcd... (a, b, c, d... - цифры) и положительное целое число p

мы хотим найти положительное целое число k, если оно существует, такое,
чтобы сумма цифр числа n, взятых в последовательных степенях p, была равна k * n.

Другими словами:
Существует ли целое число k, такое как : (a ^ p + b ^ (p+ 1) + c ^ (p + 2) + d ^ (p + 3) + ...) = n * k
Если это так, мы вернем k, если нет, вернем -1.
Примечание: n и p всегда будут задаваться как строго положительные целые числа.
https://www.codewars.com/kata/5552101f47fc5178b1000050/train/python
'''

def dig_pow(num:int, p:int)->int:
    # разбиение на список цифр
    # https://www.delftstack.com/howto/python/split-integer-into-digits-python/
    x = [int(a) for a in str(num)]
    llen = len(x); sum = 0
    for i in range(llen):
        sum = sum + x[i]**(p+i)
    # print(num,' ', x, sum,end='  ')
    if sum % num == 0:
        # print('нацело')
        return sum // num
    else:
        return -1


def thetest_dig_pow()->None:
    print('result = ', dig_pow(89, 1))
    print('result = ', dig_pow(92, 1))
    print('result = ', dig_pow(46288, 3))
    print('result = ', dig_pow(41, 5))
    print('result = ', dig_pow(114, 3))
    print('result = ', dig_pow(8, 3))

if __name__ == "__main__":
    thetest_dig_pow()