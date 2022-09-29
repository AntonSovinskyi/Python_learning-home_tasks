"""Make a class called Person. Using methods make prints
a greeting from the person containing

"""


class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def talk(self):
        full_name = f'{self.first_name} {self.last_name}'
        print(f'Hello! My name is {full_name}. I am {self.age} years old.')


greeting = Person('Anton', 'Sovinskyi', 37)
greeting.talk()
