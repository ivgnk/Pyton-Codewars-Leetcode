'''
RankUp 002
Команда маркетологов тратит слишком много времени на ввод хэштегов.
Давайте поможем им с помощью нашего собственного генератора хэштегов!

Вот в чем дело:
Оно должно начинаться с хэштега (#).
Первая буква всех слов должна быть написана с заглавной буквы.
Если конечный результат длиннее 140 символов, он должен возвращать значение false.
Если входными данными или результатом является пустая строка, она должна возвращать значение false.
Примеры
" Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
"    Hello     World   "                  =>  "#HelloWorld"
""                                        =>  false
https://www.codewars.com/kata/52449b062fb80683ec000024/train/python
'''

def generate_hashtag(s:str)-> str | bool:
    s = s.strip()
    if s == '':
        return False
    else:
        s = s.lower()
        s = s.title()
        s = s.replace(' ','')
        if len(s)<140:
            return '#'+s
        else:
            return False

def thetest_generate_hashtag()->None:
    list_of_tests = [" Hello there thanks for trying my Kata", " Hello there thanks for trying my Kata", "" , ' ',
                     'Codewars', '      Codewars', 'Codewars Is Nice', 'codewars is nice', 'CoDeWaRs is niCe',
                     'c i n', 'codewars  is  nice']
    for s in list_of_tests:
        print('result = ', generate_hashtag(s))

if __name__ == "__main__":
    thetest_generate_hashtag()