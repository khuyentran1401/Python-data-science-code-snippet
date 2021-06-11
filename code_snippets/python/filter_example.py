def get_fruit(val: str):
    fruits = ['apple', 'orange', 'grape']
    if val in fruits:
        return True 
    else:
        return False 

items = ['chair', 'apple', 'water', 'table', 'orange']
fruits = filter(get_fruit, items)
print(list(fruits))