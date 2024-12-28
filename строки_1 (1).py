# задача 1
# def search_substr(subst, st):
#     if (subst in st) == True:
#         return 'Есть контакт!'
#     else:
#         return 'Мимо!'
# print(search_substr(input(), input()))


# задача 2
# def first_last(letter, st):
#     if (letter in st) == True:
#         return (st.find(letter), st.rfind(letter))
#     else:
#         return (None, None)
# print(first_last(input(), input()))


# задача 3
# from collections import Counter
# def top3(st):
#     res = Counter(st.replace(' ', '')).most_common(3)
#     if len(res) >= 3:
#         return f'{res[0][0]} - {res[0][1]}, {res[1][0]} - {res[1][1]}, {res[2][0]} - {res[2][1]}'
#     elif len(res) == 2:
#         return f'{res[0][0]} - {res[0][1]}, {res[1][0]} - {res[1][1]}'
#     elif len(res) == 1:
#         return f'{res[0][0]} - {res[0][1]}'
# print(top3(input()))


# задача 4
# def camel(st):
#     res_st = ''
#     index = 0
#     for i in st:
#         if i.isalpha() == True:
#             if index % 2 == 0:
#                 res_st += i.lower()
#                 index += 1
#             elif index % 2 != 0:
#                 res_st += i.upper()
#                 index += 1
#         else:
#             res_st += i
#     return res_st
# print(camel(input()))