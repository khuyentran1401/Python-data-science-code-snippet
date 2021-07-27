# Add a list to a list
a = [1, 2, 3, 4]
a.append([5, 6])
print(a)  # [1, 2, 3, 4, [5, 6]]


a = [1, 2, 3, 4]
a.extend([5, 6])

print(a)  # [1, 2, 3, 4, 5, 6]
