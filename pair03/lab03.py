#1
text = input("Введіть довільний текст: ")

total_chars = len(text)
letters = 0
digits = 0
spaces = 0
vowels = 0

vowels_list = "aeiou"

for char in text:
    if char.isalpha():
        letters += 1
    if char.lower() in vowels_list:
        vowels += 1
    elif char.isdigit():
        digits += 1
    elif char.isspace():
        spaces += 1

words = text.split()
total_words = len(words)

print("Символів: ", total_chars)
print("Літер: ", letters)
print("Цифр: ", digits)
print("Пробілів: ", spaces)
print("Голосних: ", vowels)
print("Слів: ", total_words)

#2
name = input("прізвище, ім'я та по батькові: ")

parts = name.split()

if len(parts) == 3:
    surname = parts[0].capitalize()
    name = parts[1][0].upper()
    name2 = parts[2][0].upper()

    result = f"{surname} {name}.{name2}."
    print(result)
else:
    print("помилка")

#3
input1 = input("перший рядок: ")
input2 = input("другий рядок: ")

str1 = "".join(input1.lower().split())
str2 = "".join(input2.lower().split())

is_anagram = True

if len(str1) != len(str2):
    is_anagram = False
else:
    chars_list = list(str2)

    for char in str1:
        if char in chars_list:
            chars_list.remove(char)
        else:
            is_anagram = False
        break

if is_anagram:
    print("Рядки є анаграмами.")
else:
    print("Рядки не є анаграмами.")

#4
sentence = input("речення: ")
words = sentence.split()
if words:
    max_len = len(max(words, key=len))
    min_len = len(min(words, key=len))

    longest = []
    for w in words:
        if len(w) == max_len and w not in longest:
            longest.append(w)

    shortest = []
    for w in words:
        if len(w) == min_len and w not in shortest:
            shortest.append(w)

    unique = []
    for w in words:
        w_lower = w.lower()
        if w_lower not in unique:
            unique.append(w_lower)

    print("Найдовші:", ", ".join(longest))
    print("Найкоротші:", ", ".join(shortest))
    print("Унікальних слів:", len(unique))

    old_word = input("слово для заміни: ")
    new_word = input("нове слово: ")

    for i in range(len(words)):
        if words[i].lower() == old_word.lower():
            words[i] = new_word

    new_sentence = " ".join(words)
    print("Після заміни:", new_sentence)
else:
    print("нічого не введено")