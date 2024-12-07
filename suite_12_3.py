import unittest
from tests_12_3 import RunnerTest, TournamentTest

# Создание TestSuite
test_suite = unittest.TestSuite()

# Добавление тестов в TestSuite
test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))

# Создание и запуск TextTestRunner
if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(test_suite)
