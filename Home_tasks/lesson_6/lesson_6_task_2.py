"""Generate 2 lists with the length of 10 with random integers
 from 1 to 10, and make a third list containing the common integers
  between the 2 initial lists without any duplicates.


  """


import random


list_1 = []
list_2 = []
list_3 =[]

n = 10
while len(list_1) < n and len(list_2) < n:
    list_1.append(random.randint(0, 10))
    list_2.append(random.randint(0, 10))

for el in list_1:
    if el in list_2:
        list_3.append(el)

list_3 = set(list_3)

print(list(list_3))