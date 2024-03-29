# Lambda expressions
from functools import reduce

#lambda param: action(param)

my_list = [1,2,3]

def multiply_by2(item):
    return item * 2

def only_odd(item):
    return item % 2 != 0

def accumulator(acc, item):
    print(acc, item)
    
    return acc + item

print(f'\n')
# similar to const item = (item) => item * 2
print(f'list(map(lambda item: item * 2, my_list))')
print(list(map(lambda item: item * 2, my_list)))

print(f'\n')
print(f'list(filter(lambda item: item % 2 != 0, my_list))')
print(list(filter(lambda item: item % 2 != 0, my_list)))

print(f'\n')
print(f'print(reduce(lambda acc, item: acc + item, my_list))')
print(reduce(lambda acc, item: acc + item, my_list))
