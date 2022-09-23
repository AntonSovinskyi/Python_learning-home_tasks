"""Checking if my input is equal to the stored name."""


my_name = "anton"
name_check = input('Input name, please: ')
if name_check.lower() == my_name:
    print('This is correct.')
else:
    print('No, that is wrong.')
