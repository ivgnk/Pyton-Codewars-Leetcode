'''
Fundamentals 016
Реализуйте функцию, которая получает два IPv4-адреса и возвращает
количество адресов между ними (включая первый, исключая последний).
Все входные данные будут представлять собой действительные IPv4-адреса в виде строк.
Последний адрес всегда будет больше первого.
https://www.codewars.com/kata/526989a41034285187000de4/train/python

With input "10.0.0.0", "10.0.0.50"  => return   50
With input "10.0.0.0", "10.0.1.0"   => return  256
With input "20.0.0.10", "20.0.1.0"  => return  246
'''

def ips_between(start:str, end:str)->int:
    lst_start:list = start.split(sep='.')
    lst_end:list   = end.split(sep='.')
    d_s:list =[]
    d_e:list =[]
    for s in lst_start:
        d_s.append(int(s))
    d_s.reverse()
    for s in lst_end:
        d_e.append(int(s))
    d_e.reverse()
    num = 0
    for i in range(len(d_s)):
        if i == 0:
            num = num + (d_e[i] - d_s[i])
        else:
            num = num + (d_e[i] - d_s[i])*i*256
    return num
def thetest_ips_between()->None:
    print('result = ', ips_between("10.0.0.0", "10.0.0.50"))
    print('result = ', ips_between("10.0.0.0", "10.0.1.0"))
    print('result = ', ips_between("20.0.0.10", "20.0.1.0"))

if __name__ == "__main__":
    thetest_ips_between()
