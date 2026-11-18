#1
# import math
#
# radius = float(input("радіус: "))
# a = float(input("перший катет: "))
# b = float(input("другий катет: "))
# items = int(input("предметів: "))
# capacity = int(input("в упаковці: "))
#
# area = round(math.pi * radius ** 2, 2)
# hypotenuse = round(math.sqrt(a ** 2 + b ** 2), 2)
# packages = math.ceil(items / capacity)
#
# print("площа круга:", area)
# print("гіпотенуза:", hypotenuse)
# print("потрібно упаковок:", packages)

#2
# import random
# import statistics
#
# n = int(input("кількість оцінок: "))
#
# if n <= 0:
#     print("число більше за 0")
# else:
#     grades = []
#     high_grades = 0
#
#     for i in range(n):
#         grade = random.randint(1, 12)
#         grades.append(grade)
#
#         if grade >= 10:
#             high_grades += 1
#
#     print("оцінки:", grades)
#     print("min:", min(grades))
#     print("max:", max(grades))
#     print("середнє:", statistics.mean(grades))
#     print("медіана:", statistics.median(grades))
#     print("оцінок 10–12:", high_grades)

#3
from datetime import date

year = int(input("рік: "))
month = int(input("місяць: "))
day = int(input("день: "))

event = date(year, month, day)
today = date.today()
days = (event - today).days

if days > 0:
    print("до події залишилося:", days, "днів")
elif days < 0:
    print("після події минуло:", -days, "днів")
else:
    print("подія сьогодні")
