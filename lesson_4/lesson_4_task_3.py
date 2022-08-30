"""Answer for a mathematical expression"""


a, b, c = 2, 3, 2
d = (a + b) ** c
answer = input('Enter the result of a mathematical expression: ')
if int(answer) != d:
    print(f'{answer} is incorrect. Have a cup of tea, an try again later.')
else:
    print(f'Are you doctor of sciences? {answer} is correct answer!')