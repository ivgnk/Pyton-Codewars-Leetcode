'''
6 kyu Mexican Wave
https://www.codewars.com/kata/58f5c63f1e26ecda7e000029/train/python
wave("hello") => ["Hello", "hEllo", "heLlo", "helLo", "hellO"]
'''

def wave(people):
    if people=="": return []
    people = people.lower()

    llen = len(people)
    res = []; llst = [s for s in people]
    for i in range(llen):
       if llst[i] !=" ":
           # https://stackoverflow.com/questions/4260280/if-else-in-a-list-comprehension
           ss = ''.join([s.upper() if (i==j) and (s !=' ') else s for j,s in enumerate(llst)] )
           res.append(ss)
    return res

print(wave("Two words"))