# """ Напишите программу, которая находит среднее арифметическое четырех чисел.
# Пользователь должен ввести четыре числа с клавиатуры,
# после чего программа должна вычислить их среднее значение и вывести результат на экран."""
#
# num1 = int(input("Введите первое число: "))
# num2 = int(input("Введите второе число: "))
# num3 = int(input("Введите третье число: "))
# num4 = int(input("Введите четвертое число: "))
#
# sum = (num1 + num2 + num3 + num4) / 4
# print(f"Среднее арифметическое чисел: {sum}" )
#
#
# """ Напишите программу, которая получает одно целое число, и вывести его последнюю цифру."""
#
# num = int(input("Введите целое число: "))
# last_digit = num % 10  # Вычисляем последнюю цифру числа, # num % 100 = последняя 2 цифры числа и так далии, если 1000, 3 цифры и так далее
# print(f"Последняя цифра в числе: {last_digit}" )
#
# num = input("Введите целое число: ")
# print(f"Последняя цифра в числе: {num[-1]}" )
#
#
# """ Напишите программу, которая запрашивает у пользователя предложение и слово.
# Программа должна проверить, содержится ли указанное слово в предложении, и вывести результат на экран."""
#
# text = input("Введите предложение: ")
# word = input("Введите слово: ")
#
# if word in text:
#     print(f"{word} содержится в предложении")
#
# """ Напишите программу, которая запрашивает у пользователя предложение и переводит его из строчных букв в верхний регистр."""
#
# text = input("Введите предложение: ")
# print(text.upper())
#
#
# """ Напишите программу, которая запрашивает у пользователя строку с лишними пробелами,
#  в начале и в конце строки и программа должна удалить лишние и вывести чистую строку"""
#
# text = input("Введите текст: ")
# print(text.strip())  # Удаляем лишние пробелы в начале и конце текста
#
#
# """ Напишите программу, которая запрашивает у пользователя строку и два символа."""
#
# text = input("Введите текст: ")
# char1 = input("Введите первый символ: ")
# char2 = input("Введите второй символ: ")
# result = text.replace(char1, char2)  # Заменяем все вхождения char1 на char2 в тексте
# print(result)
#