class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"
#сравниваем количество этажей в домах или с числом
    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        if isinstance(other, int):
            return self.number_of_floors == other

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
        elif isinstance(value, House):
            self.number_of_floors += value.number_of_floors
        return self

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)
#Метод __lt__ : этот метод определяет поведение оператора "меньше чем" <. Он сравнивает текущий объект с другим объектом
    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        return False
#Метод __le__: метод определяет поведение оператора "меньше или равно" <=. Он использует методы __eq__ и __lt__:
    def __le__(self, other):
        return self.__eq__(other) or self.__lt__(other)
#Метод __gt__: определяет поведение оператора "больше чем" >. Он использует метод __le__. Метод возвращает True, если текущий объект не меньше или равен other (используя __le__), что эквивалентно тому, что он больше.
    def __gt__(self, other):
        return not self.__le__(other)
#Метод __ge__: Этот метод определяет поведение оператора "больше или равно" >=. Он использует метод __lt__. Метод возвращает True, если текущий объект не меньше other (используя __lt__), что эквивалентно тому, что он больше или равен.
    def __ge__(self, other):
        return not self.__lt__(other)
#Метод __ne__: Этот метод определяет поведение оператора "не равен" (!=) для объектов класса. Он использует метод __eq__, который отвечает за проверку на равенство (==)
    def __ne__(self, other):
        return not self.__eq__(other)


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2)

h1 = h1 + 10
print(h1)
print(h1 == h2)

h1 += 10
print(h1)

h2 = 10 + h2
print(h2)

print(h1 > h2)
print(h1 >= h2)
print(h1 < h2)
print(h1 <= h2)
print(h1 != h2)
