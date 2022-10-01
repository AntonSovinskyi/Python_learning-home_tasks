"""Make a class structure in python representing people at school."""


class Person:
    def __init__(self, name, age, birth_day, gender):
        self.name = name
        self.age = age
        self.birth_day = birth_day
        self.gender = gender
        print(f"\nHello! My nane is {self.name}, I'm {self.age}. I was born {self.birth_day}, and I am {self.gender}.")


class Student(Person):
    def home_work(self):
        print('I have to be ready with my home work.')

    def test_passing(self):
        print('I have to pass tests during academic year.')

    def sport_competitions(self):
        print("I will take a part in all school sport competitions this year.")


class Teacher(Person):
    def salary(self, money):
        self.money = money
        print(f'I earn {self.money} per month.')

    def test_cheking(self):
        print('I have to check students tests.')

    def taking_exams(self):
        print('I need to take exams at the end of a year.')


s = Student('Ulyana', 6, '25/08/2016', 'female')
s.home_work()
s.test_passing()
s.sport_competitions()

t = Teacher('Anton', 37, '14/07/1985', 'male')
t.salary(3000)
t.test_cheking()
t.taking_exams()
