'''
Fundamentals 017
Имея список (arr) в качестве аргумента, выполните функцию countSmileys, к
оторая должна возвращать общее количество улыбающихся лиц.
Правила для улыбающегося лица:
- Каждый смайлик должен содержать действительную пару глаз. Глаза могут быть отмечены как: или ;
- У смайлика может быть нос, но это не обязательно.
  Допустимые символы для носа: - или ~
- Каждое улыбающееся лицо должно иметь улыбающийся рот,
который должен быть отмечен либо ), либо D.
Никакие дополнительные символы, кроме упомянутых, не допускаются.

countSmileys([':)', ';(', ';}', ':-D']);       // should return 2;
countSmileys([';D', ':-(', ':-)', ';~)']);     // should return 3;
countSmileys([';]', ':[', ';*', ':$', ';-D']); // should return 1;'''

def count_smileys(llst:list)->int:
    num = 0
    for s in llst:
        glaz = (s.find(':') !=-1) or (s.find(';') !=-1)
        rot = (s.find(')') !=-1) or (s.find('D') !=-1)
        issmiley = glaz and rot
        if issmiley: num += 1
    return num
def thetest_count_smileys()->None:
    print('result = ', count_smileys([]))
    print('result = ', count_smileys([':D',':~)',';~D',':)']))
    print('result = ', count_smileys([':)',':(',':D',':O',':;']))
    print('result = ', count_smileys([';]', ':[', ';*', ':$', ';-D']))
    print('result = ', count_smileys([';D', ':-(', ':-)', ';~)']))

if __name__ == "__main__":
    thetest_count_smileys()
