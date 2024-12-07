import unittest
import logging
from module_12_4 import Runner  # Импортируем класс Runner

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,  # Уровень логирования - INFO
    filename='runner_tests.log',  # Файл для логирования
    filemode='w',  # Режим записи - замена ('w')
    encoding='utf-8',  # Кодировка - UTF-8
    format='%(asctime)s - %(levelname)s - %(message)s'  # Формат вывода
)


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        """
        Тест: проверяем обработку отрицательной скорости.
        """
        try:
            # Создаём бегуна с отрицательной скоростью
            runner = Runner("Вася", speed=-5)
            runner.walk()
            logging.info('"test_walk" выполнен успешно')
        except ValueError as e:
            # Логируем исключение на уровне WARNING
            logging.exception("Неверная скорость для Runner: %s", e)

    def test_run(self):
        """
        Тест: проверяем обработку некорректного имени.
        """
        try:
            # Создаём бегуна с некорректным именем
            runner = Runner(123, speed=10)
            runner.run()
            logging.info('"test_run" выполнен успешно')
        except TypeError as e:
            # Логируем исключение на уровне WARNING
            logging.exception("Неверный тип данных для объекта Runner: %s", e)


if __name__ == "__main__":
    unittest.main()
