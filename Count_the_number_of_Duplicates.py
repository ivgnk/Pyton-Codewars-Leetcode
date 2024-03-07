
def duplicate_count(text):
    text = text.lower()
    the_set=set(text)
    the_dict = {el:0 for el in the_set}
    # print(the_set);  print(the_dict)
    for el in text:
       the_dict[el]=the_dict[el]+1
    # print(the_dict)
    sum = 0
    for el in the_set:
       if the_dict[el]>1: sum = sum+1
    return sum

# 3 goog decision in codewars
# def duplicate_count(text):
#     count = 0
#     for c in set(text.lower()):
#         if text.lower().count(c) > 1:
#             count += 1
#     return count



# print(duplicate_count("abcde"))
# print(duplicate_count("abcdeaa"))
print(duplicate_count("abcdeaB"))
# print(duplicate_count("Indivisibilities"))
# print(duplicate_count("aA11"))
# print(duplicate_count("ABBA"))
# print(duplicate_count(""))