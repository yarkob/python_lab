#1
with open("text.txt", encoding="utf-8", newline="") as file:
    text = file.read()

lines = text.splitlines()

print("рядків:", len(lines))
print("слів:", len(text.split()))
print("символів:", len(text))

if lines:
    longest = max(lines, key=len)
    print("найдовший рядок:", lines.index(longest) + 1)
    print("довжина:", len(longest))
    print("текст:", longest)
else:
    print("файл порожній")

#2
fragment = input("фрагмент: ").casefold()
found = False

with open("text.txt", encoding="utf-8") as file:
    for number, line in enumerate(file, 1):
        line = line.rstrip("\n")
        if fragment in line.casefold():
            print(f"{number}: {line}")
            found = True

if not found:
    print("збігів немає")

#3
students = []

with open("students.txt", encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        if not line:
            continue

        name, score = line.split(";")
        score = int(score)

        if score > 80:
            students.append((name, score))

students.sort(key=lambda student: student[1], reverse=True)

with open("result.txt", "w", encoding="utf-8") as file:
    for name, score in students:
        file.write(f"{name};{score}\n")

#4
def read_grades():
    grades = {}

    with open("grades.csv", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line:
                name, _, grade = line.split(";")
                grades.setdefault(name, []).append(int(grade))

    return grades


def write_report(grades):
    students = []

    for name, marks in grades.items():
        average = sum(marks) / len(marks)
        students.append((name, len(marks), average))

    students.sort(key=lambda student: student[2], reverse=True)

    with open("report.txt", "w", encoding="utf-8") as file:
        if not students:
            file.write("оцінок немає\n")
            return

        for name, count, average in students:
            file.write(f"{name} - оцінок: {count} - середній: {average:.2f}\n")

        best_average = students[0][2]
        best_names = []

        for name, count, average in students:
            if average == best_average:
                best_names.append(name)

        names = " та ".join(best_names)
        file.write(f"найкращий результат:\n{names} - {best_average:.2f}\n")


write_report(read_grades())
