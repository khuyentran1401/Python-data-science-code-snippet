from box import Box

food_box = Box({"food": {"fruit": {"name": "apple", "flavor": "sweet"}}})

print(food_box)
# {'food': {'fruit': {'name': 'apple', 'flavor': 'sweet'}}}

print(food_box.food.fruit.name)
# apple
