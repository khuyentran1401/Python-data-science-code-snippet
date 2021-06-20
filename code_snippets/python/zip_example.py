l = [1, 2, 3, 4]
string = 'abcd'
combinations = list(zip(l, string))
for comb in combinations:
    print(comb)

""" 
(1, 'a')
(2, 'b')
(3, 'c')
(4, 'd')
"""