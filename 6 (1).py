# # задача 1
# def to_dict(lst):
#     return {element: element for element in lst}
    
# print(to_dict([0, 13.55, -10, '34', True]))


# # задача 2
# my_dict = {'first_one': 'we can do it'}
# def biggest_dict(**kwargs):
#     my_dict.update(**kwargs)
    
# biggest_dict(a=1, b=3)
# biggest_dict(c=5, s=True)
# biggest_dict(color='blue')
# print(my_dict)


# # задача 3
# from collections import Counter

# def count_it(sequence):
#     return dict(Counter([int(num) for num in sequence]).most_common(3))

# print(count_it(input()))


# # задача 4
# dct = {1: 1, 0: 2, 5: 3, 4: 4, 6: 7}

# list(dct.items())[0], list(dct.items())[-1] = list(dct.items())[-1], list(dct.items())[0]

# elem_2 = list(dct.items())[1]
# del dct[elem_2[0]]

# dct['new_key'] = 'new_value'
# print(dct.items())