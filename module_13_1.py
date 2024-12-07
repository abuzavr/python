import asyncio

# Асинхронная функция для соревнований силачей
async def start_strongman(name, power):
    """
    Симулирует поднятие шаров Атласа силачом.
    :param name: Имя силача.
    :param power: Мощь силача.
    """
    print(f"Силач {name} начал соревнования.")  # Начало соревнований

    # Поднимаем 5 шаров
    for i in range(1, 6):
        await asyncio.sleep(1 / power)  # Задержка пропорциональна силе
        print(f"Силач {name} поднял {i} шар")

    print(f"Силач {name} закончил соревнования.")  # Конец соревнований


# Асинхронная функция для старта турнира
async def start_tournament():
    """
    Запускаем соревнования для нескольких силачей.
    """
    # Создаём задачи для участников турнира
    tasks = [
        start_strongman("Pasha", 3),
        start_strongman("Denis", 4),
        start_strongman("Apollon", 5),
    ]

    # Запускаем все задачи параллельно
    await asyncio.gather(*tasks)

# Запуск турнира
if __name__ == "__main__":
    asyncio.run(start_tournament())