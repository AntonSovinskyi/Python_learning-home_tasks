"""Write a Python program to access a function inside a function
(Tips: use function, which returns another function)

"""


command = input('Введіть команду: ')


def copy():
    print('Копіювати')


def cut():
    print('Вирізати')


def paste():
    print('Вставити')


def choose(word):
    word_dict = {
        'copy': copy,
        'cut': cut,
        'paste': paste,
    }

    if word in word_dict:
        return word_dict[word]


try:
    choose(command)()
except TypeError:
    print('Wrong command')
