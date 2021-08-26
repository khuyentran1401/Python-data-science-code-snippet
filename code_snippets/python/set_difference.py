a = [1, 2, 3, 4]
b = [1, 3, 4, 5, 6]

# Find elements in a but not in b
diff = set(a).difference(set(b))
print(list(diff))  # [2]

# Find elements in b but not in a
diff = set(b).difference(set(a))
print(list(diff))  # [5, 6]
