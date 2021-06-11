class Food:
    def __init__(self, name: str, color: str):
        self.name = name 
        self.color = color 

apple = Food('apple', 'red')

print("The color of apple is", getattr(apple, 'color', 'yellow'))
# The color of apple is red

print("The flavor of apple is", getattr(apple, 'flavor', 'sweet'))
# The flavor of apple is sweet

print("The flavor of apple is", apple.sweet)
# AttributeError: 'Food' object has no attribute 'sweet'