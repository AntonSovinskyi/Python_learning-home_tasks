# number = input('Введіть число ')
# number_list = list(number)
# i = 0
# sum_ = 0
# while i < len(number_list):
#     sum_ += int(number_list[i])
#     i += 1
# print(sum_)

while True:
    number = input('Введіть число: ')
    i, sum_ = 0, 0
    if number == 'exit':
        break
    while i < len(number):
        if number[i].isdigit():
            sum_ += int(number[i])
        else:
            i += 1
            continue
        i += 1
    print(f'Сума чисел рядка {number} рівна {sum_}')