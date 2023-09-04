'''
RankUp

Напишите функцию, которая принимает неотрицательное целое число (секунды) в качестве входных данных и возвращает время в удобочитаемом формате (ЧЧ:ММ:СС)
ЧЧ = часы, дополненные 2 цифрами, диапазон: 00 - 99
ММ = минуты, дополненные 2 цифрами, диапазон: 00 - 59
SS = секунды, дополненные 2 цифрами, диапазон: 00 - 59
Максимальное время никогда не превышает 359999 (99:59:59)

test.assert_equals(make_readable(0), "00:00:00")
test.assert_equals(make_readable(5), "00:00:05")
test.assert_equals(make_readable(60), "00:01:00")
test.assert_equals(make_readable(86399), "23:59:59")
test.assert_equals(make_readable(359999), "99:59:59")
https://www.codewars.com/kata/52685f7382004e774f0001f7/train/python
'''

def make_readable(seconds):
    # Do something
    tr_sec = seconds % 60
    tr_min = seconds // 60
    tr_hr = tr_min // 60
    if tr_min>=60 : tr_min = tr_min % 60
    s = str(tr_hr).zfill(2)+':'+str(tr_min).zfill(2)+':'+str(tr_sec).zfill(2)
    return s

def thetest_make_readable()->None:
    dat = 0
    print('result = ', make_readable(dat))
    dat = 5
    print('result = ', make_readable(dat))
    dat = 60
    print('result = ', make_readable(dat))
    dat = 86399
    print('result = ', make_readable(dat))
    dat = 359999
    print('result = ', make_readable(dat))

if __name__ == "__main__":
    thetest_make_readable()