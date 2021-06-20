from itertools import combinations
num_list = [1, 2, 3]
for i in num_list: # instead of this
    for j in num_list:
        if i != j:
            print(i, j)
""" 
1 2
1 3
2 1
2 3
3 1
3 2
"""
comb = combinations(num_list, 2) # use this
for pair in list(comb):
    print(pair)
""" 
(1, 2)
(1, 3)
(2, 3)
"""