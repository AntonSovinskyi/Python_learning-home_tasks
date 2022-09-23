""" A program to get the largest number from a list
 of random numbers with the length of 10


 """


import random


num = []
n = 10
while len(num) < n:
    num.append(random.randint(1, 1000))

max_item = max(num)
print(max_item)