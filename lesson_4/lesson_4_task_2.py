'''Cheking if the phone number is correct'''

# В прикладі №1, рішення дає необхідний результат, але мені здалося,
# що можна зробити тиндітніше.
# Таке рішення в прикладі №2. Проте, чомусь программа вважати номер правильним
# коли в ньому 9 чисел, а не 10 чисел. Не можу зрозуміти чому?

# Приклад №1

phone_number = input("Please, enter phone number: ")
if phone_number.isdigit():
    if len(phone_number) == 10:
        print('The number is correct.')
    else:
        print('The number is incorrect.')
else:
    print('The number is incorrect.')

# Приклад №2

phone_number = input("Please, enter phone number: ")
if phone_number.isdigit() + len(phone_number) == 10:
    print('The number is correct.')
else:
    print('The number is incorrect.')