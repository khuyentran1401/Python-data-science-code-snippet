class Food:
    def __init__(self, name: str, color: str):
        self.name = name 
        self.color = color

    def __str__(self):
        return f'{self.color} {self.name}'

    def __repr__(self):
        return f'Food({self.color}, {self.name})'

food = Food('apple', 'red')

print(food) #  str__

print(repr(food)) #__repr__
