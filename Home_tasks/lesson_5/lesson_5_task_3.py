""" A program that reads an input string and then creates
and prints 5 random strings from characters of the input string."""


import random

your_string = input('Give me a word and I will play with it: ')
prog_string = list(your_string)
new_word = []

for _ in range(len(prog_string)):
    random.shuffle(prog_string)
    new_word.append(prog_string.copy())

for word in new_word:
    print(''.join(word))
