class Collection:
    stamps = 2

    def __init__(self, stuff):
        self.stuff = stuff

    def dispose(self):
        del self.stuff

binder = Collection(1)
print(binder.__dict__)
binder.dispose()

print('stuff' in binder.__dict__)
print(len(binder.__dict__) > 0)
print('stamps' in Collection.__dict__)
print(len(binder.__dict__) != len(Collection.__dict__))


import abc

#print(dir(abc))
print(abc.ABC.__dict__)
#@abc.abstractclass
class BluePrint(abc.ABC): # Eine abstrakte Klasse wird einfach durch Vererbung von abc.ABC definiert
    @abc.abstractmethod # jede Unterklasse diese Methode implementieren muss.
    def hello(self):
        pass

class WhitePool(BluePrint):
    def hello(self):
        print('Welcome to the White Pool!')

wp = WhitePool()
wp.hello()

import abc

# Richtige Definition einer abstrakten Klasse
class BluePrint(abc.ABC):
    @abc.abstractmethod
    def hello(self):
        pass

# Unterklasse implementiert die abstrakte Methode
class WhitePool(BluePrint):
    def hello(self):
        print('Welcome to the White Pool!')

# Instanziierung und Aufruf
wp = WhitePool()
wp.hello()

from abc import ABC, abstractmethod # abc steht für Abstract Base Classes.

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("Engine started!")

c = Car()
c.start_engine()  # Ausgabe: Engine started!
print(Car.__dict__)
print(Vehicle.__dict__)
print(ABC.__dict__)
print(dir(abc))
print(dir(ABC))
print(help(ABC))

my_list = [1, 2, 3]
try:
    my_list[3] = my_list[2]
except BaseException as error: # list assignment index out of range "IndexError"
    print(error)

print(len([i for i in range(0, -2,-1)]))

class A:
    def __init__(self):
        self.a = 1

class B(A):
    def __init__(self): #Wenn B.__init__ überschrieben wird, müssen wir A.__init__ manuell aufrufen
        # Put selected line here.
        A.__init__(self)
        self.b = 2


def attic(x):
    assert x != 0
    return 1 / x

def floor(x):
    try:
        attic(x)
    except:
        raise

try:
    x = attic(0) # AssertionError
except RuntimeError:
    x = -3
except:
    x = -2
else:
    x = -1
print(x)

