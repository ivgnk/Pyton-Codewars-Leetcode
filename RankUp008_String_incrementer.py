'''
RankUp 008
Ваша задача — написать функцию, которая увеличивает строку
для создания новой строки. Если строка уже заканчивается числом,
это число должно быть увеличено на 1.
Если строка не заканчивается числом, то к новой строке следует добавить число 1.
Примеры:
foo -> foo1
foobar23 -> foobar24
foo0042 -> foo0043
foo9 -> foo10
foo099 -> foo100
https://www.codewars.com/kata/54a91a4883a7de5d7800009c/train/python
 '''

def increment_string(s:str)->str:
    llen = len(s)
    num_s = ''; txt_s = ''
    for simb in range(llen-1, 0,-1):
        if s[simb].isdigit():
            num_s = s[simb] + num_s
        else:
            txt_s = s[:simb+1]
            break
    if num_s == '':
        s = s + '1'
    else:
        # print(num_s,' ',txt_s)
        new_s = str(int(num_s)+1)
        s = txt_s + new_s.rjust(len(num_s),'0')
    return s

s = 'foo'
print(1, s,' ', increment_string(s),'\n')
s = 'foo002'
print(1, s,' ', increment_string(s),'\n')
s = 'foobar23'
print(2, s,' ', increment_string(s),'\n')
s= 'foo0042'
print(3, s,' ', increment_string(s),'\n')
s= 'foo9'
print(4, s, increment_string(s),'\n')
