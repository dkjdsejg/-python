# # задача 14
# R = float(input())
# S = 3.14 * (R ** 2)
# H = float(input())
# V = S * H
# p = 1000
# print(round((p * V), 2))


# # задача 15
# numbers = input()
# numbers_mas = numbers.split(', ')
# res = 1
# for num in numbers_mas:
#     res *= int(num)
# print(res)


# # задача 9
# enemies = ['Екатерина', 'Артём', 'Никита', 'Илья', 'Евгений', 'Варвара', 'Вероника', 'Юлия', 'София', 'Константин', 'Владислав', 'Владимир', 'Иван', 'Матвей', 'Даниил', 'Ангелина', 'Егор', 'Вадим', 'Олег']
# enemies_names = []

# def sort_names(names):
#     for name in names:
#         if name in enemies != 0:
#             enemies_names.append(name)
#     for name in enemies_names:
#         names.remove(name)
#     return names

# names = input('Введите имена через запятую: ').split(', ')
# print(sort_names(names))


# # задача 8
# def reverse(string):
#     return string[::-1].swapcase()

# print(reverse(input()))


# # задача 21
# def median_in_massiv(massiv):
#     print(massiv)
#     if len(massiv) % 2 == 0:
#         i_median_1 = len(massiv) / 2 - 1
#         i_median_2 = len(massiv) / 2 
#         median = float(massiv[int(i_median_1)] + massiv[int(i_median_2)]) / 2
#     else:
#         median = massiv[(len(massiv) // 2)]
#     return median
        
# n_massiv = input().split(', ')
# massiv = []
# for i in range(len(n_massiv)):
#     elem = int(n_massiv[i])
#     massiv.append(elem)
# massiv = sorted(massiv)
# print(median_in_massiv(massiv))


# # задача 20
# def more(numbers):
#     for i in range(len(numbers) - 1):
#         if numbers[i] >= numbers[i + 1]:
#             return 'Числа в массиве не возрастают'
#     return 'Числа в массиве возрастают'
    
# n_massiv = input().split(', ')
# massiv = []
# for i in range(len(n_massiv)):
#     elem = int(n_massiv[i])
#     massiv.append(elem)
# print(more(massiv))


# # задача 19
# def func(massiv):
#     new_massiv = []
#     sum = 0
#     for i in range(len(massiv)):
#         elem = massiv[i] + sum
#         new_massiv.append(elem)
#         sum += massiv[i]
#     return new_massiv
    
# n_massiv = input('Запишите числа через запятую: ').split(', ')
# massiv = []
# for i in range(len(n_massiv)):
#     elem = int(n_massiv[i])
#     massiv.append(elem)
# print(func(massiv))


# # задача 17
# def coordinates(a, b):
#     one_side = abs(a['x'] - b['x'])
#     two_side = abs(a['y'] - b['y'])
#     three_side = ((one_side ** 2) + (two_side ** 2)) ** (1/2)
#     return round(three_side, 3)

# points_ax = int(input('Введите координату x точки a: '))
# points_ay = int(input('Введите координату y точки a: '))
# points_bx = int(input('Введите координату x точки b: '))
# points_by = int(input('Введите координату y точки b: '))

# a = {
#     'x': points_ax,
#     'y': points_ay
# }

# b = {
#     'x': points_bx,
#     'y': points_by
# }

# print(coordinates(a, b))


# # задача 10
# x_mas = [ 3, 45, 392, -34]
# y_mas = [ -38, 4, 45, 3]
# xy_mas = []
# for i in range(len(x_mas)):
#     xy_mas.append((x_mas[i], y_mas[i]))
# print(xy_mas)


# # задача 11
# mas = [ 'Илья', 'Иван', 'Виктор']
# for name in mas:
#     print(f'Здравствуйте, {name}')


# # задача 12
# word = input()
# for i in range(len(word) - 1):
#     if word[i] == word[i + 1]:
#         print(True)
#         break


# # задача 13
# def pr_del(string):
#     string = ' '.join(string.split())
#     return string
# string = input()
# print(pr_del(string))


# # задача 16
# def volume_res(box_param):
#     res = 0
#     for i in range(len(box_param)):
#         length, width, height = box_param[i][0], box_param[i][1], box_param[i][2]
#         volume = length * width * height
#         res += volume
#     return res

# box_param = [
#     (2, 5, 3),
#     (1, 1, 1),
#     (4, 4, 4)  
# ]
# print(volume_res(box_param))


# # задача 18
# leetspeak_dict = {
#     'A': '4',
#     'B': '8',
#     'C': '<',
#     'D': '[)',
#     'E': '3',
#     'F': '|=',
#     'G': '6',
#     'H': '#',
#     'I': '1',
#     'J': '_|',
#     'K': '|<',
#     'L': '1_',
#     'M': '/\\/\\',
#     'N': '|\\|',
#     'O': '0',
#     'P': '|>',
#     'Q': '0,',
#     'R': '|2',
#     'S': '5',
#     'T': '7',
#     'U': '|_|',
#     'V': '\\/',
#     'W': '\\/\\/',
#     'X': '><',
#     'Y': '`/',
#     'Z': '2',
#     'a': '4',
#     'b': '8',
#     'c': '<',
#     'd': '[)',
#     'e': '3',
#     'f': '|=',
#     'g': '6',
#     'h': '#',
#     'i': '1',
#     'j': '_|',
#     'k': '|<',
#     'l': '1',
#     'm': '/\\/\\',
#     'n': '|\\|',
#     'o': '0',
#     'p': '|>',
#     'q': '0,',
#     'r': '|2',
#     's': '5',
#     't': '7',
#     'u': '|_|',
#     'v': '\\/',
#     'w': '\\/\\/',
#     'x': '><',
#     'y': '`/',
#     'z': '2'
# }
# string = input()
# res_string = ''
# for i in range(len(string)):
#     if string[i].isalpha():
#         res_string += leetspeak_dict[string[i]]
#     else:
#         res_string += string[i]
# print(res_string)


# # задача 7
# key_letters = {
#     'A': 1, 'C': 3, 'E': 5, 'G': 7, 'I': 9,
#     'K': 11, 'M': 13, 'O': 15, 'Q': 17, 'S': 19,
#     'U': 21, 'W': 23, 'Y': 25
# }

# string = input()
# word = ''
# count = 1
# for i in range(len(string)):
#     if i == (len(string) - 1):
#         word += (string[i] * (count // key_letters[string[i]]))
#         count = 1
#     else:
#         if string[i] == string[i + 1]:
#             count += 1
#         else:
#             word += (string[i] * (count // key_letters[string[i]]))
#             count = 1
# print(word)