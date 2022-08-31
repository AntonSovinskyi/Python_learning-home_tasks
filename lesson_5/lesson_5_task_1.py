"""Guess the number game."""


import random

number = random.randint(1, 10)
print("Guess the number!\nIf you wat to quit, press 'q'.")
while True:
    guess_number = input('Enter a digit: ')
    if guess_number == 'q':
        break
    guess_number = int(guess_number)
    if guess_number < number:
        print('Noup. The number is bigger.')
    if guess_number > number:
        print('Noup. The number is less.')
    if guess_number == number:
        print(f'Correct, the number is {number}.')
        break
