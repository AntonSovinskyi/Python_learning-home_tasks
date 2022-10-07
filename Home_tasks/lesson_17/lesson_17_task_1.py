"""Create a base class named Animal with a method called talk
and then create two subclasses: Dog and Cat, and make their own
implementation of the method talk be different. For instance,
Dog’s can be to print ‘woof woof’, while Cat’s can be to print ‘meow’.

"""


def animal_talk(animal):
    print(animal.talk())


class Animal:
    def talk(self):
        pass


class Cat(Animal):
    def talk(self):
        return 'Cats say meow'


class Dog(Animal):
    def talk(self):
        return 'Dogs say woof woof'


cat = Cat()
dog = Dog()

animal_talk(cat)
animal_talk(dog)
