# === Урок 15: Функции в Python ===

# --- Объяснение темы ---

# Функции — это блоки кода, которые можно переиспользовать.
# Они помогают структурировать программу, избегать повторений и повышать читаемость.

# Синтаксис определения функции:
# def имя_функции(аргументы):
#     блок_кода
#     return значение (необязательно)

# Пример:

# Функция без аргументов:
def say_hello():
    print("Привет, мир!")


say_hello()  # Вызов функции без аргументов


def greet(name):
    print(f"Привет, {name}!")


greet("Анна")  # Вызов функции


# Функция с возвратом значения:
def square(x):
    return x ** 2


result = square(5)
print(result)  # 25


# Функция с несколькими аргументами:
def add(a, b):
    return a + b


print(add(2, 3))  # 5


# Аргументы по умолчанию:
def greet_user(name="гость"):
    print(f"Привет, {name}!")

# --- Ознакомительные задачи (10) ---

# 1. Напиши функцию, которая выводит "Привет, мир!".
# 2. Напиши функцию, которая принимает имя (например, 'Иван') и приветствует пользователя.
# 3. Напиши функцию, которая возвращает квадрат числа (например, 4).
# 4. Напиши функцию, которая возвращает сумму двух чисел (например, 5 и 7).
# 5. Напиши функцию, которая проверяет, чётное число или нет (например, 10).
# 6. Напиши функцию, которая возвращает длину строки (например, 'python').
# 7. Напиши функцию, которая принимает список (например, [1, 2, 3]) и возвращает его сумму.
# 8. Напиши функцию, которая принимает строку (например, 'hello') и возвращает строку в верхнем регистре.
# 9. Напиши функцию, которая возвращает True, если число (например, 15) делится на 3 и 5.
# 10. Напиши функцию, которая принимает имя и возраст ('Анна', 25), и возвращает строку вида
# "Меня зовут ... мне ... лет".

# --- Домашнее задание (40 задач) ---

# 1. Функция, возвращающая разность двух чисел (например, 10 и 3).
# 2. Функция, принимающая число (например, -7) и возвращающая его модуль.
# 3. Функция, проверяющая, является ли число (например, -5) отрицательным.
# 4. Функция, возвращающая максимальное из двух чисел (например, 5 и 8).
# 5. Функция, возвращающая минимальное из трёх чисел (например, 3, 7, 2).
# 6. Функция, возвращающая True, если строка (например, 'python is fun') содержит слово 'python'.
# 7. Функция, проверяющая, пустая строка или нет (например, '').
# 8. Функция, считающая количество символов в строке без пробелов (например, 'hello world').
# 9. Функция, возвращающая True, если в строке (например, 'abc123') есть хотя бы одна цифра.
# 10. Функция, возвращающая строку наоборот (например, 'python' -> 'nohtyp').
# 11. Функция, проверяющая, является ли число (например, 17) простым.
# 12. Функция, возвращающая все делители числа (например, 12 -> [1, 2, 3, 4, 6, 12]).
# 13. Функция, возвращающая факториал числа (например, 5 -> 120).
# 14. Функция, преобразующая список строк (например, ['cat', 'dog']) в список их длин.
# 15. Функция, проверяющая, все ли элементы списка (например, [2, 4, 6]) чётные.
# 16. Функция, считающая количество чётных чисел в списке (например, [1, 2, 3, 4, 5]).
# 17. Функция, возвращающая сумму квадратов всех чисел в списке (например, [1, 2, 3]).
# 18. Функция, возвращающая True, если два слова (например, 'listen', 'silent') являются анаграммами.
# 19. Функция, принимающая список (например, [1, 2, 2, 3]) и возвращающая только уникальные элементы.
# 20. Функция, соединяющая два списка без повторений (например, [1, 2], [2, 3] -> [1, 2, 3]).
# 21. Функция, возвращающая среднее значение чисел из списка (например, [4, 8, 12]).
# 22. Функция, проверяющая, входит ли элемент (например, 5) в список [1, 3, 5, 7].
# 23. Функция, принимающая строку (например, 'hello world') и возвращающая количество слов.
# 24. Функция, удаляющая все пробелы из строки (например, 'hello world' -> 'helloworld').
# 25. Функция, преобразующая строку (например, 'one two three') в список слов.
# 26. Функция, возвращающая True, если слово (например, 'madam') читается одинаково в обе стороны.
# 27. Функция, удаляющая дубликаты из списка (например, [1, 2, 2, 3]).
# 28. Функция, заменяющая все гласные в строке (например, 'hello') на *.
# 29. Функция, проверяющая, все ли символы в строке (например, 'abc') уникальны.
# 30. Функция, принимающая два числа (например, 3 и 7) и возвращающая список чисел между ними.
# 31. Функция, преобразующая список чисел (например, [1, 2, 3]) в строку '1,2,3'.
# 32. Функция, находящая максимальное и минимальное число в списке (например, [4, 2, 9]).
# 33. Функция, возвращающая True, если список (например, [1, 2, 3, 4]) отсортирован по возрастанию.
# 34. Функция, возвращающая количество положительных чисел в списке (например, [-2, 3, 4]).
# 35. Функция, возвращающая произведение всех чисел в списке (например, [2, 3, 4]).
# 36. Функция, объединяющая значения словаря (например, {'a': 'hi', 'b': 'there'}) в одну строку 'hithere'.
# 37. Функция, сортирующая словарь (например, {'a': 3, 'b': 1}) по значениям.
# 38. Функция, принимающая строку (например, 'hello') и возвращающая словарь частот символов.
# 39. Функция, возвращающая словарь квадратов чисел от 1 до N (например, N = 5).
# 40. Функция, проверяющая, является ли введённый год (например, 2024) високосным.
