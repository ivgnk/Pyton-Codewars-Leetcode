'''
RankUp 006
Напишите функцию, которая при задании URL-адреса в виде строки анализирует только имя домена и возвращает его в виде строки.
Например
url = "http://github.com/carbonfive/raygun" -> domain name = "github"
url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
url = "https://www.cnet.com"                -> domain name = cnet"
https://www.codewars.com/kata/514a024011ea4fb54200004b/train/python
'''

# import tldextract
# def domain_name1(url:str)->str:
#     ext = tldextract.extract(url)
#     return ext.domain


def domain_name(url:str)->str:
    s = url.replace('http://','')
    s = s.replace('https://','')
    s = s.replace('www.','')
    res = s.split('.')
    return res[0]

def thetest_domain_name()->None:
    # '-6,-3-1,3-5,7-11,14,15,17-20'
    print('result = ', domain_name("http://google.com"))
    print('result = ', domain_name("http://google.co.jp"))
    print('result = ', domain_name("www.xakep.ru"))
    print('result = ', domain_name("https://youtube.com"))

if __name__ == "__main__":
    thetest_domain_name()