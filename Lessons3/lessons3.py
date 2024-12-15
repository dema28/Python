# numbers = []
# items = [1, 2, 3, True, "hello", [1, 2]]
# numbers = [5, 45, 33, 123, 1, 2, 3, 45]

# numbers[2] = 100
# del numbers[3]

# print(numbers[2:])
# print(numbers[-2])
# print(numbers[1:5])
# print(numbers[2:])
# print(numbers[:5])
# string = "Hello world"
# print(string[::-1])
# print(string[1:4:2])
# print(string[1])
# print(string[2:5])

#numbers = [4]

# numbers.append("Hello")
# numbers.append(True)
# print(numbers)
# numbers.append([1, 2, 3])
# numbers.insert(100, 100)
# print(numbers)
# num = numbers.pop(1)
#
# print(num)
# numbers.clear()

#numbers = [5, 45, 33, 123, 1, 2, 3, 45]

# print(sorted(numbers))
# print(len(numbers))
# print(sum(numbers))
# print(max(numbers), min(numbers))

# "Hello", range(10), [1, 2, 3]

# numbers = [10, 5, 45, 33, 123, 6, 1, 2, 3, 45, 8]
# filtered_numbers = []
#
# for i in numbers:
#     if i % 2 == 0:
#         filtered_numbers.append(i)
#
# print(filtered_numbers)

# numbers = []
#
# for i in range(1, 10):
#     if i % 2 == 0:
#         numbers.append(i + 1)
#
# print(numbers)
#
# numbers_2 = [i + 1 for i in range(1, 10) if i % 2 == 0]
# print(numbers_2)

# [1, 2, 3]
# 1, 1.0, None, True, "hello"

# a = 1
# b = a
# b += 1
# print(a)
# print(b)

# numbers = [1, 2, 3]
# print(id(numbers))
# numbers_2 = numbers.copy()
# print(id(numbers_2))
# print(numbers)
# print(numbers_2)

# numbers_2.append(4)
#
# print(numbers)
# print(numbers_2)

# items = (1, 2, 3, 4, 1, 1, 1, "True", [1, 2, 3], 1.23, 1.34)
# numbers = []
#
# # 1 - int, "hey" - str, True - bool, 1.0 - float, [1, 2] - list, (1, 2) tuple
#
# for i in items:
#     if isinstance(i, (int, float)):
#         numbers.append(i)
#
# print(numbers)


# numbers = (343, 33, 1, 0, 5)
# sorted_numbers = sorted(numbers)
#
# print(tuple(sorted_numbers))

# info = {"name": "Juliana", "age": 35, "admin": True, 100: False}
#
# info["name"] = "Maria"
# print(info["name"])
# print(info[100])

# admins = [{"name": "Juliana", "age": 35, "admin": True, 100: False},
#           {"name": "Ksenia", "age": 22, "admin": True, 100: False, "info": {1: True}},
#           {"name": "Maria", "age": 20, "admin": True, 100: False}]
#
#
# print(admins[1]["info"][1])



# surname = info.get("surname", "Фамилия не указана!")
# surname = info.setdefault("surname", "Фамилия не указана!")

# print(info.keys())
# print(info.values())
# print(info.items())
#
# admins = [{"name": "Juliana", "age": 35, "admin": True, 100: False},
#           {"name": "Ksenia", "age": 22, "admin": True, 100: False, "info": {1: True}},
#           {"name": "Maria", "age": 20, "admin": True, 100: False}]
#
# new_admins = []
#
# for admin in admins:
#     if admin["age"] > 20:
#         new_admins.append(admin)
#
# print(new_admins)

# info = {"Sasha": 31, "Evgenia": 22}
#
# print("a" in "abc")
# print(1 in [1, 2, 3])
#
# print("Maria" in info)
# print(len(info))
# info["Katya"] = 20
# info["Katya"] = 30
# print(info)

# numbers = [1, 2, 343, 43, 34, 1, 1]
# count = {}
#
# for i in numbers:
#     count.setdefault(i, 0)
#     count[i] += 1
#
# print(count)

# set_a = {1, 2, 3, 4}
# set_b = {3, 4, 5, 6}
#
# print(set_a.union(set_b))
# print(set_a.intersection(set_b))

# set_a = {'a', 'b', 'c'}
# set_a.add('a')
#
# print(set_a)

# numbers = [1, 2, 3, 3, 3, 4]
# set_numbers = set(numbers)
#
# print(set_numbers)

# numbers = [15, 3, 8, 42, 3, 23, 8, 7, 42, 1, 9, 23, 15, 5, 9, 4, 6, 1]
#
# print(sorted(set(numbers)))