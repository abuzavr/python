from threading import Thread  # Для работы с потоками
import time  # Для создания задержек

# Создаём класс Knight, который наследуется от класса Thread
class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()  # Вызываем конструктор родительского класса Thread
        self.name = name  # Имя рыцаря
        self.power = power  # Сила рыцаря
        self.enemies = 100  # У каждого рыцаря своё количество врагов (100 в начале)

    def run(self):
        """
        Метод run запускается, когда мы вызываем start() на объекте потока.
        Здесь описывается, как рыцарь сражается.
        """
        days = 0  # Счётчик дней, сколько времени рыцарь сражается
        print(f"{self.name}, на нас напали!")  # Сообщение о начале битвы
        while self.enemies > 0:  # Пока есть враги
            days += 1  # Начался новый день
            time.sleep(1)  # Ждём 1 секунду, чтобы имитировать 1 день сражения
            # Уменьшаем количество врагов на силу рыцаря (но не ниже 0)
            self.enemies = max(self.enemies - self.power, 0)
            # Сообщаем о текущем статусе сражения
            print(f"{self.name}, сражается {days} день(дня)..., осталось {self.enemies} воинов.")
        # Когда враги закончились, выводим сообщение о победе
        print(f"{self.name} одержал победу спустя {days} дней(дня)!")


# Создаём двух рыцарей с их именами и силой
first_knight = Knight('Sir Lancelot', 10)  # Рыцарь с именем Sir Lancelot, сила 10
second_knight = Knight('Sir Galahad', 20)  # Рыцарь с именем Sir Galahad, сила 20

# Запускаем потоки, чтобы рыцари начали сражаться
first_knight.start()  # Sir Lancelot начинает бой
second_knight.start()  # Sir Galahad начинает бой

# Ожидаем завершения работы потоков
first_knight.join()  # Ждём, пока Sir Lancelot завершит бой
second_knight.join()  # Ждём, пока Sir Galahad завершит бой

# Когда оба рыцаря закончили, выводим финальное сообщение
print("Все битвы закончились!")
