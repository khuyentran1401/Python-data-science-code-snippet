from abc import ABC, abstractmethod 

class Animal(ABC):

    def __init__(self, name: str):
        self.name = name 
        super().__init__()

    @abstractmethod 
    def make_sound(self):
        pass 

class Dog(Animal):
    def make_sound(self):
        print(f'{self.name} says: Woof')

class Cat(Animal):
    def make_sound(self):
        print(f'{self.name} says: Meows')

Dog('Pepper').make_sound()
Cat('Bella').make_sound()