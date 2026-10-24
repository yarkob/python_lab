#1
user_input = input("числа через пробіл: ").split()
numbers = []

for n in user_input:
    numbers.append(int(n))


positives = []
negatives = []
evens = []
mult_of_3 = []

for num in numbers:
    if num > 0:
        positives.append(num)
    if num < 0:
        negatives.append(num)
    if num % 2 == 0:
        evens.append(num)
    if num % 3 == 0:
        mult_of_3.append(num)

if numbers:
    min_val = min(numbers)
    max_val = max(numbers)
    total_sum = sum(numbers)
    avg_val = round(total_sum / len(numbers), 2)

    print(f"Додатні: {positives}")
    print(f"Від'ємні: {negatives}")
    print(f"Парні: {evens}")
    print(f"Кратні 3: {mult_of_3}")
    print(f"Min: {min_val}; Max: {max_val}; Sum: {total_sum}; Average: {avg_val}")
else:
    print("немає чисел")

#2
input_group1 = input("перша група: ")
group1 = set(input_group1.split())

input_group2 = input("друга група: ")
group2 = set(input_group2.split())

common = group1 & group2
only_group1 = group1 - group2
only_group2 = group2 - group1
all_unique = group1 | group2

if common:
    print(f"Спільні: {', '.join(common)}")
else:
    print("Спільні: немає")

if only_group1:
    print(f"Тільки group1: {', '.join(only_group1)}")
else:
    print("Тільки group1: немає")

if only_group2:
    print(f"Тільки group2: {', '.join(only_group2)}")
else:
    print("Тільки group2: немає")

if all_unique:
    print(f"Усі: {', '.join(sorted(all_unique))}")
else:
    print("Усі: немає")

#3
catalog = {}

print("товари та їх ціни (для завершення введіть stop)")

while True:
    name = input("назва: ")
    if name.lower() == 'stop':
        break
    price = float(input(f"ціну товару {name}: "))
    catalog[name] = price

update_name = input("назва товару для додавання або оновлення ціни: ")
update_price = float(input(f"ціна {update_name}: "))
catalog[update_name] = update_price

search_name = input("назва товару для пошуку: ")
price = catalog.get(search_name)

if price:
    print(f"{search_name} {price} грн")
else:
    print(f"{search_name} не знайдено")

min_price = float(input("мінімальна ціна: "))
max_price = float(input("максимальна ціна: "))

print(f"Ціновий діапазон: {min_price}..{max_price} грн")
found_any = False

for name, price in catalog.items():
    if min_price <= price <= max_price:
        print(f"{name} — {price} грн")
        found_any = True

if not found_any:
    print("немає товарів.")

#4
group_info = ('10-IT', '2026/2027')

journal = {}

while True:
    name = input("ім'я або stop щоб зупинитись: ")

    if name.lower() == 'stop':
        break

    grades_input = input(f"5 оцінок учня {name} через пробіл: ")

    grades = [int(x) for x in grades_input.split()]

    if len(grades) == 5 and all(1 <= grade <= 12 for grade in grades):
        journal[name] = grades
        print(f"{name} додано\n")
    else:
        print("учень повинен мати 5 оцінок у діапазоні від 1 до 12\n")

print(f"{group_info[0]} — {group_info[1]}")

for name, grades in journal.items():
    average = sum(grades) / len(grades)
    print(f"{name} — {average}")

if journal:
    ranking_list = []
    for name, grades in journal.items():
        average = sum(grades) / len(grades)
        ranking_list.append((average, name, grades))

    ranking_list.sort(reverse=True)

    best_average, best_name, best_grades = ranking_list[0]
    print(f"Найкращий результат: {best_name} — {best_average}")
else:
    print("немає учнів")
