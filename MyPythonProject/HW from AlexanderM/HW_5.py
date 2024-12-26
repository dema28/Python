""" 1. Прямоугольник

- Создайте класс Rectangle, который принимает ширину и высоту
прямоугольника при создании и должен иметь соответствующие атрибуты
width и height (целые числа).
- Создайте метод area(), который возвращает площадь прямоугольника.
- Создайте метод perimeter(), который возвращает периметр
прямоугольника.
Пример:
rect = Rectangle(2, 4)
a = rect.area() # Вернул 8
p = rect.perimeter() # Вернул 12"""

# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return self.width * self.height
#
#     def perimeter(self):
#         return 2 * (self.width + self.height)
#
# print(Rectangle(2, 4).area())  # 8
# print(Rectangle(2, 4).perimeter())  # 12


""" 2. Автомобиль

- Создайте класс Car, который принимает марку автомобиля (make) в виде
строки и максимально возможную скорость (max_speed) в виде целого
числа при создании. Также при инициализации (в теле __init__) экземпляра
Car должен быть автоматически создан атрибут speed, равный 0 (текущая
скорость автомобиля).
- Создайте метод display_speed(), который выводит в консоль текущую
скорость автомобиля.
- Создайте метод accelerate(), который увеличивает скорость автомобиля на
10, при этом скорость автомобиля не должна превышать max_speed, если
вызывается accelerate() при максимальной скорости, то скорость не
должна увеличиваться.
- Создайте метод brake(), который уменьшает скорость автомобиля на 10,
при этом скорость автомобиля не может быть меньше 0. Если вызывается
метод brake() при скорости равной 0, то скорость не должна уменьшаться.
Пример:
my_toyota = Car("Toyota", 180)
my_toyota.accelerate()
my_toyota.accelerate()

my_toyota.accelerate()
my_toyota.display_speed() # вывел в консоль 30"""

# class Car:
#     def __init__(self, make, max_speed):
#         self.make = make
#         self.max_speed = max_speed
#         self.speed = 0
#
#     def display_speed(self):
#         print(f"Current speed: {self.speed}")
#
#     def accelerate(self):
#         if self.speed + 10 <= self.max_speed:
#             self.speed += 10
#         else:
#             self.speed = self.max_speed
#
#     def brake(self):
#         if self.speed - 10 >= 0:
#             self.speed -= 10
#         else:
#             self.speed = 0
#
#             print(f"Current speed: {self.speed}")
#             self.display_speed()
#             print("Car is stopped")
#
# my_VW = Car("Volkswagen", 220)
# my_VW.accelerate()
# my_VW.accelerate()
# my_VW.accelerate()
# my_VW.accelerate()
# my_VW.brake()
# my_VW.brake()
# my_VW.brake()
# my_VW.brake()
# my_VW.display_speed()


""" 3. Интернет-банк

- Создайте класс BankAccount, который принимает имя владельца (name) в
виде строки и текущее состояние счета (balance) в виде целого числа. Оба
этих атрибута должны быть _защищенным.
- Создайте метод deposit(), который принимает 1 аргумент (если не считать
self, конечно) amount (целое число). Метод должен увеличить текущий
баланс аккаунта на amount.
- Создайте метод withdraw(), который принимает 1 аргумент amount (целое
число). Метод должен уменьшить текущий баланс аккаунта на amount. Если
денег на счету недостаточно, то метод выводит на экран “Недостаточно
средств!”.
- Создайте метод get_balance(), который возвращает текущее значение
баланса аккаунта.
Пример:
account = BankAccount("Maria", 1000)
account.deposit(700)
account.withdraw(200)
print(account.get_balance()) # 1500"""

# class BankAccount:
#     def __init__(self, name, balance):
#         self.__name = name
#         self.__balance = balance
#
#     def deposit(self, amount):
#         self.__balance += amount
#
#     def withdraw(self, amount):
#         if self.__balance >= amount:
#             self.__balance -= amount
#         else:
#             print("Недостаточно средств!")
#
#     def get_balance(self):
#         return self.__balance
#
#     def _update_balance(self, amount):  # Добавляем метод для изменения баланса
#         self.__balance += amount
#
# account = BankAccount("Vasia", 10000)
# account.deposit(1000)
# account.withdraw(11000)
# print(account.get_balance())  # 1500


""" 4. Овердрафт

- Создайте класс OverdraftAccount, унаследованный от вашего класса
BankAccount из предыдущей задачи.
- Переопределите существующий метод withdraw(), но теперь, если баланс
аккаунта меньше или равен 0, то это не выводит на экран сообщение
“Недостаточно средств!”, а уменьшает баланс в минус.
Пример:
jack_account = OverdraftAccount("Jack", 0)
jack_account.withdraw(100)

jack_account.withdraw(100)
jack_account.withdraw(100)
print(jack_account.get_balance()) # -300"""

# class OverdraftAccount(BankAccount):
#     def withdraw(self, amount):
#         current_balance = self.get_balance()
#         if current_balance - amount < 0:
#             self._update_balance(-amount)
#         else:
#             self._update_balance(-amount)
#
# Vasia_account = OverdraftAccount("Vasia", 10000)
# Vasia_account.withdraw(1000)
# Vasia_account.withdraw(11000)
# print(Vasia_account.get_balance())


""" Повторение прошлого материала.

Ответьте на следующие вопросы:
1. Что такое and, or и not? Приведите пример их использования.
2. Что такое цикл? Чем отличается for от while?
3. Как нельзя именовать переменную? Почему я не могу назвать переменную
max или min?
4. Что такое функция? Зачем она нужна?

Ответы: 
    1. Что такое and, or и not?
Это логические операторы:
and: возвращает True, если обе части выражения истинны.
print(True and False)  # False
or: возвращает True, если хотя бы одна часть выражения истинна.
print(True or False)  # True
not: возвращает обратное значение (True → False, False → True).
print(not True)  # False

    2. Что такое цикл? Чем отличается for от while?
Цикл позволяет повторять блок кода несколько раз.
for: используется, когда известно, сколько раз нужно повторить.
for i in range(5):  # Выполнится 5 раз
    print(i)
while: используется, когда повторение зависит от условия.
x = 0
while x < 5:  # Выполняется, пока x < 5
    print(x)
    x += 1
	
    3. Как нельзя именовать переменную?
Нельзя использовать зарезервированные слова (например, if, for, while).
Нельзя начинать имя с цифры (2var — ошибка).
Нельзя использовать имя встроенных функций (max, min, len) — это может привести к ошибкам в коде.
max = 5  # Теперь встроенная функция max не работает
print(max([1, 2, 3]))  # Ошибка

    4. Что такое функция? Зачем она нужна?
Функция — это блок кода, который можно вызывать многократно.
Упрощает код: повторяющийся функционал пишется один раз.
Делает код читаемым и поддерживаемым.
Пример:
def greet(name):
    return f"Hello, {name}!"
print(greet("Alice"))  # Hello, Alice!"""
