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