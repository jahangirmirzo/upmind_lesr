"""
Урок: Принцип Абстракции в ООП на Python

1. Теоретическая часть
2. Примеры с подробным объяснением
3. Практические задания (20 шт.)
"""

# 1. Теоретическая часть
"""
Абстракция — это принцип ООП, позволяющий скрывать детали реализации и оставлять только наиболее важные характеристики объекта.
Проще говоря, это выделение общих свойств и поведения объектов в отдельный класс, не вдаваясь в детали, которые могут различаться.

Абстракция помогает:
- Сократить количество кода
- Сделать систему более гибкой
- Упростить поддержку и развитие кода

В Python абстракция реализуется через абстрактные классы и абстрактные методы, которые задают интерфейс, а конкретная 
реализация предоставляется в дочерних классах.
"""


# 2. Примеры

# == Пример 1: Абстрактный класс и метод =="

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        """Абстрактный метод — подклассы должны его реализовать."""
        pass

class Dog(Animal):
    def make_sound(self):
        print("Гав-гав!")

class Cat(Animal):
    def make_sound(self):
        print("Мяу!")

# Попытка создать объект абстрактного класса вызовет ошибку:
try:
    a = Animal()
except TypeError as e:
    print("Ошибка:", e)

# Создание объектов потомков
dog = Dog()
dog.make_sound()  # Выведет: Гав-гав!

cat = Cat()
cat.make_sound()  # Выведет: Мяу!

"""
В этом примере:
- Абстрактный класс Animal задаёт интерфейс (метод make_sound).
- Подклассы Dog и Cat реализуют этот метод по-своему.
"""


# == Пример 2: Абстракция через базовый класс =="

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

rect = Rectangle(10, 5)
print(f"Площадь: {rect.area()}")
print(f"Периметр: {rect.perimeter()}")

"""
Здесь Shape — это абстрактный класс, который задаёт интерфейс для фигур.
Rectangle реализует конкретные методы area и perimeter.
"""


# == Пример 3: Интерфейс подключения (концептуальный пример) =="

class Database(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass

class MySQLDatabase(Database):
    def connect(self):
        print("Подключение к MySQL...")

    def disconnect(self):
        print("Отключение от MySQL...")

class PostgreSQLDatabase(Database):
    def connect(self):
        print("Подключение к PostgreSQL...")

    def disconnect(self):
        print("Отключение от PostgreSQL...")

mysql_db = MySQLDatabase()
mysql_db.connect()
mysql_db.disconnect()

psql_db = PostgreSQLDatabase()
psql_db.connect()
psql_db.disconnect()

"""
Абстракция позволяет задавать общий интерфейс для работы с базой данных, а конкретные реализации могут быть разными (MySQL, PostgreSQL).
"""


# 3. Практические задания

# 1. Создайте абстрактный класс Vehicle с методом move().
# 2. Реализуйте два класса Car и Bike, которые наследуются от Vehicle и реализуют move().
# 3. Создайте абстрактный класс Appliance с абстрактным методом turn_on().
# 4. Реализуйте подклассы: Fridge и Microwave, которые включаются по-своему.
# 5. Создайте абстрактный класс Worker с методом work().
# 6. Реализуйте два подкласса: Developer и Designer.
# 7. Создайте абстрактный класс Animal с методом speak().
# 8. Создайте классы Cow и Sheep, которые "говорят" по-разному.
# 9. Создайте абстрактный класс Payment с методом pay().
# 10. Реализуйте подклассы: CreditCardPayment и CashPayment.
# 11. Создайте абстрактный класс File с методом open().
# 12. Реализуйте подклассы: TextFile и ImageFile.
# 13. Создайте абстрактный класс Person с методом introduce().
# 14. Реализуйте подклассы Student и Teacher.
# 15. Создайте абстрактный класс Account с методом login().
# 16. Реализуйте подклассы: FacebookAccount и GoogleAccount.
# 17. Создайте абстрактный класс Sensor с методом read_data().
# 18. Реализуйте подклассы: TemperatureSensor и PressureSensor.
# 19. Создайте абстрактный класс Employee с методом calculate_salary().
# 20. Реализуйте подклассы: HourlyEmployee и SalariedEmployee.



