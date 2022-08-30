"""Cheking if the phone number is correct"""


phone_number = input("Please, enter phone number: ")
if phone_number.isdigit():
    if len(phone_number) != 10:
        print('The correct number must be 10 digits.')
    else:
        print(f'{phone_number} is correct.')
else:
    print('The number must contain only digits.')