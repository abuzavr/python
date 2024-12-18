import threading
from time import sleep, time


# Функция записи слов в файл
def write_words(word_count, file_name):
    with open(file_name, 'w') as file:  # Открываем файл на запись
        for i in range(1, word_count + 1):  # Цикл от 1 до word_count включительно
            file.write(f"Какое-то слово № {i}\n")  # Пишем строку в файл
            sleep(0.1)  # Ждём 0.1 секунды перед записью следующей строки
    print(f"Завершилась запись в файл {file_name}")  # Сообщаем, что запись завершена


# Основной блок программы
if __name__ == "__main__":
    # Измерение времени выполнения без потоков
    start_time = time()

    # Последовательный вызов функций
    write_words(10, "example1.txt")
    write_words(30, "example2.txt")
    write_words(200, "example3.txt")
    write_words(100, "example4.txt")

    end_time = time()
    print(f"Работа функций заняла: {end_time - start_time:.2f} секунд")

    # Измерение времени выполнения с потоками
    start_time = time()

    # Создание потоков
    thread1 = threading.Thread(target=write_words, args=(10, "example5.txt"))
    thread2 = threading.Thread(target=write_words, args=(30, "example6.txt"))
    thread3 = threading.Thread(target=write_words, args=(200, "example7.txt"))
    thread4 = threading.Thread(target=write_words, args=(100, "example8.txt"))

    # Запуск потоков
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()

    # Ожидание завершения потоков
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()

    end_time = time()
    print(f"Работа потоков заняла: {end_time - start_time:.2f} секунд")
