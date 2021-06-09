# pip install faker
from faker import Faker

fake = Faker()

print(fake.color_name())

print(fake.name())

print(fake.address())

print(fake.date_of_birth(minimum_age=22))

print(fake.city())

print(fake.job())
