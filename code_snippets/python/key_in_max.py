birth_year = {"Ben": 1997, "Alex": 2000, "Oliver": 1995}

print(max(birth_year))
# Oliver

max_val = max(birth_year, key=lambda k: birth_year[k])
print(max_val)
# Alex