class Horse:
    def __init__(self):
        self.x_distance = 0
        self.sound = 'Frrr'

    def run(self, dx):
        self.x_distance += dx

class Eagle:
    def __init__(self):
        self.y_distance = 0
        self.sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy):
        self.y_distance += dy


class Pegasus(Horse, Eagle):
    def __init__(self):
        Horse.__init__(self)
        Eagle.__init__(self)

    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)

    def get_pos(self):
        return (self.x_distance, self.y_distance)

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
