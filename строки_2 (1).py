# # задача 5
# def shortener(st):
#     while '(' in st or ')' in st:
#         start = st.rfind('(')
#         end = st.find(')', start)
#         st = st.replace(st[start:end + 1], '')
#     return st

# print(shortener(input()))


# # задача 6
# def cleaned_str(st):
#     lst = []
#     for symbol in st:
#         if symbol == '@' and lst:
#             lst.pop()
#         elif symbol != '@':
#             lst.append(symbol)
#     return ''.join(lst)

# print(cleaned_str('гр@оо@лк@оц@ва'))