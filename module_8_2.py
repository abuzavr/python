def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for i in numbers:
        try:
            # Попытка добавить элемент к результату, если это число
            result += i
        except TypeError:
            # Обработка исключения, если элемент не числового типа
            print(f'Некорректный тип данных для подсчёта суммы - {i}')
            incorrect_data += 1
    return result, incorrect_data


def calculate_average(numbers):
    try:
        # Вызываем personal_sum для получения суммы и числа некорректных данных
        total, incorrect_data = personal_sum(numbers)
        # Вычисляем количество корректных данных
        correct_data = len(numbers) - incorrect_data
        # Выполняем деление с обработкой ZeroDivisionError на случай пустой коллекции
        try:
            return total / correct_data
        except ZeroDivisionError:
            return 0  # Возвращаем 0, если деление на ноль невозможно
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None


print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать
