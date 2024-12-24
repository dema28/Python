""" 1. Особые числа.

- Сгенерируйте список numbers, состоящий из чисел в диапазоне от 0 до 100
включительно, которые делятся без остатка как на 2, так и на 3.
- Выведите список numbers на экран. Решите эту задачу в 2 способа - с помощью генератора списков и без него.
Ответ: [0, 6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96]"""


# 1 способ
# numbers = [num for num in range(101) if num % 2 == 0 and num % 3 == 0]
# print(numbers)

# 2 способ
# numbers = []
# for num in range(101):
#     if num % 2 == 0 and num % 3 == 0:
#         numbers.append(num)
# print(numbers)


""" 2. Фильтр.
Имеется список items = [1.2, 3, None, 100, {'info': 'bla-bla'}, 44, 'Hi!', 99, 44.32, None]
- Составьте новый список numbers, который содержит только целые числа
(int) и вещественные числа (float) из списка items.
- Выведите на экран сумму чисел в numbers.
Ответ: 291.52"""

# items = [1.2, 3, None, 100, {'info': 'bla-bla'}, 44, 'Hi!', 99, 44.32, None]
# numbers = [item for item in items if isinstance(item, (int, float))]
# print(sum(numbers))


""" 3. История сообщений.

- Создать список messages, который будет хранить “сообщения”.
- Программа должна в бесконечном цикле запрашивать у пользователя
ввести сообщение (строку) с клавиатуры и сохранять ее в список messages.
Причем программа должна запоминать не более 5 последних сообщений.
То есть, если длина списка messages превысила 5, то первое сообщение в
нем должно быть удалено.
- Если пользователь ввел “Пока”, то программа должна вывести “Ну ладно,
пока!” и список последних сообщения на экран. Пример: если пользователь вводил такие сообщения (без кавычек): “Привет!”,
“Как твои дела?”, “Как твое настроение?”, “Бла-бла-бла”, “Что нового?”, “Сори я
занят”, “Пока”"""

# messages = []
# while True:
#     message = input("Введите сообщение (или 'Пока' для выхода): ")
#     if message == "Пока":
#         print("Ну ладно, пока!")
#         print("Последние сообщения:", messages[-5:])
#         break
#     if len(messages) >= 5:
#         messages.pop(0)
#     messages.append(message)


""" 4. Без дубликатов.

Имеется список numbers = [15, 3, 8, 42, 3, 23, 8, 7, 42, 1, 9, 23, 15, 5, 9, 4, 6, 1]
- Создайте новый список, где будут удалены все дубликаты из списка
numbers.
- Отсортируйте итоговый список и выведите на экран.
Ответ: [1, 3, 4, 5, 6, 7, 8, 9, 15, 23, 42]
# Решите задачу с использованием множества и без него."""

# numbers = [15, 3, 8, 42, 3, 23, 8, 7, 42, 1, 9, 23, 15, 5, 9, 4, 6, 1]
# numbers = list(set(numbers))
# numbers.sort()
# print(numbers)
#
# # Решение с использованием множества
# numbers = [15, 3, 8, 42, 3, 23, 8, 7, 42, 1, 9, 23, 15, 5, 9, 4, 6, 1]
# # Удаляем дубликаты вручную
# unique_numbers = []
# for number in numbers:
#     if number not in unique_numbers:
#         unique_numbers.append(number)
# unique_numbers.sort() # Сортируем результат
# print(unique_numbers) # Выводим результат


""" 5. Повторение прошлого материала.

Ответьте на следующие вопросы:
1. Что такое итерируемый объект? Какие итерируемые объекты вы знаете?
2. Что такое break и где он может быть полезен? А что такое continue?

Ответы: 1. Что такое итерируемый объект?
Итерируемый объект (или iterable) — это объект, который можно "перебирать" по элементам с помощью цикла (например, for) или других инструментов, работающих с итерациями.

Основные характеристики итерируемого объекта:
Он реализует метод __iter__() или имеет метод __getitem__().
Возвращает итератор, который можно использовать для последовательного получения элементов.
Примеры итерируемых объектов:
Списки (list):

my_list = [1, 2, 3]
for item in my_list:
    print(item)
	
Кортежи (tuple):
my_tuple = (10, 20, 30)
for item in my_tuple:
    print(item)
	
Строки (str):
my_string = "hello"
for char in my_string:
    print(char)
	
Словари (dict):
my_dict = {"a": 1, "b": 2}
for key in my_dict:
    print(key, my_dict[key])
	
Множества (set):
my_set = {1, 2, 3}
for item in my_set:
    print(item)
	
Диапазоны (range):
for i in range(5):
    print(i)
	
	Дополнительно:
Если объект не является итерируемым, при попытке использовать его в цикле for будет выброшено исключение TypeError.

	2. Что такое break и где он может быть полезен?
break:
Команда break немедленно завершает выполнение текущего цикла (for или while) и продолжает выполнение программы после цикла.
Пример использования:
for i in range(10):
    if i == 5:
        break  # Остановка цикла при достижении числа 5
    print(i)
Вывод:
0
1
2
3
4

Где полезен break:
Преждевременное завершение цикла:
Если нет смысла продолжать выполнение цикла после достижения определенного условия.
Поиск элемента:
Найти нужный элемент и выйти из цикла, чтобы не продолжать ненужные итерации.

items = [10, 20, 30, 40, 50]
for item in items:
    if item == 30:
        print("Элемент найден!")
        break
		
	3. Что такое continue?
continue:
Команда continue завершает текущую итерацию цикла и переходит к следующей, пропуская оставшийся код внутри цикла.
Пример использования:

for i in range(10):
    if i % 2 == 0:  # Пропуск четных чисел
        continue
    print(i)
Вывод:
1
3
5
7
9

Где полезен continue:
Пропуск ненужных итераций:
Если нужно пропустить определенные элементы при выполнении цикла.
Фильтрация данных:

for item in range(10):
    if item < 5:  # Пропустить числа меньше 5
        continue
    print(item)
	
Сравнение break и continue:

break -> Прерывает выполнение всего цикла (Завершение поиска после нахождения элемента)
continue -> Пропускает текущую итерацию и переходит к следующей	(Пропуск обработки определенных элементов)
	Обе команды полезны для управления потоком цикла, чтобы оптимизировать его выполнение."""


""" 6. Программиста попросили написать кусок кода, который проверяет, что
пользователь совершеннолетний или он является администратором. Если одно из
этих условий истинно, то ему предоставляют доступ, в противном случае доступ
запрещен. Но что-то пошло не так и код работает совсем не так, что нужно
исправить?"""

# age = 17
# admin = True
#
# if age <= 18 or admin:
#     print("Доступ разрешен!")
# else:
#     print("Доступ запрещен!")
