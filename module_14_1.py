import sqlite3

# Подключение к базе данных (создание файла, если он не существует)
conn = sqlite3.connect("not_telegram.db")
cursor = conn.cursor()

# Создание таблицы Users, если она ещё не создана
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL
)
''')

# Очистка таблицы перед добавлением новых данных
cursor.execute("DELETE FROM Users")

# Заполнение таблицы 10 записями
users_data = [
    (f"User{i}", f"example{i}@gmail.com", i * 10, 1000)
    for i in range(1, 11)
]
cursor.executemany("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", users_data)

# Обновление balance у каждой 2-ой записи начиная с 1-ой на 500
cursor.execute("UPDATE Users SET balance = 500 WHERE id % 2 = 1")

# Удаление каждой 3-ей записи начиная с 1ой. (Временная таблица индексов)
cursor.execute('''
WITH temp AS (
    SELECT id, ROW_NUMBER() OVER (ORDER BY id) AS row_num FROM Users
)
DELETE FROM Users WHERE id IN (SELECT id FROM temp WHERE row_num % 3 = 1)
''')

# Выборка всех записей, где возраст не равен 60
cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != 60")
rows = cursor.fetchall()

# Вывод результатов в консоль
print("Вывод на консоль:")
for row in rows:
    print(f"Имя: {row[0]} | Почта: {row[1]} | Возраст: {row[2]} | Баланс: {row[3]}")

# Сохранение изменений и закрытие подключения
conn.commit()
conn.close()
