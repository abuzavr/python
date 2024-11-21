class StepValueError(ValueError):
    """Класс исключения для проверки шага."""
    pass


class Iterator:
    """Итератор с шагом."""

    def __init__(self, start, stop, step=1):
        if step == 0:  # Проверяем, чтобы шаг не был равен нулю
            raise StepValueError('Шаг не может быть равен 0')
        self.start = start  # Устанавливаем начальное значение
        self.stop = stop  # Устанавливаем конечное значение
        self.step = step  # Устанавливаем шаг
        self.pointer = start  # Указываем на начальное значение

    def __iter__(self):
        """
        Метод, сбрасывающий значение pointer
        на start и возвращающий сам объект итератора.
        """
        self.pointer = self.start  # Сброс указателя
        return self

    def __next__(self):
        """Увеличивает pointer на step и проверяет завершение итерации."""
        if (self.step > 0 and self.pointer >= self.stop) or (self.step < 0 and self.pointer <= self.stop):
            raise StopIteration  # Завершаем итерацию
        current = self.pointer  # Сохраняем текущее значение
        self.pointer += self.step  # Смещаем указатель на шаг
        return current

try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)

for i in iter2:
    print(i, end=' ')
print()
for i in iter3:
    print(i, end=' ')
print()
for i in iter4:
    print(i, end=' ')
print()
for i in iter5:
    print(i, end=' ')
print()