import threading
from random import randint
from time import sleep


class Bank:
    def __init__(self):
        """Инициализация объекта банка."""
        self.balance = 0  # Начальный баланс
        self.lock = threading.Lock()  # Блокировка для управления потоками

    def deposit(self):
        """Метод для пополнения баланса."""
        for _ in range(100):  # Совершаем 100 транзакций
            amount = randint(50, 500)  # Случайная сумма пополнения
            with self.lock:  # Защищаем изменение баланса
                self.balance += amount
                print(f"Пополнение: {amount}. Баланс: {self.balance}")
                if self.balance >= 500:
                    pass  # Блокировка снимается автоматически
            sleep(0.001)  # Имитируем задержку пополнения

    def take(self):
        """Метод для снятия средств."""
        for _ in range(100):  # Совершаем 100 транзакций
            amount = randint(50, 500)  # Случайная сумма снятия
            print(f"Запрос на {amount}")
            with self.lock:  # Блокируем поток для проверки и изменения баланса
                if amount <= self.balance:
                    self.balance -= amount
                    print(f"Снятие: {amount}. Баланс: {self.balance}")
                else:
                    print("Запрос отклонён, недостаточно средств")
                    self.lock.acquire()  # Блокируем поток, если денег недостаточно
            sleep(0.001)  # Имитируем задержку снятия


# Создаём объект класса Bank
bk = Bank()

# Создаём два потока: один для пополнения, другой для снятия
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

# Запускаем потоки
th1.start()
th2.start()

# Ожидаем завершения потоков
th1.join()
th2.join()

# Вывод итогового баланса
print(f"Итоговый баланс: {bk.balance}")
