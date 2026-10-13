#1
N = int(input("N: "))

count = 0
sum = 0

for i in range(1, N + 1):
    if i % 3 == 0 or i % 5 == 0:
        count += 1
        sum += i

if count > 0:
    average = sum / count
else:
    average = 0

print("кількість: ", count)
print("сума: ", sum)
print("середнє: ", average)

#2
N = int(input("N: "))

if N == 0:
    count2 = 1
    sum2 = 0
    max = 0
    min = 0
else:
    count2 = 0
    sum2 = 0
    max = 0
    min = 9
    temp = N
    while temp > 0:
        digit = temp % 10
        count2 += 1
        sum2 += digit
        if digit > max:
            max = digit
        if digit < min:
            min = digit
        temp //= 10

print("кількість: ", count2)
print("сума: ", sum2)
print("найбільша: ", max)
print("найменша: ", min)

#3
N = int(input("Введіть N: "))
result = []

for i in range(1, N + 1):
    temp2 = i
    is_valid = True
    has_zero = False

    t = temp2
    while t > 0:
        digit = t % 10
        if digit == 0:
            has_zero = True
            break
        if i % digit != 0:
            is_valid = False
            break
        t //= 10

    if not has_zero and is_valid:
        result.append(str(i))

print(" ".join(result))

#4
width = int(input("ширина: "))
height = int(input("висота: "))
border = input("символ контуру: ")
inner = input("символ внутрішньої частини: ")

if width < 3 or height < 3:
    print("мінімальний розмір 3x3")
else:
    for i in range(height):
        row = ""
        for j in range(width):
            if i == 0 or i == height - 1 or j == 0 or j == width - 1:
                row += border
            else:
                row += inner
        print(row)
