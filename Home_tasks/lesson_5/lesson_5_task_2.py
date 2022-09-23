"""A program that takes my name and age as input,
and greets me with the following.
"""


name = input('Enter your name: ')
age = int(input('Enter your age: '))
print(f"Hello {name.title()}, on your next birthday you will be {age + 1}!")