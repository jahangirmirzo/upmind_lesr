
# 🔹 1. Целые числа (int)
age = int(input("Введите ваш возраст: "))  # Ввод числа
print("Ваш возраст:", age)
print(type(age))  # <class 'int'>

a = 10
b = 3
print(a + b)  # 13 (сложение)
print(a - b)  # 7 (вычитание)
print(a * b)  # 30 (умножение)
print(a // b)  # 3 (целочисленное деление)
print(a % b)  # 1 (остаток от деления)
print(a ** b)  # 1000 (возведение в степень)

# 🔹 2. Числа с плавающей точкой (float)
pi = float(input("Введите число с плавающей точкой: "))  # Ввод float
print("Вы ввели:", pi)
print(type(pi))  # <class 'float'>
print(round(pi, 2))  # Округление

num_str = "3.5"
num_float = float(num_str)
print(type(num_float))  # <class 'float'>

# 🔹 3. Строки (str)
name = input("Введите ваше имя: ")  # Ввод строки
print("Привет, " + name + "!")
print(type(name))  # <class 'str'>

text = """Это многострочный
текст в Python"""
print(text)

word = "Python"
print(word[0])  # P
print(word[-1])  # n
print(len(word))  # 6

number = 42
num_str = str(number)
print(type(num_str))  # <class 'str'>

# 🔹 4. Булевы значения (bool)
is_python_easy = input("Python легкий? (да/нет): ").lower() == "да"  # Ввод bool
print("Вы ответили:", is_python_easy)
print(type(is_python_easy))  # <class 'bool'>

print(a > b)  # False
print(a < b)  # True
print(a == b)  # False
print(a != b)  # True

print(True and False)  # False
print(True or False)  # True
print(not True)  # False

# 🔹 5. Преобразование типов
print(float(5))  # 5.0
print(int(5.9))  # 5
print(int("100"))  # 100
print(str(42))  # "42"
print(int(True))  # 1
print(int(False))  # 0
