import tkinter as tk

import student_utils


students = ["Anna", "Ivan", "Olha"]


def show_report():
    value = count_entry.get().strip()
    result.delete("1.0", tk.END)

    if not value.isdecimal() or not 1 <= int(value) <= 20:
        result.insert(tk.END, "число від 1 до 20")
        return

    count = int(value)
    lines = []

    for student in students:
        grades = student_utils.generate_grades(count)
        average = student_utils.average_grade(grades)
        level = student_utils.get_level(average)
        lines.append(f"{student}: {grades} → {round(average, 2)} → {level}")

    report = "\n".join(lines)
    result.insert(tk.END, report)
    print(report)


window = tk.Tk()
window.title("Статистика учнів")

tk.Label(window, text="кількість оцінок (1–20)").pack()

count_entry = tk.Entry(window)
count_entry.pack()

tk.Button(window, text="Сформувати звіт", command=show_report).pack()

result = tk.Text(window, width=65, height=8)
result.pack()

window.mainloop()
