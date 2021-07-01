class Fruit:
    def __init__(self, name: str, color: str):
        self._name = name 
        self._color = color
        
    @property
    def color(self):
        print("The color of the fruit is:")
        return self._color 
    
    @color.setter
    def color(self, value):
        print("Setting value of color...")
        if self._color is None:
            if not isinstance(value, str):
                raise ValueError('color must be of type string')
            self.color = value 
        else:
            raise AttributeError("Sorry, you cannot change a fruit's color!")
        
fruit = Fruit('apple', 'red')
print(fruit.color)    
fruit.color = 'yellow'
