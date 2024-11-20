first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

# Создаем генераторную сборку first_result
# Используем zip для попарного перебора строк из списков first и second
# Проверяем условие: длины строк не равны, если это так, вычисляем разницу длин
first_result = (
    abs(len(f) - len(s)) # Вычисляем разницу длин строк
    for f, s in zip(first, second) # f - элемент из first, s - элемент из second
    if len(f) != len(s)) # Условие: длина не равна

# Создаем генераторную сборку second_result
# Для доступа к строкам на одинаковых позициях используем индексы
# Итерируемся по диапазону от 0 до длины списка first (или second, так как длины равны)
second_result = (
    len(first[i]) == len(second[i]) # Сравниваем длины строк с одинаковыми индексами
    for i in range(len(first)) # Итерируемся по индексам
                 )

# Выводим результаты в виде списков
print(list(first_result))
print(list(second_result))