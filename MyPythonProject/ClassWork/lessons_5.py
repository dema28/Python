# print("Числа:")
# tp = type(1)
# print(tp)
# print(type(17))
# print(type(100))
# print()
#
# print("Строки:")
# print(type("Hello"))
# print(type("33dgd"))
# print(type(""))



# class User:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# user1 = User("Jack", 20)
# user2 = User("Mike", 25)
#
# print(user1.name, user1.age)
# print(user2.name, user2.age)


# class User:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def greet(self):
#         print(f"Hi, {self.name}!")
#
#
#
# user1 = User("Jack", 20)
# user2 = User("Mike", 25)


# class User:
#     def __init__(self, name, age):
#         self.name = name
#         self._age = age
#         self._ban = False
#
#     def greet(self):
#         print(f"Hi, {self.name}!")
#
#     def set_age(self, age):
#         if type(age) == int and age >= 0:
#             self._age = age
#         else:
#             print("Не удалось сменить возраст")
#
#     def get_age(self):
#         return self._age
#
#     @staticmethod
#     def is_correct_age(age):
#         return type(age) == int and age >= 0
#
#
# user1 = User("Jack", 20)
# user2 = User("Mike", 25)
#
# user1.greet()
#
# user1.set_age(21)
# print(user1.get_age())


# class User:
#     def __init__(self, name, age):
#         self.name = name
#         self._age = age
#         self._ban = False
#
#     def greet(self):
#         print(f"Hi, {self.name}!")
#
#     def set_age(self, age):
#         if self.is_correct_age(age):
#             self._age = age
#         else:
#             print("Не удалось сменить возраст")
#
#     def get_age(self):
#         return self._age
#
#     @staticmethod
#     def is_correct_age(age):
#         return type(age) == int and age >= 0
#
#
# user1 = User("Jack", 20)
# user2 = User("Mike", 25)
#
# user1.greet()
# user1.set_age(25)
# print(User.is_correct_age(100))

# class User:
#
#     COUNT = 0
#
#     def __init__(self, name, age):
#         self.name = name
#         self._age = age
#         self._ban = False
#         User.add_one_to_count()
#
#     def greet(self):
#         print(f"Hi, {self.name}!")
#
#     def set_age(self, age):
#         if self.is_correct_age(age):
#             self._age = age
#         else:
#             print("Не удалось сменить возраст")
#
#     def get_age(self):
#         return self._age
#
#     def get_info(self):
#         return (self.name, self._age, self._ban)
#
#     @staticmethod
#     def is_correct_age(age):
#         return type(age) == int and age >= 0
#
#     @classmethod
#     def add_one_to_count(cls):
#         cls.COUNT += 1
#
#
#
# user1 = User("Jack", 20) # __init__
# user2 = User("Mike", 25)
# user3 = User("Slava", 26)
#
# print(user1.get_age())
# print(user1.get_info())



# class URL:
#     DOMAIN = "google.com"
#     HOME = "google.com/home"
#     SETTINGS = "google.com/settings"
#
#
# print(URL.HOME)
# print(URL.SETTINGS)

# from classes import User
#
#
# jack = User("Jack", 12)
# oksana = User("Oksana", 28)
#
# jack.greet()
# oksana.greet()
#
# jack.set_age(25)
#
# oksana.get_age()
#
# print(User.COUNT)


# class User:
#     def __init__(self, name, age):
#         self.name = name
#         self._age = age
#         self._ban = False
#
#     def greet(self):
#         print(f"Hi, {self.name}!")
#
#     def set_age(self, age):
#         if self.is_correct_age(age):
#             self._age = age
#         else:
#             print("Не удалось сменить возраст")
#
#     def get_age(self):
#         return self._age
#
#     def get_info(self):
#         return (self.name, self._age, self._ban)
#
#     @staticmethod
#     def is_correct_age(age):
#         return type(age) == int and age >= 0
#
#
# class PremiumUser(User):
#     def __init__(self, name, age, desc):
#         super().__init__(name, age)
#         self.desc = desc
#
#     def greet(self):
#         print(f"***Hi, {self.name}!***")
#
#     def set_desc(self, desc):
#         self.desc = desc
#
#
# pr_user = PremiumUser("Oksana", 28, "Привет, меня зовут Окс!")
# user1 = User("Jack", 40)
#
# pr_user.set_desc("Привет!!!")
# print(pr_user.desc)
