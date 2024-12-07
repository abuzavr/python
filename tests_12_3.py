from module_12_2 import Runner, Tournament
import unittest

# Декоратор для пропуска тестов, если is_frozen = True
def skip_if_frozen(test_func):
    """Пропускает тест, если is_frozen = True."""
    def wrapper(self, *args, **kwargs):
        if self.is_frozen:
            self.skipTest("Тесты в этом кейсе заморожены")
        return test_func(self, *args, **kwargs)
    return wrapper


class RunnerTest(unittest.TestCase):
    is_frozen = False  # Этот класс активен

    @skip_if_frozen
    def test_run(self):
        """
        Тест на проверку корректности создания бегуна.
        """
        runner = Runner("Усэйн", speed=10)
        self.assertEqual(runner.name, "Усэйн")
        self.assertEqual(runner.speed, 10)

    @skip_if_frozen
    def test_walk(self):
        """
        Тест на проверку скорости бегуна.
        """
        runner = Runner("Ник", speed=3)
        self.assertEqual(runner.speed, 3)


class TournamentTest(unittest.TestCase):
    is_frozen = True  # Этот класс заморожен

    @classmethod
    def setUpClass(cls):
        """
        Метод вызывается один раз перед запуском всех тестов.
        Инициализируем общий словарь для хранения результатов тестов.
        """
        cls.all_results = {}  # Словарь для хранения результатов всех тестов

    def setUp(self):
        """
        Метод вызывается перед каждым тестом.
        Создаём участников: Усэйн, Андрей, Ник.
        """
        self.usain = Runner("Усэйн", speed=10)  # Быстрый бегун
        self.andrey = Runner("Андрей", speed=9)  # Средний бегун
        self.nick = Runner("Ник", speed=3)  # Самый медленный бегун

    @classmethod
    def tearDownClass(cls):
        """
        Метод вызывается один раз после выполнения всех тестов.
        Выводим результаты всех тестов в столбец.
        """
        for result_name, result in cls.all_results.items():
            print(result)

    def run_tournament_and_test(self, test_name, participants, expected_last):
        """
        Вспомогательный метод для создания турнира, запуска и тестирования.
        :param test_name: Имя теста для сохранения результата.
        :param participants: Участники турнира.
        :param expected_last: Ожидаемый последний бегун.
        """
        tournament = Tournament(90, *participants)
        results = tournament.start()
        # Преобразуем результаты в словарь с именами бегунов
        named_results = {place: str(runner) for place, runner in results.items()}
        TournamentTest.all_results[test_name] = named_results
        self.assertTrue(named_results[max(named_results.keys())] == expected_last)

    @skip_if_frozen
    def test_usain_and_nick(self):
        """
        Тест на забег Усэйна и Ника.
        """
        self.run_tournament_and_test(
            "test_usain_and_nick",
            [self.usain, self.nick],
            expected_last="Ник"
        )

    @skip_if_frozen
    def test_andrey_and_nick(self):
        """
        Тест на забег Андрея и Ника.
        """
        self.run_tournament_and_test(
            "test_andrey_and_nick",
            [self.andrey, self.nick],
            expected_last="Ник"
        )

    @skip_if_frozen
    def test_usain_andrey_and_nick(self):
        """
        Тест на забег Усэйна, Андрея и Ника.
        """
        self.run_tournament_and_test(
            "test_usain_andrey_and_nick",
            [self.usain, self.andrey, self.nick],
            expected_last="Ник"
        )


if __name__ == "__main__":
    unittest.main()
