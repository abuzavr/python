import time
from multiprocessing import Pool, cpu_count

def read_info(name):
    """Функция для считывания информации из файла."""
    with open(name, 'r') as file:
        data = file.read()
    return len(data)

if __name__ == '__main__':
    """
    Точка входа в программу. Используется для правильной работы многопроцессного кода.
    """
    # Формируем список файлов для обработки
    filenames = [f'file {number}.txt' for number in range(1, 5)]  # Относительный путь к файлам

    # --- Линейный вызов ---
    start_time = time.time()  # Засекаем время начала выполнения
    for filename in filenames:  # Поочередно проходим по всем файлам
        read_info(filename)  # Вызываем функцию для каждого файла
    linear_duration = time.time() - start_time  # Вычисляем время выполнения
    print(f"Линейный вызов: {linear_duration:.6f} секунд")  # Выводим результат линейного выполнения

    # --- Многопроцессный вызов ---
    start_time = time.time()  # Засекаем время начала выполнения
    with Pool(processes=cpu_count()) as pool:  # Создаём пул процессов, используя все доступные ядра
        pool.map(read_info, filenames)  # Распределяем вызовы функции read_info по процессам
    parallel_duration = time.time() - start_time  # Вычисляем время выполнения
    print(f"Многопроцессный вызов: {parallel_duration:.6f} секунд")  # Выводим результат многопроцессного выполнения