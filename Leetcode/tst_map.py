"""
Done 07.05.2023. Test map & labda
2016_Python 3 и PyQt 5. Разработка приложений_Прохоренок.pdf, p.150
"""

r=list(range(15))
r2=list(map(lambda x: x+10, r))
print(r)
r[4:]=list(map(lambda x: x+10, r[4:]))
print(r)
