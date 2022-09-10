"""A list that contains all integers from 1 to 100,
then find all integers from the list that are divisible
by 7 but not a multiple of 5, and store them in a separate list.


"""


num_1 = []
num_2 = []

i = 1
while i < 101:
    num_1.append(i)
    i += 1

for el in num_1:
    if el % 7 == 0 and el % 5 != 0:
        num_2.append(el)

print(num_2)
