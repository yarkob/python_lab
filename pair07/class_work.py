#1
with open("hello.txt", "w", encoding="utf-8") as file:
    file.write("Привіт, Python!\n")

#2
with open("log.txt", "w", encoding="utf-8") as file:
    file.write("Перший запуск\n")
with open("log.txt", "a", encoding="utf-8") as file:
    file.write("Новий запис\n")

#3
with open("hello.txt", "r", encoding="utf-8") as file:
    text = file.read()

print(text)

#4
with open("text.txt", "r", encoding="utf-8") as file:
    text = file.read()
print(text)
print("Символів:", len(text))

#5
with open("text.txt", "r", encoding="utf-8") as file:
    for number, line in enumerate(file, start=1):
        print(f"{number}: {line.strip()}")

#6
with open("text.txt", "r", encoding="utf-8") as file:
    for line in file:
        clean_line = line.strip()
        print(clean_line)

#7
numbers = []
with open("numbers.txt", "r", encoding="utf-8") as file:
    for line in file:
        numbers.append(int(line.strip()))

print("Min:", min(numbers))
print("Max:", max(numbers))
print("Sum:", sum(numbers))
print("Average:", sum(numbers) / len(numbers))

#8
with open("students.txt", "r", encoding="utf-8") as file:
    for line in file:
        name, score = line.strip().split(";")
        print(name, int(score))

#9
line = "Anna;Python;11"
name, subject, grade = line.split(";")

print("Учень:", name)
print("Предмет:", subject)
print("Оцінка:", int(grade))

#10
selected = []
with open("students.txt", "r", encoding="utf-8") as file:
    for line in file:
        name, score = line.strip().split(";")
        score = int(score)

    if score > 80:
        selected.append([name, score])

print(selected)

#11
students = [
    ["Anna", 91],
    ["Ivan", 84],
    ["Olha", 97]
]

students.sort(key=lambda student: student[1], reverse=True)

for student in students:
    print(student[0], student[1])

#12
students = [
    ["Olha", 97],
    ["Anna", 91],
    ["Ivan", 84]
]

with open("result.txt", "w", encoding="utf-8") as file:
    for name, score in students:
        print(f"{name};{score}", file=file)

print("Звіт result.txt створено.")
