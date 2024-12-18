import io
import pprint
class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'


    def get_products(self):
        file = open(self.__file_name, 'r', encoding='utf-8')
        products = file.read()
        file.close()
        return products

    def add(self, *products):
        current_products = self.get_products().split('\n')
        file = open(self.__file_name, 'a', encoding='utf-8')
        print(file.readable())
        print(file.writable())
        print(file.seekable())
        print(file.tell())
        print(file.name)
        print(file.closed)
        print(file.buffer)
        print(file.encoding)
        print(file.line_buffering)
        print(file.mode)
        print(file.newlines)
        print(file.fileno())
        print(file.isatty())
        print(file.tell())
        for product in products:
            if product.__str__() not in current_products:
                file.write(product.__str__() + '\n')
            else:
                print(f'Продукт {product.name}, {product.weight}, {product.category} уже есть в магазине')
        file.close()

'''
#используя метод with
    def get_products(self):
            with open(self.__file_name, 'r', encoding='utf-8') as file:
                return file.read()

    def add(self, *products):
            current_products = self.get_products().split('\n')
            with open(self.__file_name, 'a', encoding='utf-8') as file:
                for product in products:
                    if product.__str__() not in current_products:
                        file.write(product.__str__() + '\n')
                    else:
                        print(f'Продукт {product.name}, {product.weight}, {product.category} уже есть в магазине')'''



s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
print(p2)  # __str__

s1.add(p1, p2, p3)
print(s1.get_products())