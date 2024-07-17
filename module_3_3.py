def print_params(a = 1, b = 'stroka', c = True):
    print(a, b, c)
values_list = [2, 'spisok', True]
values_dict = {'a': 3, 'b': 'slovarik', 'c': True}
values_list_2 = [4, 'wow']
print_params()
print_params('lol')
print_params(20, 'noob')
print_params(b = 25)
print_params(c = [1,2,3])
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)

