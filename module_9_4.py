# Задача 1: Lambda-функция
# Даны две строки
first = 'Мама мыла раму'
second = 'Рамена мало было'

# Используем lambda-функцию для сравнения символов в одинаковых позициях
# map проходит по парам символов из first и second
# lambda f, s: f == s возвращает True, если символы совпадают, иначе False
result = list(map(lambda f, s: f == s, first, second))
print(result)

#---------------------------------------------------------------------------
# Задача 2: Замыкание
# Функция get_advanced_writer создаёт замыкание
def get_advanced_writer(file_name):
    # Внутренняя функция write_everything принимает любое количество данных
    def write_everything(*data_set):
        # Открываем файл с именем file_name в режиме записи
        with open(file_name, 'w', encoding='utf-8') as file:
            # Проходим по всем элементам data_set
            for data in data_set:
                # Преобразуем текущий элемент в строку и записываем в файл
                file.write(str(data) + '\n')
    # Возвращаем внутреннюю функцию, чтобы использовать её снаружи
    return write_everything

# Создаём функцию записи, указывая имя файла
write = get_advanced_writer('example.txt')

# Записываем данные в файл
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

# ------------------------------------------------------------------------------------------

# Задача 3: Класс MysticBall с методом __call__
from random import choice  # Импортируем функцию choice для случайного выбора элемента

# Создаём класс MysticBall
class MysticBall:
    def __init__(self, *words):
        # Храним переданные слова в атрибуте words
        self.words = words

    # Метод __call__ делает объект вызываемым, как функцию
    def __call__(self):
        # Случайным образом выбираем слово из списка words
        return choice(self.words)

# Создаём объект класса MysticBall с заданными словами
first_ball = MysticBall('Да', 'Нет', 'Наверное')

# Вызываем объект как функцию несколько раз
print(first_ball())
print(first_ball())
print(first_ball())

# ------------------------------------------------------------------------------------------
