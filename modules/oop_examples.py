from modules.color_console import type_color_decorator, debug
from modules.color_in_consol import WHITE


class Car:
    def __init__(self, brand, wheels, model):
        self.brand = brand
        self.wheels = wheels
        self.model = model
    def description(self):
        return f'{self.brand} {self.model} mit {self.wheels} Rädern'


#mehre objekt
#objekt speicheren
#vererbung einbauen

class Book:#Vererbung (inheritance) beschreibt eine Spezialisierung.
    pass

class EBook(Book):#Ein EBook ist ein Book.
    pass

class Author:
    pass

class Book:#Komposition (composition) beschreibt Aufbau aus Teilen.
    def __init__(self):
        self.author = Author() #Ein Book hat einen Author.


class StorageStrategy:
    def save(self, book):
        pass

class FileStorage(StorageStrategy):
    ...

class BookRepository:# Repository hat eine Speicherstrategie → austauschbar ohne Umbau.
    def __init__(self, storage):
        self.storage = storage
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[0;31m'
ENDC = '\033[0m'

# from color import colored_class
# @colored_class
class Product:
    count = 0
    def __init__(self, name, price):

        self._name = name
        self._price = price
        self._other = []
        # Product.count += 1
        # self.id = Product.count
        self.id = Product.get_no()

    @type_color_decorator
    def get_name(self):
        return self._name

    #@debug
    @type_color_decorator
    def get_price(self):
        return self._price


    def set_price(self, price):
        self._price = price

    #@type_color_decorator

    @classmethod
    def get_no(cls):
        cls.count += 1
        return cls.count

class ProductHelper:

    @staticmethod # @staticmethod verhält sich wie eine ganz normale Funktion, kein self , cls. und kann direkt über die Klasse aufgerufen werden
    def add(x, y):
        """Addiert zwei Zahlen"""
        return x + y

    @staticmethod
    def greet(name):
        """Gibt eine Begrüßung zurück"""
        return f"Hello, {name}!"


auto = Product("Auto", 100)

print(auto.get_name())
print(auto.get_price())

auto.set_price(200)

print(auto.get_price())

print(auto.get_price())


pc = Product("LapTop", 300)

print(pc.get_name())
print(Product.get_price(pc))
print(Product.get_no())
print(ProductHelper.add(0,2))

tool = Product("Tool", 100)
tool3 = Product("Tool", 100)
tool2 = Product("Tool", 100)
print(Product.get_no()) #+1
tool4 = Product("Tool", 100)
tool5 = Product("Tool", 100)
print(pc.get_no())
