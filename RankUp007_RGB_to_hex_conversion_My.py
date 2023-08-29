'''
RankUp 007 My
Функция RGB неполная. Завершите его так, чтобы передача десятичных значений
RGB приводила к возврату шестнадцатеричного представления.
Допустимые десятичные значения для RGB: 0–255.
Любые значения, выходящие за пределы этого диапазона,
должны быть округлены до ближайшего допустимого значения.
Примечание. Ваш ответ всегда должен состоять из 6 символов
https://www.codewars.com/kata/513e08acc600c94f01000001/train/python
'''
import subprocess
import sys
from colormap import rgb2hex

# How install a Python module within code?
# https://stackoverflow.com/questions/12332975/how-can-i-install-a-python-module-within-code
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def repl(elem):
    if elem>=0 and elem <=255:
        return elem
    elif elem < 0:
        return 0
    else:
        return 255

def rgb(r:int, g:int, b:int)->str:
    nr = repl(r);   ng=repl(g);  nb=repl(b)
    # print(' = ',nr, ng, nb)
    s = rgb2hex(nr, ng, nb)
    return s[1:]

print(rgb(0, 0, 0))
print(rgb(1, 2, 3))
print(rgb(255, 255, 255))
print(rgb(254, 253, 253))
print(rgb(-20, 253, 253))


