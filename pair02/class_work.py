#1
n = int(input('N = '))
for i in range(1, n + 1):
    print(i)

#2
n = int(input('N = '))
i = 1
while i <= n:
    print(i)
    i += 1

#3
n = int(input('N = '))
total = 0
for i in range(1, n + 1):
    total += i
print('Сума:', total)
print('Середнє:', total / n)

#4
n = int(input('N = '))
result = 1
for i in range(1, n + 1):
    result *= i
print('Факторіал:', result)

#5
n = int(input('N = '))
total = 0
for i in range(1, n + 1):
    if i % 3 == 0:
        total += i
print('Сума:', total)

#6
print(list(range(5)))
print(list(range(2, 8)))
print(list(range(10, 1, -2)))

#7
n = int(input('N = '))
count = 0
total = 0
max_digit = 0
while n > 0:
    digit = n % 10
count += 1
total += digit
if digit > max_digit:
    max_digit = digit
n //= 10
print('Кількість:', count)
print('Сума цифр:', total)
print('Найбільша цифра:', max_digit)

#8
while True:
    value = input("Введіть число або 'stop': ")
    if value == 'stop':
        break
    print('Введено:', value)

#9
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)

#10
for i in range(1, 6):
    for j in range(1, 6):
        print(i * j, end='\t')
    print()

#11
width = int(input('Ширина: '))
height = int(input('Висота: '))
for row in range(height):
    for col in range(width):
        print('*', end='')
    print()

#12
n = int(input('N = '))
for i in range(1, n + 1):
    if n % i == 0:
        print(i)
