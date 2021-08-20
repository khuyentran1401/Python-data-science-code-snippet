nums = [1, 2, 3]
print(list(map(str, nums)))  # ['1', '2', '3']


def multiply_by_two(num: float):
    return num * 2


print(list(map(multiply_by_two, nums)))  # [2, 4, 6]
