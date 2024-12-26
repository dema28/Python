# import requests
#
# BASE_URL = "https://restful-booker.herokuapp.com"
# HEADERS = {"Content-Type": "application/json"}
#
# """ 1. Тест: Получение всех id всех бронирований.
# GET
# - Создайте тест для получения списка всех id всех бронирований на сайте.
# - Тест считается пройденным, если status code ответа равен 200. """
# def test_get_all_bookings():
#     response = requests.get(f"{BASE_URL}/booking")
#     assert response.status_code == 200, f"Expected 200, got {response.status_code}"
#     print("Test 1 passed: GET all bookings")
#
# """" 2. Тест: Создание и проверка бронирования. POST
#
# Создайте тест, который включает в себя следующие шаги:
# - Шаг 1. Создайте новое бронирование на сайте используя ваши данные.
# - Шаг 2. C помощью id вашего созданного бронирования получите
# информацию о вашем бронировании (через эндпоинт booking/{id}).
# - Тест считается пройденным, если имя и фамилия в вашем созданном
# бронировании (Шаг 1) совпадают с теми данными, которые вы получили.
# (Шаг 2)"""
# def test_create_and_verify_booking():
#     # Шаг 1: Создание бронирования
#     booking_data = {
#         "firstname": "John",
#         "lastname": "Doe",
#         "totalprice": 150,
#         "depositpaid": True,
#         "bookingdates": {"checkin": "2024-12-01", "checkout": "2024-12-10"},
#         "additionalneeds": "Breakfast"
#     }
#     response = requests.post(f"{BASE_URL}/booking", json=booking_data, headers=HEADERS)
#     assert response.status_code == 200, f"Expected 200, got {response.status_code}"
#     booking_id = response.json().get("bookingid")
#
#     # Шаг 2: Получение информации о бронировании
#     response = requests.get(f"{BASE_URL}/booking/{booking_id}")
#     assert response.status_code == 200, f"Expected 200, got {response.status_code}"
#     booking_details = response.json()
#
#     assert booking_data["firstname"] == booking_details["firstname"], "Firstname mismatch"
#     assert booking_data["lastname"] == booking_details["lastname"], "Lastname mismatch"
#     print("Test 2 passed: Create and verify booking")
#
# """" 3. Тест: Изменение бронирования. PATCH
#
# Создайте тест, который включает в себя следующие шаги:
# - Шаг 1. Создайте новое бронирование на сайте используя ваши данные.
# - Шаг 2. Создайте токен авторизации.
# - Шаг 3. Измените имя и фамилию в вашей брони через метод PATCH. (не
# забудьте передать в заголовке токен авторизации)
# - Шаг 4. C помощью id вашего созданного бронирования получите
# информацию о вашем бронировании.
#
# - Тест считается пройденным, если имя и фамилия в вашем измененном
# бронировании (Шаг 3) совпадают с теми данными, которые вы получили.
# (Шаг 4)"""
# def test_update_booking():
#     # Шаг 1: Создание бронирования
#     booking_data = {
#         "firstname": "Alice",
#         "lastname": "Smith",
#         "totalprice": 200,
#         "depositpaid": False,
#         "bookingdates": {"checkin": "2024-12-05", "checkout": "2024-12-15"},
#         "additionalneeds": "Dinner"
#     }
#     response = requests.post(f"{BASE_URL}/booking", json=booking_data, headers=HEADERS)
#     assert response.status_code == 200, f"Expected 200, got {response.status_code}"
#     booking_id = response.json().get("bookingid")
#
#     # Шаг 2: Создание токена авторизации
#     auth_data = {"username": "admin", "password": "password123"}
#     auth_response = requests.post(f"{BASE_URL}/auth", json=auth_data, headers=HEADERS)
#     assert auth_response.status_code == 200, f"Expected 200, got {auth_response.status_code}"
#     token = auth_response.json()["token"]
#     auth_headers = {**HEADERS, "Cookie": f"token={token}"}
#
#     # Шаг 3: Изменение имени и фамилии
#     update_data = {"firstname": "Bob", "lastname": "Brown"}
#     patch_response = requests.patch(f"{BASE_URL}/booking/{booking_id}", json=update_data, headers=auth_headers)
#     assert patch_response.status_code == 200, f"Expected 200, got {patch_response.status_code}"
#
#     # Шаг 4: Проверка изменений
#     response = requests.get(f"{BASE_URL}/booking/{booking_id}")
#     assert response.status_code == 200, f"Expected 200, got {response.status_code}"
#     updated_details = response.json()
#
#     assert update_data["firstname"] == updated_details["firstname"], "Firstname mismatch after update"
#     assert update_data["lastname"] == updated_details["lastname"], "Lastname mismatch after update"
#     print("Test 3 passed: Update booking")
#
# """ 4. Тест: Удаление бронирования. DELETE
#
# Создайте тест, который включает в себя следующие шаги:
# - Шаг 1. Создайте новое бронирование на сайте используя ваши данные.
# - Шаг 2. Создайте токен авторизации.
# - Шаг 3. Удалите ваше бронирование по его id через метод DELETE. (не
# забудьте передать в заголовке токен авторизации)
#
# - Тест считается пройденным, если попытка получения информации о вашей
# брони по ее id возвращает статус 404 (Not Found)."""
# def test_delete_booking():
#     # Шаг 1: Создание бронирования
#     booking_data = {
#         "firstname": "Jane",
#         "lastname": "Doe",
#         "totalprice": 300,
#         "depositpaid": True,
#         "bookingdates": {"checkin": "2024-12-20", "checkout": "2024-12-25"},
#         "additionalneeds": "Lunch"
#     }
#     response = requests.post(f"{BASE_URL}/booking", json=booking_data, headers=HEADERS)
#     assert response.status_code == 200, f"Expected 200, got {response.status_code}"
#     booking_id = response.json().get("bookingid")
#
#     # Шаг 2: Создание токена авторизации
#     auth_data = {"username": "admin", "password": "password123"}
#     auth_response = requests.post(f"{BASE_URL}/auth", json=auth_data, headers=HEADERS)
#     assert auth_response.status_code == 200, f"Expected 200, got {auth_response.status_code}"
#     token = auth_response.json()["token"]
#     auth_headers = {**HEADERS, "Cookie": f"token={token}"}
#
#     # Шаг 3: Удаление бронирования
#     delete_response = requests.delete(f"{BASE_URL}/booking/{booking_id}", headers=auth_headers)
#     assert delete_response.status_code == 201, f"Expected 201, got {delete_response.status_code}"
#
#     # Шаг 4: Проверка удаления
#     response = requests.get(f"{BASE_URL}/booking/{booking_id}")
#     assert response.status_code == 404, f"Expected 404, got {response.status_code}"
#     print("Test 4 passed: Delete booking")
#
# # Запуск тестов
# test_get_all_bookings()
# test_create_and_verify_booking()
# test_update_booking()
# test_delete_booking()


