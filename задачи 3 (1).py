# задача 1
# def play(one, two):
#     if one == two:
#         return 'Ничья'
#     if one == 'камень' and two == 'ножницы':
#         return ('Первый игрок победил')
#     if one == 'ножницы' and two == 'камень':
#         return ('Второй игрок победил')
#     if one == 'камень' and two == 'бумага':
#         return ('Второй игрок победил')
#     if one == 'бумага' and two == 'камень':
#         return ('Первый игрок победил')
#     if one == 'бумага' and two == 'ножницы':
#         return ('Второй игрок победил')
#     if one == 'ножницы' and two == 'бумага':
#         return ('Первый игрок победил')

# player_1 = input('Знак первого игрока: ')
# player_2 = input('Знак второго игрока: ')
# print(play(player_1, player_2))


# # задача 2
# string = input()
# string = string[::-1]
# del_massiv = []
# del_string = '' 

# if string[0] == '!':
#     for i in range(len(string)):
#         if string[i] == '!':
#             del_string += string[i]
#         if string[i + 1].isalpha():
#             break
        
#     string = string.replace(del_string, '!')
    
# if string[0] == '?':
#     for i in range(len(string)):
#         if string[i] == '?':
#             del_string += string[i]
#         if string[i + 1].isalpha():
#             break
        
#     string = string.replace(del_string, '?')
    
# print(string[::-1])


# задача 5
# def plus_letter(string):
#     for i in range(len(string)):
#         if string[i].isalpha():
#             if (i + 1) == len(string):
#                 if string[i].isalpha():
#                     print(False)
#                 break
#             else:
#                 if string[i - 1] != '+' and string[i + 1] != '+':
#                     print(False)

# string = input()
# print(plus_letter(string))


# задача 7
# def password_check(password):
#     mark = 0

#     # условие 1: длина пароля не менее 8 символов
#     if len(password) >= 8:
#         mark += 1

#     # условие 2: есть хотя бы одна буква верхнего регистра
#     if any(char.isupper() for char in password):
#         mark += 1

#     # условие 3: есть хотя бы одна буква нижнего регистра
#     if any(char.islower() for char in password):
#         mark += 1

#     # условие 4: есть хотя бы одна цифра
#     if any(char.isdigit() for char in password):
#         mark += 1
        
#     # условие 5: Пароль не должен содержать пробелов
#     if " " not in password:
#         mark += 1

#     return mark

# password = "Pa_ssw0rd123"
# res = password_check(password)
# print(f"Сложность пароля: {res} из 5")


# # задача 8
# def num_to_text(num):
#     units = {
#         0: 'ноль', 1: 'один', 2: 'два', 3: 'три', 4: 'четыре',
#         5: 'пять', 6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять'
#     }
    
#     teens = {
#         10: 'десять', 11: 'одиннадцать', 12: 'двенадцать', 13: 'тринадцать',
#         14: 'четырнадцать', 15: 'пятнадцать', 16: 'шестнадцать', 
#         17: 'семнадцать', 18: 'восемнадцать', 19: 'девятнадцать'
#     }
    
#     tens = {
#         20: 'двадцать', 30: 'тридцать', 40: 'сорок', 50: 'пятьдесят',
#         60: 'шестьдесят', 70: 'семьдесят', 80: 'восемьдесят', 90: 'девяносто'
#     }
    
#     hundreds = {
#         100: 'сто', 200: 'двести', 300: 'триста', 400: 'четыреста',
#         500: 'пятьсот', 600: 'шестьсот', 700: 'семьсот', 800: 'восемьсот', 
#         900: 'девятьсот'
#     }
    
#     if num == 0:
#         return units[0]
    
#     result = []
    
#     if 999 >= num >= 100:
#         h = (num // 100) * 100
#         result.append(hundreds[h])
#         num %= 100
    
#     if 10 <= num <= 19:
#         result.append(teens[num])
#         num = 0
#     elif 99 >= num >= 20:
#         t = (num // 10) * 10
#         result.append(tens[t])
#         num %= 10
    
#     if 9 >= num > 0:
#         result.append(units[num])
    
#     return ' '.join(result)

# num = int(input())
# print(num_to_text(num))


# # задача 6
# def times(time):
#     hours = int(time.split(':')[0])
#     minutes = time.split(':')[1][0:2]
#     if time.endswith('am'):
#         return f"{hours - 12}:{minutes}"
#     elif time.endswith('pm'):
#         return f"{hours + 12}:{minutes}"
#     elif hours > 12:
#         return f"{hours - 12}:{minutes} pm"
#     else:
#         return f"{hours}:{minutes} am"
# print(times(input('Введите время в формате "4:00 pm", или "12:00 am": ')))


# # задача 3
# def black_jack(cards):
#     count = {x : x for x in range(2, 11)}
#     # В – валет, Д – дама, К – король, Т – туз
#     count['В'] = 10
#     count['Д'] = 10
#     count['К'] = 10
#     count['Т'] = 1
#     sum = 0
#     for card in cards:
#         sum += count[card]
#     return sum > 21
# print(black_jack([2, "К", "В"]))


# # задача 10
# def coins_and_kids(coins):
#     count_1 = 0
#     count_2 = 0
#     count_5 = 0
#     count_10 = 0
#     for coin in coins:
#         if coin == 1:
#             count_1 += coin
#         elif coin == 2:
#             count_2 += coin
#         elif coin == 5:
#             count_5 += coin
#         elif coin == 10:
#             count_10 += coin
#     if (count_1 % 3 == 0) and (count_2 % 3 == 0) and (count_5 % 3 == 0) and (count_10 % 3 == 0):
#         return ('Монеты можно распределить поровну')
#     else:
#         return ('Монеты нельзя распределить поровну')
# coins = [1, 1, 10, 2, 1, 10, 5, 5, 2, 5, 1, 1, 10, 5, 5, 10]
# print(coins_and_kids(coins))