# задача 1
# def to_float(num):
#     if type(num) is int or type(num) is float:
#         return float(num)
#     return 'Невозможно преобразовать'

# print(to_float(2))
# print(to_float('2'))
# print(to_float(True))
# print(to_float(3.4))


# задача 2
# def avg_5(a, b, c, d):
#     return round(((a + b + c + d) / 4), 5) 
# a, b, c, d = float(input()), float(input()), float(input()), float(input())
# print(avg_5(a, b, c, d))


# задача 3
# def mul_to_int(a, b):
#     if ((a * b) % int(a * b)) >= 0.5:
#         return a * b
#     else:
#         return int(a * b)
# print(mul_to_int(float(input()), float(input())))


# задача 4
# def rad(X):
#     r = ((3 * X) / (4 * π)) ** (1/3)
#     return r
# X = float(input()) # V (объём)
# π = 3.14159265358980 
# print(rad(X))
