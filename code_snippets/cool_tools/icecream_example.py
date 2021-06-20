from icecream import ic

def plus_one(num):
    return num + 1

# Instead of this
print('output of plus_on with num = 1:', plus_one(1))
print('output of plus_on with num = 2:', plus_one(2))

# Use this
ic(plus_one(1))
ic(plus_one(2))

# One your terminal
"""
$ python icecream_example. py
output of plus_on with num = 1: 2
output of plus_on with num = 2: 3
ic| plus_one(1): 2
ic| plus_one(2): 3
"""