"""
Основные виды полиморфизма в Python:
1. Ad-hoc полиморфизм (перегрузка операторов и функций)
2. Параметрический полиморфизм (дженерики)
3. Полиморфизм подтипов (наследование)

Полиморфизм — это возможность объектов с одинаковым интерфейсом использовать разные реализации.
Это один из основных принципов ООП, который делает код гибким и удобным для расширения.

Проявления полиморфизма:
- Полиморфизм функций/методов — одна и та же функция может работать с разными типами.
- Полиморфизм классов — один и тот же метод/интерфейс работает по-разному в разных классах.

Duck typing (утиная типизация): "Если объект выглядит как утка и крякает как утка, то это утка".
В Python важна не принадлежность к классу, а наличие нужных методов.

"""

# "\n=== 1.2.1 Встроенный полиморфизм ==="
# print("5 + 3 =", 5 + 3)  # Сложение чисел
# print("'Hello' + '!' =", "Hello" + "!")  # Конкатенация строк
# print("[1, 2] + [3] =", [1, 2] + [3])  # Объединение списков



# Полиморфизм с разными типами данных
# def process(data):
#     if isinstance(data, str):
#         return data.upper()
#     elif isinstance(data, list):
#         return [process(item) for item in data]
#     elif isinstance(data, dict):
#         return {k: process(v) for k, v in data.items()}
#     else:
#         return data
#
# print("Пример 1:")
# print(process("hello"))
# print(process(["hello", "world"]))
# print(process({"a": "hello", "b": "world"}))
# print()
#
#
#
"=== 1.2.2 Полиморфизм через наследование ==="


#
# class Animal:
#     def make_sound(self):
#         pass
#
#
# class Dog(Animal):
#     def make_sound(self):
#         return "Гав!"
#
#
# class Cat(Animal):
#     def make_sound(self):
#         return "Мяу!"
#
#
# animals = [Dog(), Cat()]
# for animal in animals:
#     print(f"{animal.__class__.__name__}: {animal.make_sound()}")
#
# Создайте функцию my_max() и my_min() которая может принимать:
# 1. Список чисел (int, float)
# 2. Список строк (string)
# 3. Строку (string)

def my_max(data):
    max_value = ""
    if isinstance(data, str) and len(data) >  0:
        max_value = data[0]
        for char in data:
            if char > max_value:
                max_value = char
    elif isinstance(data, list):
        print("list")
        return max_value

def my_min(data):

    pass


print(my_max([1, 2, 3]), "--", max([1, 2, 3]))
print(my_max(["a", "b", "c"]), "--", min(["a", "b", "c"]))
print(my_max("Hello World"), "--", max("Hello World!"))

print(my_min([1, 2, 3]), "--", min([1, 2, 3]))
print(my_min(["a", "b", "c"]), "--", min(["a", "b", "c"]))



# ========================
# 2. ПРАКТИЧЕСКИЕ ЗАДАНИЯ
# ========================

# "\n=== 2.1 Задания на понимание полиморфизма ==="

# "1. Создайте классы Bird и Fish с методом move(). У птицы метод должен возвращать 'Летит', у рыбы — 'Плывет'.",
class Bird:
    def move(self):
        return "Летит"


class Fish:
    def move(self):
        return "Плывет"
bird = Bird()
print(bird.move())

fish = Fish()
print(fish.move())

# "2. Перегрузите оператор * для класса String, чтобы он повторял строку N раз.",
class String:
    def __init__(self, text):
        self.text = text

    def __mul__(self, n):
        if isinstance(n, int):
            return String(self.text * n)
        raise TypeError("Оператор * работает только с целыми числами")

    def __str__(self):
        return self.text

    def __repr__(self):
        return f'String("{self.text}")'
s = String("Привет ")
print(s * 3)
print(repr(s * 2))

# "3. Напишите функцию multiply(a, b), которая работает для чисел (умножение) и строк (повторение a b раз).",
def multiply(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a * b
    elif isinstance(a, str) and isinstance(b, int):
        return a * b
    elif isinstance(b, str) and isinstance(a, int):
        return b * a
    else:
        raise TypeError("Функция поддерживает только умножение чисел или повторение строки целое число раз.")
print(multiply(3, 4))
print(multiply("hi", 3))
print(multiply(2, "ok"))

# "5. Реализуйте полиморфное поведение в классе Calculator с методом add(a, b) (должен работать с числами и строками).",
class Calculator:
    def add(self, a, b):
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return a + b
        elif isinstance(a, str) and isinstance(b, str):
            return a + b
        else:
            raise TypeError("Метод add поддерживает только сложение чисел или конкатенацию строк.")
calc = Calculator()

print(calc.add(5, 3))
print(calc.add("Hello, ", "world!"))
print(calc.add(3.5, 2.1))

# "6. Создайте абстрактный класс Device с методом turn_on() и реализуйте его в Lamp и Computer.",
from abc import ABC, abstractmethod

# Абстрактный класс
class Device(ABC):
    @abstractmethod
    def turn_on(self):
        pass

# Класс Lamp реализует метод turn_on
class Lamp(Device):
    def turn_on(self):
        print("Лампа включена. Светло!")

# Класс Computer реализует метод turn_on
class Computer(Device):
    def turn_on(self):
        print("Компьютер включен. Загрузка системы...")
lamp = Lamp()
lamp.turn_on()         

computer = Computer()
computer.turn_on()

# "7. Напишите функцию print_length(obj), которая выводит длину строки, списка или кортежа.",
# "8. Перегрузите метод __str__ в классах Book и Author, чтобы они выводили разную информацию.",
# "9. Создайте класс Playable с методом play() и реализуйте его в Audio и Video.",
# "10. Напишите функцию concat(a, b), которая складывает числа и объединяет строки."


#  2.2 Задания на применение полиморфизма в ООП
# "11. Создайте иерархию классов Transport (с методом move()), реализовав его в Car, Boat, Airplane.",
# "12. Реализуйте полиморфное поведение в методе draw() для классов Circle, Square, Triangle.",
# "13. Создайте класс Database с абстрактным методом connect() и реализуйте его в MySQL и PostgreSQL.",
# "14. Напишите функцию process_data(data), которая работает с int, str и list по-разному.",
# "15. Создайте класс Logger с методом log() и переопределите его в FileLogger и ConsoleLogger.",
# "16. Реализуйте __add__ в классе Matrix для сложения матриц.",
# "17. Создайте класс Payment с методом pay() и реализуйте его в CreditCard, PayPal, Crypto.",
# "18. Напишите функцию compare(a, b), которая сравнивает числа, строки и списки.",
# "19. Создайте класс Animal с методом speak() и переопределите его в Dog, Cat, Cow.",
# "20. Реализуйте __mul__ в классе Fraction для умножения дробей."

"""
=== 4.1 Итоги урока ===
- Полиморфизм позволяет использовать одинаковые методы для разных типов
- В Python реализуется через:
  * Перегрузку операторов (__add__, __mul__ и др.)
  * Наследование и переопределение методов
- Делает код более гибким и расширяемым
"""
