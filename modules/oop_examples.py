
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