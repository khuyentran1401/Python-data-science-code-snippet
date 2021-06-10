variable_1 = 'a'
variable_2 = 'b'
variable_3 = 'c'

print(eval('variable_1'))
# a

variables = [eval(f'variable_{i}') for i in range(1, 4)]
print(variables)
# ['a', 'b', 'c']