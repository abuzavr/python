def add_everything_up(a, b):
    """Складывает числа(int, float) и строки(str)"""
    try:
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return round(a + b, 3)
        elif isinstance(a, str) and isinstance(b, str):
            return a + b
        else:
            return str(a) + str(b)
    except TypeError as exc:
        print(f'Ошибочка вышла: {exc}')


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))


