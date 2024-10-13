# Класс Horse описывает лошадь
class Horse:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # Вызов конструктора следующего класса по MRO
        self.x_distance = 0  # начальная дистанция по оси X
        self.sound = 'Frrr'  # звук лошади

    # Метод увеличивает пройденную дистанцию
    def run(self, dx):
        self.x_distance += dx


# Класс Eagle описывает орла
class Eagle:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # Вызов конструктора следующего класса по MRO
        self.y_distance = 0  # начальная высота по оси Y
        self.sound = 'I train, eat, sleep, and repeat'  # звук орла

    # Метод увеличивает высоту полета
    def fly(self, dy):
        self.y_distance += dy


# Класс Pegasus наследует от Horse и Eagle
class Pegasus(Horse, Eagle):
    def __init__(self):
        super().__init__()  # Вызов super(), который пойдёт по цепочке MRO и инициализирует все родительские классы

    # Метод перемещения
    def move(self, dx, dy):
        self.run(dx)  # вызов метода run из Horse для перемещения по X
        self.fly(dy)  # вызов метода fly из Eagle для перемещения по Y

    # Метод для получения текущей позиции
    def get_pos(self):
        return (self.x_distance, self.y_distance)

    # Метод для вывода звука
    def voice(self):
        print(self.sound)


# Пример использования
p1 = Pegasus()

print(p1.get_pos())  # начальная позиция
p1.move(10, 15)  # перемещение
print(p1.get_pos())  # новая позиция
p1.move(-5, 20)  # ещё одно перемещение
print(p1.get_pos())  # обновлённая позиция
p1.voice()  # вывод звука
