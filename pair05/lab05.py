#1
def circle_area(radius):
    pi = 3.14159
    return pi * (radius ** 2)

def rectangle_area(width, height):
    return width * height

def triangle_area(base, height):
    return 0.5 * base * height

def main():
    choice = input("фігура: ")

    if choice == 'круг':
        r = int(input("радіус: "))
        print(f"площа круга: {circle_area(r)}")
    elif choice == 'прямокутник':
        width = int(input("ширина: "))
        height = int(input("висота: "))
        print(f"площа прямокутника: {rectangle_area(width, height)}")
    elif choice == 'трикутник':
        base = int(input("основа: "))
        height = int(input("висота: "))
        print(f"площа трикутника: {triangle_area(base, height)}")
    else:
        print("фігури не існує")

main()

#2
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def divisors(n):
    return [i for i in range(1, n + 1) if n % i == 0]

def digit_sum(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

def main():
    n = int(input("N = "))

    if is_prime(n):
        prime_result = "так"
    else:
        prime_result = "ні"

    divs = divisors(n)
    d_sum = digit_sum(n)

    print(f"Просте число: {prime_result}")
    print(f"Дільники: {divs}")
    print(f"Сума цифр: {d_sum}")

main()

#3
def average(grades):
    return sum(grades) / len(grades)

def minimum(grades):
    return min(grades)

def maximum(grades):
    return max(grades)

def count_above(grades, value):
    result = 0

    for grade in grades:
        if grade > value:
            result += 1

    return result

def main():
    input_grades = input("Оцінки: ")
    grades = [int(x) for x in input_grades.split()]

    threshold = int(input("Поріг: "))

    print(f"Середній бал: {average(grades)}")
    print(f"Мінімальна: {minimum(grades)}")
    print(f"Максимальна: {maximum(grades)}")
    print(f"Вище {threshold}: {count_above(grades, threshold)}")

main()

#4
def check_length(password):
    return len(password) >= 8

def check_digit(password):
    for char in password:
        if char.isdigit():
            return True
    return False

def check_upper(password):
    for char in password:
        if char.isupper():
            return True
    return False

def check_lower(password):
    for char in password:
        if char.islower():
            return True
    return False

def check_special(password):
    for char in password:
        if not char.isalnum():
            return True
    return False

def find_unfulfilled(password):
    unfulfilled = []

    if not check_length(password):
        unfulfilled.append("мінімальна довжина менше 8 символів")
    if not check_digit(password):
        unfulfilled.append("немає жодної цифри")
    if not check_upper(password):
        unfulfilled.append("немає великої літери")
    if not check_lower(password):
        unfulfilled.append("немає малої літери")
    if not check_special(password):
        unfulfilled.append("немає спеціального символу")

    return unfulfilled

def main():
    password = input("пароль: ")
    unfulfilled = find_unfulfilled(password)

    if len(unfulfilled) == 0:
        print("пароль надійний")
    else:
        print("Пароль не відповідає вимогам.")
        for requirement in unfulfilled:
            print(f"Не виконано: {requirement}")

main()