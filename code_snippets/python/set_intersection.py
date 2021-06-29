requirement1 = ['pandas', 'numpy', 'statsmodel']
requirement2 = ['numpy', 'statsmodel', 'sympy', 'matplotlib']

intersection = set.intersection(set(requirement1), set(requirement2))
print(list(intersection))