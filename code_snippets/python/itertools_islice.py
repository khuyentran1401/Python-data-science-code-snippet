from itertools import islice

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_a = list(islice(a, 1, 7, 2))
print(new_a)
