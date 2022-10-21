"""Write a program that reads in a sequence of characters,
and determines whether it's parentheses, braces, and curly
brackets are 'balanced'.

"""


sequence = input("Enter a sequence of characters using parentheses, braces, and curly brackets: ")

stack = []
check = True

for i in sequence:
    if i in '([{':
        stack.append(i)
    elif i in ')]}':
        if len(stack) == 0:
            check = False
            break

        el = stack.pop()
        if el == '(' and i == ')':
            continue
        if el == '[' and i == ']':
            continue
        if el == '{' and i == '}':
            continue

        check = False
        break

if check and len(stack) == 0:
    print('Check is successful.')
else:
    print('Check is failed.')
