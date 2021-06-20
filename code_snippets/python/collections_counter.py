from collections import Counter

char_list = ['a', 'b', 'c', 'a', 'd', 'b', 'b']

# Instead of this
custom_counter = {}
for char in char_list:
    if char not in custom_counter:
        custom_counter[char] = 1
    else:
        custom_counter[char] += 1

print(custom_counter)
# {'a': 2, 'b': 3, 'c': 1, 'd': 1}

# Use this
print(Counter(char_list))
# Counter({'b': 3, 'a': 2, 'c': 1, 'd': 1})