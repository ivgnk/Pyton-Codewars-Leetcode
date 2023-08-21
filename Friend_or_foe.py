'''
Создайте программу, которая фильтрует список строк и возвращает список, содержащий только имена ваших друзей.
Если в имени ровно 4 буквы, вы можете быть уверены, что это должен быть ваш друг! В противном случае,
вы можете быть уверены, что это не так...
Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]
'''

def friend(llst:list)->list:
    out_list = []
    for name in llst:
        if len(name) == 4:
            print(name)
            out_list.append(name)
    return out_list

def thetest_friend()->None:
    s = ["Ryan", "Kieran", "Jason", "Yous"]
    print('friend = ', friend(s))

if __name__ == "__main__":
    thetest_friend()