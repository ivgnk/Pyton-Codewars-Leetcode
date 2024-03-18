'''
Питон. Как вывести ключ по его значению в словаре?
https://otvet.mail.ru/question/230489205
'''
stats = {'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}
print(stats)
stats = dict(map(reversed, stats.items()))
print(stats)