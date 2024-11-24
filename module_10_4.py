import threading
import time
import random
from queue import Queue

class Table:
    """Класс для стола."""
    def __init__(self, number):
        self.number = number  # Номер стола
        self.guest = None  # Гость за столом (изначально None)

class Guest(threading.Thread):
    """Класс для гостя, представляющий поток."""
    def __init__(self, name):
        super().__init__()
        self.name = name  # Имя гостя

    def run(self):
        """Метод запуска потока (гость кушает)."""
        dining_time = random.randint(3, 10)  # Время пребывания от 3 до 10 секунд
        time.sleep(dining_time)  # Имитируем время приёма пищи

class Cafe:
    """Класс для кафе."""
    def __init__(self, *tables):
        self.tables = list(tables)  # Список столов
        self.queue = Queue()  # Очередь для гостей

    def guest_arrival(self, *guests):
        """Метод прибытия гостей."""
        for guest in guests:
            # Проверяем наличие свободного стола
            for table in self.tables:
                if table.guest is None:
                    table.guest = guest  # Сажаем гостя за стол
                    guest.start()  # Запускаем поток гостя
                    print(f"{guest.name} сел(-а) за стол номер {table.number}")
                    break
            else:
                # Если столов нет, добавляем гостя в очередь
                self.queue.put(guest)
                print(f"{guest.name} в очереди")

    def discuss_guests(self):
        """Метод обслуживания гостей."""
        while not self.queue.empty() or any(table.guest is not None for table in self.tables):
            for table in self.tables:
                if table.guest is not None:
                    if not table.guest.is_alive():  # Проверяем, закончил ли гость кушать
                        print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
                        print(f"Стол номер {table.number} свободен")
                        table.guest = None  # Освобождаем стол

                # Если очередь не пуста и стол освободился
                if table.guest is None and not self.queue.empty():
                    next_guest = self.queue.get()  # Берём гостя из очереди
                    table.guest = next_guest  # Сажаем за стол
                    next_guest.start()  # Запускаем поток гостя
                    print(f"{next_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")

            time.sleep(0.5)  # Небольшая задержка для имитации времени обслуживания


# Код для тестирования
if __name__ == "__main__":
    # Создание столов
    tables = [Table(number) for number in range(1, 6)]

    # Имена гостей
    guests_names = [
        'Наташа', 'Александр', 'Евгений', 'Сергей', 'Юля', 'Валерий',
        'Кирилл', 'Дарья', 'Галя', 'Паша', 'Лида', 'Александр'
    ]

    # Создание гостей
    guests = [Guest(name) for name in guests_names]

    # Заполнение кафе столами
    cafe = Cafe(*tables)

    # Приём гостей
    cafe.guest_arrival(*guests)

    # Обслуживание гостей
    cafe.discuss_guests()
