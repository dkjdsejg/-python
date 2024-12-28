# задача 1
# massiv = [1, 2, 3, 4]
# print(massiv[::-1])


# задача 2
# list = [2, 4, 3, 4, 23, 0]

# def change(list):
#     list[0], list[-1] = list[-1], list[0]
#     return(list)

# print(change(list))


# задача 3
# def to_list(*args):
#     return(args)

# print(to_list([1, 2], 45, True, '2'))

# задача 4
# def useless(s):
#     return max(s) / len(s)

# s = [1, 5, 98, 45]
# print(useless(s))


# задача 5
# def list_sort(lst):
#     lst.sort(key = None, reverse = True)
#     return lst

# lst = [1, 5, 3, -6, 0, 34, 34]    
# print(list_sort(lst))


# задача 6
true_lst = []

def all_eq(lst):
    max_string = ''
    for string in lst:
        if len(string) > len(max_string):
            max_string = string
    len_m_s = len(max_string)
    for string in lst:
        string += ('_' * (len_m_s - len(string)))
        true_lst.append(string)
    return true_lst

print(all_eq(['ab', 'abcd', 'abcdef']))





