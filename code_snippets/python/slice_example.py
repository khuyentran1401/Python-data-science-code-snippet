data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Instead of this
some_sum = sum(data[:8]) * sum(data[8:])

# do this
JANUARY = slice(0, 8)
FEBRUARY = slice(8, len(data))
some_sum = sum(data[JANUARY] * sum(data[FEBRUARY]))
print(some_sum) 
# 684