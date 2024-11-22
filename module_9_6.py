def all_variants(text):
    """
    Генератор, возвращающий все подпоследовательности строки text в порядке длины.
    """
    n = len(text)  # Длина строки
    for length in range(1, n + 1):  # Перебираем длины подпоследовательностей
        for start in range(n - length + 1):  # Перебираем стартовые позиции
            yield text[start:start + length]  # Возвращаем срез строки



a = all_variants("abc")
for i in a:
    print(i)
