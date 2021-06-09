sample_range = (2, 5)
sample_range2 = (3, 7)

# With *
print(list(range(*sample_range)))
print(list(range(*sample_range2)))
"""
[2, 3, 4]
[3, 4, 5, 6]
"""

# Without *
print(list(range(sample_range)))
"""
Traceback (most recent call last):
  File "code_snippets/python/args_example.py", line 9, in <module>
    print(list(range(sample_range)))
TypeError: 'tuple' object cannot be interpreted as an integer
"""


