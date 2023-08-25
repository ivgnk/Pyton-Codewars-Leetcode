'''
RankUp 005
parseInt() reloaded
преобразовать строку (английскую) в целое число
https://www.codewars.com/kata/525c7c5ab6aecef16e0001a5/train/python

1) Ищем готовую функции и пакет для преобразования
https://pypi.org/project/word2number/
2) устанавливаем пакет в программе
3) делаем предваарительную проверку установлен ли ли пакет
'''
import subprocess
import sys
import importlib.util

# How install a Python module within code?
# https://stackoverflow.com/questions/12332975/how-can-i-install-a-python-module-within-code
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# How to check if a Python module exists without importing it
# https://stackoverflow.com/questions/14050281/how-to-check-if-a-python-module-exists-without-importing-it
llib_name = "word2number"
llib = importlib.util.find_spec(llib_name)
ffound = llib is not None
if not ffound:
    install(llib_name)
else:
    print('installed '+llib_name)

# https://pypi.org/project/word2number/
from word2number import w2n

def parse_int(s:str):
    return w2n.word_to_num(s)

print(parse_int('one'))
print(parse_int('twenty'))
print(parse_int('two hundred forty-six'))

'''
import subprocess
import sys
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

install('word2number')    
    
from word2number import w2n

def parse_int(s:str):
    return w2n.word_to_num(s)
'''