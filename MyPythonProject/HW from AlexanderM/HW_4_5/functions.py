# functions.py

def sum_ignore_non_numbers(items):
    """
    Возвращает сумму всех чисел (int, float) в переданной последовательности.
    Все нечисловые значения игнорируются. Если чисел нет, возвращает 0.

    Args:
        items (list | tuple): Последовательность элементов для подсчёта суммы.

    Returns:
        float: Сумма числовых элементов.
    """
    return sum(item for item in items if isinstance(item, (int, float)))

def is_triangle(a, b, c):
    """
    Определяет, может ли существовать треугольник с заданными сторонами.

    Условия существования треугольника: сумма любых двух сторон должна быть больше третьей стороны.

    Args:
        a (float): Длина первой стороны.
        b (float): Длина второй стороны.
        c (float): Длина третьей стороны.

    Returns:
        bool: True, если треугольник может существовать, иначе False.
    """
    return a + b > c and a + c > b and b + c > a

def average(*args):
    """
    Вычисляет среднее арифметическое из произвольного количества чисел.

    Если аргументы не переданы, возвращает 0.

    Args:
        *args (float): Числа для вычисления среднего значения.

    Returns:
        float: Среднее арифметическое или 0, если аргументы отсутствуют.
    """
    return sum(args) / len(args) if args else 0

def common_strings(list1, list2, ignore_case=True):
    """
    Возвращает список строк, которые присутствуют в обоих списках.

    Если ignore_case=True, регистр игнорируется, и строки приводятся к нижнему регистру.
    Если ignore_case=False, строки сравниваются с учётом регистра.

    Args:
        list1 (list): Первый список строк.
        list2 (list): Второй список строк.
        ignore_case (bool): Игнорировать ли регистр при сравнении строк. По умолчанию True.

    Returns:
        list: Список строк, присутствующих в обоих списках.
    """
    def convert_to_lower(string):
        return string.lower() if ignore_case else string

    transformed_list1 = [convert_to_lower(item) for item in list1]
    transformed_list2 = [convert_to_lower(item) for item in list2]

    return list(set(transformed_list1).intersection(transformed_list2))