""" Повторение прошлого материала.

Ответьте на следующие вопросы:
1. Что такое итерируемый объект? Какие итерируемые объекты вы знаете?
2. Что такое изменяемый или неизменяемый объект? Строка - это изменяемый
или неизменяемый объект?
3. Что такое “генератор”? Как можно сгенерировать список?

Ответы: 1. Что такое итерируемый объект? Какие итерируемые объекты вы знаете?
Итерируемый объект — это объект, который можно перебирать (итерация) с помощью цикла, например for. Итерируемый объект должен иметь метод __iter__(), который возвращает итератор. Итератор, в свою очередь, имеет метод __next__() для последовательного получения значений.

Примеры итерируемых объектов:

Списки (list) — [1, 2, 3]
Кортежи (tuple) — (1, 2, 3)
Строки (str) — "hello"
Множества (set) — {1, 2, 3}
Словари (dict) — {"key": "value"}
Диапазоны (range) — range(1, 5)
Пример:


my_list = [1, 2, 3]
for item in my_list:
    print(item)  # Вывод: 1 2 3
2. Что такое изменяемый или неизменяемый объект? Строка - это изменяемый или неизменяемый объект?
Изменяемые объекты — можно изменить их содержимое после создания. Примеры: list, set, dict.

Неизменяемые объекты — их содержимое нельзя изменить после создания. Примеры: int, float, str, tuple, frozenset.

Строка (str) — это неизменяемый объект. После создания строку нельзя модифицировать, но можно создать новую строку.

Пример:

s = "hello"
# Нельзя изменить символ строки напрямую: s[0] = "H" вызовет ошибку.
# Но можно создать новую строку:
s = "H" + s[1:]  # "Hello"
3. Что такое “генератор”? Как можно сгенерировать список?
Генератор — это объект, который позволяет создавать последовательность значений "лениво" (по мере необходимости). Это похоже на итератор, но значения создаются на лету, что экономит память.

Способы создания генератора:

Генераторное выражение:

gen = (x**2 for x in range(5))
print(next(gen))  # 0
print(next(gen))  # 1
Функция с yield:

def my_gen():
    for i in range(3):
        yield i
gen = my_gen()
print(next(gen))  # 0
Генерация списка:

Через list comprehension:

my_list = [x**2 for x in range(5)]
print(my_list)  # [0, 1, 4, 9, 16] """


""" 1.
Калькулятор

- Создайте класс Calculator с методами add(), mul(), div(), которые
выполняют сложение, умножение, деление двух чисел и возвращающих
результат.
- Калькулятор должен “запоминать” все совершенные операции. Например,
если был вызван метод add(1, 2), то калькулятор должен запомнить это в
виде строки “1 + 2 = 3” и тд.
- Создайте метод show_operations(), который выводит на экран все
совершенные раннее операции.
- Создайте метод clear(), который “чистит память” калькулятора и удаляет
историю операций.
Например, такой код:
calc = Calculator()
calc.add(1, 3)
calc.add(2, 10)
calc.mul(100, 12.2)
calc.show_operations()

Должен вывести:

1 + 3 = 4
2 + 10 = 12
100 * 12.2 = 1220.0 """

class Calculator:
    def __init__(self):
        self.history = []  # Список для хранения истории операций

    def add(self, a, b):
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result

    def sub(self, a, b):
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result

    def mul(self, a, b):
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result

    def div(self, a, b):
        if b == 0:
            self.history.append(f"{a} / {b} = Division by zero error")
            return "Division by zero error"
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result

    def show_operations(self):
        if not self.history:
            print("No operations performed yet.")
        else:
            for operation in self.history:
                print(operation)

    def clear(self):
        self.history = []

# Пример использования:
calc = Calculator()
calc.add(1, 3)
calc.sub(10, 5)
calc.add(2, 10)
calc.mul(100, 12.2)
calc.show_operations()




