from module_12_1 import Runner  # Импортируем Runner из исходного кода.
import unittest

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        # Создаём объект Runner
        run = Runner('Васёк')

        # Вызываем метод walk 10 раз
        for i in range(10):
            run.walk()

        # Cравниваем distance этого объекта со значением 50 с помощью assertEqual
        self.assertEqual(run.distance, 50, 'очень важное сообщение, которое выскочет в случае провала тестирования')

    def test_run(self):
        # Создаём объект Runner
        run = Runner('Клава')

        # Вызываем метод walk 10 раз.
        for i in range(10):
            run.run()

        # Сравниваем distance этого объекта со значением 100 с помощью assertEqual
        self.assertEqual(run.distance, 100, "Дистанция должна быть равна 100 после 10 пробежек.")

    def test_challenge(self):
        # Создаём 2 объекта Runner
        run = Runner('Павел')
        run2 = Runner('кто-то')

        # 10 раз вызываем методы run и walk
        for i in range(10):
            run.run()
            run2.walk()
        # Используем метод assertNotEqual, т.к дистанции должны быть разными
        self.assertNotEqual(run.distance, run2.distance)


if __name__ == "__main__":
    unittest.main()
