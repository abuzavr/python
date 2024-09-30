class Example:
    def __new__(cls, *args, **kwargs):
        print(args)
        print(kwargs)
        return object.__new__(cls)

    def __init__(self, first, second, third):
        print(first)
        print(second)
        print(third)

ex = Example('data', second=25, third=3.14)


class User:
    __instance = None
    def __new__(cls, *args, **kwargs):
        print('Darova ya v __new__')
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            return cls.__instance


    def __init__(self, *args, **kwargs):
        print('Darova ya v __init__')
        self.args = args
        self.kwargs = kwargs
        self.name = kwargs.get('name')
        self.age = kwargs.get('age')
        self.city = kwargs.get('city')
        for key, values in kwargs.items():
            setattr(self, key, values)

other = [1,2,3]
user = {'name': 'abu', 'age': 32, 'city': 'Oryol', 'gender': 'male', 'other': other}

User1 = User(*other, **user)
print(User1.args)
print(User1.kwargs)
print(User.__mro__)
print(User1)
print(User1.name)
print(User1.age)
print(User1.city)
print(User1.gender)
print(User1.other)

User1 = User()
User2 = User()
print(User1 is User2)
print(id(User1), id(User2))'''