from modules.decorators_dome import type_color_decorator, debug


# ---------------------------------------------------------------------------
# Vererbung (Inheritance)
# ---------------------------------------------------------------------------

class Book:  # Vererbung: Spezialisierung
    pass

class EBook(Book):  # EBook ist ein Book
    pass


# ---------------------------------------------------------------------------
# Komposition (Composition)
# ---------------------------------------------------------------------------

class Author:
    pass

class BookWithAuthor:  # Komposition: Book hat einen Author
    def __init__(self):
        self.author = Author()


# ---------------------------------------------------------------------------
# Strategy Pattern
# ---------------------------------------------------------------------------

class StorageStrategy:
    def save(self, book):
        pass

class FileStorage(StorageStrategy):
    ...

class BookRepository:  # Repository hat eine Speicherstrategie - austauschbar ohne Umbau
    def __init__(self, storage):
        self.storage = storage


# ---------------------------------------------------------------------------
# Car - einfache Klasse
# ---------------------------------------------------------------------------

class Car:
    def __init__(self, brand, wheels, model):
        self.brand = brand
        self.wheels = wheels
        self.model = model

    def description(self):
        return f'{self.brand} {self.model} mit {self.wheels} Raedern'


# ---------------------------------------------------------------------------
# Product - Klassenmethode, Decorator, Static
# ---------------------------------------------------------------------------

class Product:
    count = 0

    def __init__(self, name, price):
        self._name = name
        self._price = price
        self._other = []
        self.id = Product.get_no()

    @type_color_decorator
    def get_name(self):
        return self._name

    @type_color_decorator
    def get_price(self):
        return self._price

    def set_price(self, price):
        self._price = price

    @classmethod
    def get_no(cls):
        cls.count += 1
        return cls.count


class ProductHelper:

    @staticmethod
    def add(x, y):
        """Addiert zwei Zahlen"""
        return x + y

    @staticmethod
    def greet(name):
        """Gibt eine Begruessung zurueck"""
        return f"Hello, {name}!"


# ---------------------------------------------------------------------------

if __name__ == "__main__":
    auto = Product("Auto", 100)
    print(auto.get_name())
    print(auto.get_price())

    auto.set_price(200)
    print(auto.get_price())

    pc = Product("LapTop", 300)
    print(pc.get_name())
    print(Product.get_price(pc))
    print(Product.get_no())
    print(ProductHelper.add(0, 2))

    tool = Product("Tool", 100)
    print(Product.get_no())

    car = Car("Audi", 4, "A4")
    print(car.description())