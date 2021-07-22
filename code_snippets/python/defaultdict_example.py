from collections import defaultdict

# Instead of this
food_price = {'apple': [], 'orange': []}

# Use this
food_price = defaultdict(list)

for i in range(1, 4):
    food_price['apple'].append(i)
    food_price['orange'].append(i)    

print(food_price.items()) 
# dict_items([('apple', [1, 2, 3]), ('orange', [1, 2, 3])])
