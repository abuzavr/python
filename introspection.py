# Функция для анализа (интроспекции) объекта

def introspection_info(obj):
    """
    Анализирует объект и возвращает информацию о его свойствах, методах, типе и модуле.

    Args:
        obj: Любой объект для анализа.

    Returns:
        dict: Словарь с описанием объекта.
    """
    # Собираем все "атрибуты" объекта (то, что не является функциями/методами)
    # Исключаем специальные служебные атрибуты, которые начинаются с "__"
    attributes = [
        attr for attr in dir(obj)
        if not callable(getattr(obj, attr)) and not attr.startswith("__")
    ]

    # Собираем все "методы" объекта (то, что можно вызывать)
    # Исключаем служебные методы, которые начинаются с "__"
    methods = [
        method for method in dir(obj)
        if callable(getattr(obj, method)) and not method.startswith("__")
    ]

    # Создаем словарь с подробной информацией о переданном объекте
    info = {
        'type': type(obj).__name__,  # Тип объекта, например, "int", "str", "CustomClass"
        'attributes': attributes,  # Список обычных атрибутов объекта (не функций)
        'methods': methods,  # Список методов объекта (то, что можно вызывать)
        'module': getattr(obj, '__module__', 'built-in'),  # Модуль, в котором определен объект
        'docstring': obj.__doc__  # Описание объекта (докстринг), если оно есть
    }

    return info


# Пример 1: Работа с обычным числом
number_info = introspection_info(42)  # Передаем число для анализа
print("Информация о числе:")
print(number_info)


# Пример 2: Работа с пользовательским классом
class CustomClass:
    """
    Это пример пользовательского класса для демонстрации работы функции.
    """

    def __init__(self, value):
        # Создаем атрибут объекта и сохраняем переданное значение
        self.value = value

    def custom_method(self):
        """
        Пример метода, который возвращает строку с текущим значением.
        """
        return f"Value is {self.value}"


# Создаем объект класса с переданным значением
custom_object = CustomClass(10)

# Анализируем пользовательский объект
custom_object_info = introspection_info(custom_object)
print("\nИнформация о пользовательском объекте:")
print(custom_object_info)
