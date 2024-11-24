import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Использование Pandas: чтение данных и анализ
print("1. Работа с Pandas")

# Создаем DataFrame с данными
data = pd.DataFrame({
    'Name': ['Женя', 'Вася', 'Юля', 'Давид', 'Ева'],
    'Age': [24, 27, 22, 32, 29],
    'Score': [88, 92, 95, 70, 85]
})

# Пример анализа: расчет среднего возраста
average_age = data['Age'].mean()  # Среднее значение по столбцу 'Age'
print(f"Средний возраст: {average_age}")

# Фильтрация данных: выбор студентов с баллом выше 85
high_scores = data[data['Score'] > 85]  # Условная фильтрация по столбцу 'Score'
print("Студенты с баллом выше 85:")
print(high_scores)

# Добавление нового столбца: возраст в месяцах
data['Age_in_Months'] = data['Age'] * 12  # Преобразование возраста в месяцы
print("Данные с новым столбцом:")
print(data)

# 2. Использование NumPy: работа с массивами
print("\n2. Работа с NumPy")

# Создаем одномерный массив
array = np.array([1, 2, 3, 4, 5])
print("Исходный массив:", array)

# Математические операции: возведение элементов массива в квадрат
squared_array = np.array(array**2)
print("Возведение в квадрат:", squared_array)

# Генерация случайного массива с числами от 0 до 1
random_array = np.random.random(5)
print("Случайный массив:", random_array)

# Нахождение среднего значения массива
mean_value = np.mean(random_array)
print("Среднее значение случайного массива:", mean_value)

# 3. Использование Matplotlib: визуализация данных
print("\n3. Работа с Matplotlib")

# Построение линейного графика y = x^2
plt.plot(array, squared_array, label='y = x^2', marker='o')  # Линия с метками точек
plt.title('График y = x^2')  # Заголовок графика
plt.xlabel('x')  # Подпись оси X
plt.ylabel('y')  # Подпись оси Y
plt.legend()  # Добавляем легенду
plt.grid(True)  # Включаем сетку
plt.savefig("plot_example.png")  # Сохраняем график в файл
plt.show()  # Отображаем график на экране

# Создание гистограммы случайных значений
plt.hist(random_array, bins=5, color='grey', alpha=0.7, edgecolor='black')  # Гистограмма с 5 интервалами
plt.title('Гистограмма случайного массива')  # Заголовок гистограммы
plt.xlabel('Значение')  # Подпись оси X
plt.ylabel('Частота')  # Подпись оси Y
plt.savefig("histogram_example.png")  # Сохраняем гистограмму в файл
plt.show()  # Отображаем гистограмму на экране

# Вывод о проделанной работе
print("\nРабота завершена! Проверьте полученные файлы plot_example.png и histogram_example.png")
