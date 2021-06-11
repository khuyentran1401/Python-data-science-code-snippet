from collections import namedtuple

Person = namedtuple("Person", "name gender")

oliver = Person("Oliver", "male")
khuyen = Person("Khuyen", "female")

print(oliver)
# Person(name='Oliver', gender='male')

print(khuyen)
# Person(name='Khuyen', gender='female')

print(oliver.name)
# Oliver
