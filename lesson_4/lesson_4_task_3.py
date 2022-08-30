"""Answer for a mathematical expression"""


a, b, c = 2, 3, 2
d = (a + b) ** c
user = input('Enter the result of a mathematical expression: ')
if int(user) != d:
    print(f'{user} is incorrect. Have a cup of tea, an try again later.')
else:
    print(f'Are you doctor of sciences? {user} is correct answer!')