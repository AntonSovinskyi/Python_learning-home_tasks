"""1.Створити лист із днями тижня.

2. В один рядок (ну або як завжди) створити словник виду: {1: “Monday”, 2:...
3. Також в один рядок або як вдасться створити зворотний словник {“Monday”: 1,...

"""


days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

num_day = {num + 1: day for num, day in enumerate(days)}
print(num_day)

day_num = {day: num for num, day in num_day.items()}
print(day_num)

# -------------------------------------------------------------------------------

# Варіант "як завжди"

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

num_day = {}

for num, day in enumerate(days):
    num_day[num + 1] = day

print(num_day)

day_num = {}
for k, v in num_day.items():
    day_num[v] = k

print(day_num)
