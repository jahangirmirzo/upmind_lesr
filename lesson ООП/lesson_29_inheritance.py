
# Урок по ООП: Наследование

# 1. Введение в наследование
# Наследование — это механизм, который позволяет создавать новый класс на основе уже существующего. Новый класс (дочерний) наследует атрибуты и методы старого класса (родительского), что позволяет избежать дублирования кода и расширять функциональность.

# Зачем нужно наследование?
# - Повторное использование кода.
# - Расширение и модификация функциональности без изменений в родительском классе.
# - Упрощение структуры программы за счет создания иерархий классов.

# 2. Основы наследования
# Родительский класс (superclass) — класс, от которого наследуют другие классы.
# Дочерний класс (subclass) — класс, который наследует функциональность родительского.
# Переопределение метода — дочерний класс может изменить поведение метода, унаследованного от родительского класса.
# Использование super() — позволяет обратиться к методам и атрибутам родительского класса.

# Пример 1: Основы наследования
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Вызов конструктора родительского класса
        self.breed = breed

    def speak(self):  # Переопределение метода родительского класса
        return f"{self.name} barks"

dog = Dog("Buddy", "Golden Retriever")
print(dog.speak())  # Вывод: Buddy barks

# Пример 2: Использование super()
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Вызов конструктора родительского класса
        self.breed = breed

    def speak(self):  # Переопределение метода
        parent_speak = super().speak()  # Вызов метода родительского класса
        return f"{parent_speak}, but {self.name} barks"

dog = Dog("Buddy", "Golden Retriever")
print(dog.speak())  # Вывод: Buddy makes a sound, but Buddy barks

# Пример 3: Множественное наследование
class Swimmer:
    def swim(self):
        return "Swimming"

class Animal:
    def speak(self):
        return "Animal sound"

class Dolphin(Animal, Swimmer):
    pass

dolphin = Dolphin()
print(dolphin.speak())  # Вывод: Animal sound
print(dolphin.swim())   # Вывод: Swimming

# 3. Преимущества наследования
# - Повторное использование кода: Переиспользование методов и атрибутов родительских классов.
# - Легкость в модификации: Когда нужно изменить поведение, достаточно переопределить метод в дочернем классе.
# - Структурированность: Наследование помогает организовать иерархию классов.

# 4. 15 задач по теме "Наследование"
# 1. Создайте класс Person с атрибутами name и age. Реализуйте метод introduce(), который будет выводить строку "Hello, my name is {name} and I am {age} years old". Создайте класс Student, который наследует Person и добавляет атрибут student_id. Переопределите метод introduce(), чтобы выводить "Hello, I am {name}, a student with ID {student_id}".
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Привет меня зовут  {self.name} и мне {self.age} год")


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def introduce(self):
        print(f"Hello, I am {self.name}, Студент с удостоверением личности  {self.student_id}")
p = Person("SHabdan", 28)
p.introduce()

s = Student("Botya", 25, "8181868")
s.introduce()

# 2. Создайте класс Vehicle с атрибутом speed и методом move(), который выводит сообщение "Moving at {speed} km/h". Создайте класс Car, который наследует от Vehicle и добавляет атрибут fuel_type. Переопределите метод move() для вывода сообщения "Car is moving at {speed} km/h using {fuel_type} fuel".
class Vehicle:
    def __init__(self, speed):
        self.speed = speed

    def move(self):
        print(f"Moving at {self.speed} km/h")


class Car(Vehicle):
    def __init__(self, speed, fuel_type):
        super().__init__(speed)
        self.fuel_type = fuel_type

    def move(self):
        print(f"Car is moving at {self.speed} km/h using {self.fuel_type} fuel")
v = Vehicle(60)
v.move()

c = Car(100, "diesel")
c.move()

# 3. Создайте базовый класс Shape с методом area() (возвращает 0). Создайте дочерние классы Circle и Rectangle, которые переопределяют метод area() для вычисления площади круга и прямоугольника соответственно.

# 4. Создайте класс Animal с методом speak(), который возвращает "Animal sound". Создайте классы Dog и Cat, которые переопределяют метод speak() и выводят звуки соответствующих животных.

# 5. Создайте класс Employee с атрибутами name и salary. Создайте класс Manager, который наследует от Employee и добавляет атрибут department. Переопределите метод __str__() в классе Manager, чтобы выводить строку "Manager {name}, Department: {department}, Salary: {salary}".

# 6. Создайте класс BankAccount с атрибутом balance и методами deposit() и withdraw(). Создайте класс SavingsAccount, который наследует от BankAccount и добавляет метод add_interest().

# 7. Создайте класс Person с атрибутом name и методом greet(). Создайте класс Employee, который наследует от Person и добавляет атрибут job_title. Переопределите метод greet() в классе Employee, чтобы выводить "Hello, I am {name}, and I work as a {job_title}".

# 8. Создайте класс Book с атрибутами title и author. Создайте дочерний класс EBook, который добавляет атрибут file_size и переопределяет метод __str__(), чтобы включить размер файла в строковое представление.

# 9. Создайте класс Product с атрибутами name и price. Создайте дочерний класс DiscountedProduct, который добавляет атрибут discount и метод get_discounted_price() для расчета цены со скидкой.

# 10. Создайте класс Shape с методом draw(). Создайте дочерние классы Circle и Square, которые переопределяют метод draw() для рисования соответствующих фигур.

# 11. Создайте класс Person с методом speak(). Создайте дочерний класс Teacher, который добавляет метод teach() и переопределяет метод speak(), чтобы выводить информацию о том, что этот человек учит.

# 12. Создайте класс Vehicle с атрибутом capacity. Создайте класс Bus, который наследует от Vehicle и добавляет метод pick_up(), который выводит сообщение о том, что автобус забирает пассажиров.

# 13. Создайте класс Shape с атрибутами width и height. Создайте класс Rectangle, который наследует от Shape и добавляет метод calculate_area(), который вычисляет площадь прямоугольника.

# 14. Создайте класс Person с методом work(). Создайте дочерний класс Engineer, который наследует от Person и переопределяет метод work(), чтобы выводить информацию о проекте, над котором работает инженер.

# 15. Создайте класс Student с атрибутом name и методом study(). Создайте дочерний класс GraduateStudent, который добавляет метод research() и переопределяет метод study() для вывода информации о научной работе.
