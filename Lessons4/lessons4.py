# def greet():
#     print("***")
#     print("Hello world!")
#     print("***")
#
#
# greet()
# greet()

# def greet(name):
#     print(f"Hello, {name}!")
#
#
# greet("Ivan")
# greet("Sergey")

# def add(a, b):
#     print(a + b)
#
# # add(1, 2)
# add(1, 4)
# add(b=4, a=1)


# def add(a, b=10):
#     print(a + b)
#
# add(1, 100)

# def func(*args):
#     print(args)
#
# func()
# func(1, 2)
# func(1, 2, 3, 4, 5, 6, 7, 8)
#
# print()
# print(1, 2)
# print(1, 2, 3, 4, 5, 6)

# def func(a, b, c, *args, **kwargs):
#     print(a, b, c, args, kwargs)
#
#
# func(1, 2, 3, 4, 5, 6, sep="*")

# def func(*args):
#     for i in args:
#         print(i)
#
#
# func(1, 2, 3, "A")

# def func(**kwargs):
#     print(kwargs)
#
#
# func(a=10, c=2)

# numbers = [1, 4, 2]
# sorted_numbers = sorted(numbers)
#
# print(sorted_numbers)
#
# result = print(1, 2)
# print(result)

# def add(a, b):
#     result = a + b
#     return result
#
#
# num = add(1, 2)
#
# print(num)

# def is_digit(value):
#     if isinstance(value, int):
#         return True
#     return False
#
# print(is_digit(12))
# print(is_digit("Hello"))

# numbers = [1, 2, 3, 4, 5, 6]
# sum_numbers = sum(numbers)
#
# print(sum_numbers)


# def my_sum(items):
#     """
#     Суммирует числа из переданного списка.
#
#     :param items: Список чисел.
#     :return: Сумма чисел из списка.
#     """
#
#     total = 0
#
#     for i in items:
#         total += i
#
#     return total
#
# numbers = [1, 2, 3, 4, 5, 6]
#
# result = my_sum([1, 2, 3, 4, 5, 6])
# print(result)


# def func():
#     string = "Локальная"
#     print(string)
#
# string = "Глобальная"
# func()
#
# print(string)

# def add(a, b):
#     result = a + b
#
#     return result
#
#
# def mul(a, b):
#     result = a * b
#
#     return result
#
# print(mul(2, 4))

# from functions import add, mul, div
# import functions as func
#
# a = 2
# b = 10
#
# print(func.add(a, b))
# print(func.mul(4, 5))
# print(func.div(4, 5))


# def add(a, b):
#     return a + b
#
#
# # items = [1, 2, None, add, 56]
# item = add
#
# print(item(1, 5))

# def is_positive(i):
#     return i > 0
#
#
# def is_negative(i):
#     return i < 0


# def filter_by(items, func):
#     new_list = []
#
#     for item in items:
#         if func(item):
#             new_list.append(item)
#
#     return new_list
#
#
# numbers = [1, 2, -12, 123, -7]
# # result = filter_by(numbers, lambda i: i > 0)
# #
# # print(result)
#
# result = filter(lambda i: i > 5, numbers)
#
# print(result)

#
# def mother():
#     a = 20
#     def son():
#         print(a)
#
#     return son


# def calc(a, b):
#     def add(a, b):
#         return a + b
#
#     result = add(a, b)
#
#     return result
#
# num = calc(1, 2)
#
# print(num)


# def decorator(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         print(f"Записываю в логи результата {result}!")
#         return result
#
#     return wrapper
#
# @decorator
# def add(a, b):
#     return a + b
#
# @decorator
# def mul(a, b):
#     return a * b
#
# @decorator
# def div(a, b):
#     return a / b
#
# @decorator
# def my_sum(a, b, c):
#     return a + b + c
#
#
# # add = decorator(add)
# print(add(1, 2))
# print(mul(1, 5))
# print(div(1, 5))
# print(my_sum(1, 2, 3))
























