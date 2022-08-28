"""Printing OH by using one and multiple print() with adding '\n' and '\t' symbols"""


print(str('#') * 9 + "\n" + ("#\t\t#\n") * 3 + str('#') * 9 + "\n")
print(("#\t\t#\n")*2 + str('#') * 9 + "\n" + ("#\t\t#\n")*2)

# В мене питання, чому якщо використовувати коми замість плюсів, додаються зайві пробіли?