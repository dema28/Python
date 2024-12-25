from functions import sum_ignore_non_numbers, is_triangle, average, common_strings

# Тестирование функций с различными аргументами

# 1. sum_ignore_non_numbers
print(sum_ignore_non_numbers([1, 2, 'Hey', None, 4.3]))  # 7.3
print(sum_ignore_non_numbers([1, 2, 3, 4]))              # 10
print(sum_ignore_non_numbers([]))                       # 0

# 2. is_triangle
print(is_triangle(2, 4, 9))  # False
print(is_triangle(3, 4, 5))  # True

# 3. average
print(average(1, 2, 3, 4, 5, 6, 7, 8))  # 4.5
print(average())                        # 0

# 4. common_strings
fruits_1 = ['banana', 'APPLE', 'watermelon', 'cherry']
fruits_2 = ['Mango', 'apple', 'orange', 'cherry']
print(common_strings(fruits_1, fruits_2))                  # ['apple', 'cherry']
print(common_strings(fruits_1, fruits_2, ignore_case=False))  # ['cherry']
