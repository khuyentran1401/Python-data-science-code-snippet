# Instead of this 
l1 = [1, 2, 3]
l2 = l1 
l2.append(4)
print(l2)
# [1, 2, 3, 4]

print(l1)
# [1, 2, 3, 4]

# Do this
l1 = [1, 2, 3]
l2 = l1.copy()
l2.append(4)
print(l1)
# [1, 2, 3]