nums = [1, 2, 3, 4]
chars = ['a', 'b', 'c', 'd']

comb = list(zip(nums, chars))
print(comb)
# [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]

nums_2, chars_2 = zip(*comb)
print(nums_2, chars_2)
# (1, 2, 3, 4) ('a', 'b', 'c', 'd')