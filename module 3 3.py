def print_params(a = 1, b = 'Строка', c = True ):
    print (a, b, c)
#1
print_params()
print_params('Собака')
print_params(4, False)
print_params(95, 'Какая-то строка', 'Еще не придумал')
print_params(b = 25)
print_params(c = [1,2,3])
#2
values_list = ['я изучаю пайтон))', [9,8,7], True]
values_dict = {'a': 5, 'b': 0, 'c': 1}
print_params(*values_list)
print_params(**values_dict)
#3
values_list2 = ['33', 1.5]
print_params(*values_list2, 42)